# agent.py
"""
Agente de IA corporativo — arquitectura Corrective RAG (CRAG) con LangGraph.

Idea general:
    1. retrieve            -> busca fragmentos relevantes en el índice vectorial
                               construido a partir de los documentos internos.
    2. grade_documents     -> un LLM evalúa si esos fragmentos alcanzan para
                               responder la pregunta.
    3. (condicional)
         - si alcanzan          -> generate
         - si NO alcanzan       -> transform_query -> web_search -> generate
           (fallback opcional con Tavily, solo si hay TAVILY_API_KEY)
    4. generate            -> redacta la respuesta final citando la fuente.

Esta estructura reutiliza el mismo patrón de grafo con nodos + checkpointer
SQLite + Gemini que ya se usaba en el ejemplo `new_backend.py` del curso,
pero orientado a responder preguntas sobre documentos internos en lugar de
escribir redacciones.
"""
import os
from dotenv import load_dotenv
from typing import TypedDict, List
from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

from ingestion import load_vectorstore

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
USE_WEB_FALLBACK = bool(TAVILY_API_KEY)

if USE_WEB_FALLBACK:
    from tavily import TavilyClient
    tavily = TavilyClient(api_key=TAVILY_API_KEY)

# --- Modelo de lenguaje ---
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, google_api_key=GEMINI_API_KEY)

# --- Checkpointer (memoria de conversación por hilo) ---
conn = sqlite3.connect("checkpoints.db", check_same_thread=False)
memory = SqliteSaver(conn)

# --- Índice vectorial con los documentos internos ---
try:
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 8})
except Exception as e:
    print(f"⚠️  No se encontró un índice vectorial. Ejecuta 'python ingestion.py' primero. ({e})")
    retriever = None


# --------------------------------------------------------------------------
# Estado del agente
# --------------------------------------------------------------------------
class AgentState(TypedDict):
    question: str
    documents: List[str]
    sources: List[str]
    generation: str
    needs_web_search: str
    steps: List[str]


class GradeDocuments(BaseModel):
    binary_score: str = Field(description="Los documentos son relevantes para responder la pregunta: 'si' o 'no'")


class RewrittenQuery(BaseModel):
    query: str = Field(description="Pregunta reescrita, optimizada para una búsqueda web")


# --------------------------------------------------------------------------
# Prompts
# --------------------------------------------------------------------------
GRADE_PROMPT = """Eres un evaluador que determina si un conjunto de fragmentos de documentos \
internos de una empresa contiene información RELACIONADA con la pregunta de un colaborador, \
aunque sea parcial o incompleta. \
Responde 'si' si al menos uno de los fragmentos toca el tema de la pregunta (aunque la respuesta \
final termine siendo parcial). Responde 'no' ÚNICAMENTE si ninguno de los fragmentos tiene relación \
alguna con el tema de la pregunta."""

GENERATE_PROMPT = """Eres el asistente de conocimiento interno de una empresa. Tu tarea es responder \
la pregunta de un colaborador de forma clara, directa y en español, basándote ÚNICAMENTE en el \
siguiente contexto extraído de los documentos internos (o de la búsqueda web de respaldo, si aplica). \
Prioriza siempre los datos de los documentos internos por sobre los resultados de búsqueda web. \
Si el contexto incluye una tabla de datos (por ejemplo ventas por mes), haz los cálculos o \
comparaciones necesarias (sumas, máximos, etc.) tú mismo a partir de esos datos. \
Si el contexto solo cubre parcialmente el período o el tema de la pregunta, responde con lo que sí \
se puede determinar y aclara explícitamente qué parte falta, en lugar de inventar información. \
Menciona el documento de origen cuando sea posible.

Contexto:
{context}"""

REWRITE_PROMPT = """Reescribe la siguiente pregunta interna de una empresa como una consulta \
de búsqueda web efectiva y concisa, conservando la intención original."""


