# app.py
"""
Interfaz Gradio del Agente de Conocimiento Corporativo.

Dos pestañas:
    1. "Cargar documentos": sube archivos (PDF, DOCX, XLSX, CSV, PPTX, MD, JSON, HTML)
       y construye/actualiza el índice vectorial.
    2. "Preguntar al agente": escribe una pregunta y observa en tiempo real los
       pasos que sigue el grafo de LangGraph (recuperar -> evaluar -> generar),
       igual que en el ejemplo original que transmitía el progreso paso a paso.
"""
import os
import uuid
import shutil
import gradio as gr

from ingestion import load_all_documents, build_vectorstore

# 'docs/' contiene la documentación curada y organizada por categoría de la empresa
# (docs/company/, docs/product/, docs/ai/, docs/hr/, etc.). 'sample_docs/' es para
# archivos sueltos que se suban manualmente desde esta interfaz. El índice combina ambas.
CURATED_FOLDER = "docs"
UPLOAD_FOLDER = "sample_docs"
INDEX_PATH = "vectorstore_index"


def ingest_files(files):
    if not files:
        return "⚠️ No se seleccionó ningún archivo."
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    for f in files:
        shutil.copy(f.name, os.path.join(UPLOAD_FOLDER, os.path.basename(f.name)))

    docs = load_all_documents([CURATED_FOLDER, UPLOAD_FOLDER])
    if not docs:
        return "⚠️ No se pudo extraer contenido de los archivos cargados."

    build_vectorstore(docs, persist_path=INDEX_PATH)
    return f"✅ Índice actualizado con {len(docs)} fragmento(s) provenientes de '{CURATED_FOLDER}/' y '{UPLOAD_FOLDER}/'."


def ask_agent(question):
    if not question or not question.strip():
        yield "", "⚠️ Escribe una pregunta primero.", ""
        return

    # Se importa aquí para tomar siempre la versión más reciente del índice.
    from agent import graph

    thread_config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    initial_state = {
        "question": question,
        "documents": [],
        "sources": [],
        "generation": "",
        "needs_web_search": "",
        "steps": [],
    }

    trace = ""
    final_answer = ""
    final_sources = []
    for s in graph.stream(initial_state, thread_config):
        step_output = list(s.values())[0]
        if step_output.get("steps"):
            trace = "\n".join(step_output["steps"])
        if step_output.get("generation"):
            final_answer = step_output["generation"]
        if step_output.get("sources"):
            final_sources = step_output["sources"]
        yield trace, final_answer, ""

    sources_text = "\n".join(f"- {s}" for s in sorted(set(final_sources))) if final_sources else "Sin fuentes."
    yield trace, final_answer, sources_text


with gr.Blocks(theme=gr.themes.Default(spacing_size="sm", text_size="sm")) as demo:
    gr.Markdown("# 🤖 Agente de Conocimiento Corporativo")
    gr.Markdown(
        "Sube tus documentos internos (PDF, DOCX, XLSX, CSV, PPTX, Markdown, JSON, HTML) "
        "y pregúntale al agente en lenguaje natural, sin necesidad de abrir ningún archivo."
    )

    with gr.Tab("📚 Cargar documentos"):
        file_uploader = gr.File(label="Documentos internos", file_count="multiple")
        ingest_button = gr.Button("Procesar y crear índice", variant="primary")
        ingest_status = gr.Textbox(label="Estado de la ingestión", interactive=False)
        ingest_button.click(fn=ingest_files, inputs=file_uploader, outputs=ingest_status)
        gr.Markdown(
            "_La documentación curada de la empresa vive en `docs/` (organizada por "
            "categoría: `company/`, `product/`, `ai/`, `hr/`, etc.) y se incluye siempre "
            "en el índice. Aquí puedes subir documentos adicionales sueltos, que se "
            "guardan en `sample_docs/` y se combinan automáticamente con `docs/`._"
        )

    with gr.Tab("💬 Preguntar al agente"):
        question_box = gr.Textbox(
            label="Tu pregunta",
            placeholder="Ej: ¿Cuál fue el producto más vendido en diciembre de 2015?",
        )
        ask_button = gr.Button("Preguntar", variant="primary")
        trace_box = gr.Textbox(label="Trazabilidad del agente (pasos del grafo)", lines=6)
        answer_box = gr.Textbox(label="Respuesta", lines=8)
        sources_box = gr.Textbox(label="Fuentes utilizadas", lines=4)

        ask_button.click(fn=ask_agent, inputs=question_box, outputs=[trace_box, answer_box, sources_box])

if __name__ == "__main__":
    demo.launch(share=False)