# --------------------------------------------------------------------------
# Nodos del grafo
# --------------------------------------------------------------------------
def retrieve_node(state: AgentState):
    if retriever is None:
        return {
            "documents": [],
            "sources": [],
            "steps": state.get("steps", []) + ["⚠️ No hay índice vectorial disponible (ejecuta ingestion.py)"],
        }
    docs = retriever.invoke(state["question"])
    contents = [d.page_content for d in docs]
    sources = [d.metadata.get("source", "desconocido") for d in docs]
    return {
        "documents": contents,
        "sources": sources,
        "steps": state.get("steps", []) + [f"🔎 Recuperados {len(contents)} fragmento(s) de los documentos internos"],
    }


def grade_documents_node(state: AgentState):
    if not state["documents"]:
        return {"needs_web_search": "si", "steps": state.get("steps", []) + ["🧐 No hay documentos que evaluar"]}

    context = "\n\n".join(state["documents"])
    structured_model = model.with_structured_output(GradeDocuments)
    result = structured_model.invoke([
        SystemMessage(content=GRADE_PROMPT),
        HumanMessage(content=f"Pregunta: {state['question']}\n\nDocumentos:\n{context}"),
    ])
    needs_web = "no" if result.binary_score.strip().lower().startswith("s") else "si"
    etiqueta = "suficientes ✅" if needs_web == "no" else "insuficientes 🌐"
    return {
        "needs_web_search": needs_web,
        "steps": state.get("steps", []) + [f"🧐 Evaluación de relevancia: documentos {etiqueta}"],
    }


def transform_query_node(state: AgentState):
    structured_model = model.with_structured_output(RewrittenQuery)
    result = structured_model.invoke([
        SystemMessage(content=REWRITE_PROMPT),
        HumanMessage(content=state["question"]),
    ])
    return {
        "question": result.query,
        "steps": state.get("steps", []) + [f"✏️ Pregunta reescrita para búsqueda web: {result.query}"],
    }


def web_search_node(state: AgentState):
    if not USE_WEB_FALLBACK:
        return {"steps": state.get("steps", []) + ["⚠️ TAVILY_API_KEY no configurada: se omite la búsqueda web"]}
    response = tavily.search(query=state["question"], max_results=3)
    web_content = [r["content"] for r in response["results"]]
    web_sources = [r.get("url", "web") for r in response["results"]]
    return {
        "documents": state["documents"] + web_content,
        "sources": state["sources"] + web_sources,
        "steps": state.get("steps", []) + [f"🌐 Se agregaron {len(web_content)} resultado(s) de búsqueda web"],
    }


def generate_node(state: AgentState):
    context = "\n\n---\n\n".join(state["documents"]) if state["documents"] else "Sin contexto disponible."
    messages = [
        SystemMessage(content=GENERATE_PROMPT.format(context=context)),
        HumanMessage(content=state["question"]),
    ]
    response = model.invoke(messages)
    return {
        "generation": response.content,
        "steps": state.get("steps", []) + ["✍️ Respuesta generada"],
    }


def decide_next_step(state: AgentState):
    if state.get("needs_web_search") == "si" and USE_WEB_FALLBACK:
        return "transform_query"
    return "generate"


# --------------------------------------------------------------------------
# Construcción del grafo
# --------------------------------------------------------------------------
builder = StateGraph(AgentState)
builder.add_node("retrieve", retrieve_node)
builder.add_node("grade_documents", grade_documents_node)
builder.add_node("transform_query", transform_query_node)
builder.add_node("web_search", web_search_node)
builder.add_node("generate", generate_node)

builder.set_entry_point("retrieve")
builder.add_edge("retrieve", "grade_documents")
builder.add_conditional_edges(
    "grade_documents",
    decide_next_step,
    {"transform_query": "transform_query", "generate": "generate"},
)
builder.add_edge("transform_query", "web_search")
builder.add_edge("web_search", "generate")
builder.add_edge("generate", END)

graph = builder.compile(checkpointer=memory)

# Ejemplo de uso directo (sin Gradio):
# thread = {"configurable": {"thread_id": "1"}}
# for s in graph.stream({
#     "question": "¿Cuál fue el producto más vendido en diciembre de 2015?",
#     "documents": [], "sources": [], "generation": "", "needs_web_search": "", "steps": []
# }, thread):
#     print(s)
