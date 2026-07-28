# 🤖 Agente de Conocimiento Corporativo (Alura Agentes Challenge)

Agente de inteligencia artificial que permite a cualquier colaborador de una empresa
hacer preguntas en lenguaje natural sobre sus documentos internos (manuales, políticas,
informes, hojas de cálculo, etc.) y recibir respuestas directas, sin tener que abrir
ningún archivo.

Construido con **Python + LangChain + LangGraph + Gemini**, siguiendo el patrón de
grafo de agentes visto en el curso *"LangGraph: Orquestación de agentes y multiagentes"*.

---

## 🧩 Problema que resuelve

Empresas (fintechs, consultoras, startups) acumulan grandes volúmenes de documentos
—manuales, políticas, hojas de cálculo, informes— y sus colaboradores pierden horas
buscando información dentro de ellos. Este agente centraliza esos documentos en una
base de conocimiento conversacional, siempre disponible, que responde preguntas al
instante.

---

## 🏗️ Arquitectura

El proyecto tiene dos grandes componentes:

### 1. Ingestión de documentos (`ingestion.py`)
Lee documentos en múltiples formatos —**PDF, Word (.docx), Excel (.xlsx/.xls), CSV,
PowerPoint (.pptx), Markdown, JSON y HTML**—, los normaliza a un formato común
(`Document` de LangChain), los divide en fragmentos (chunks) y genera embeddings
con el modelo `gemini-embedding-001` de Gemini. Estos embeddings se guardan en un
índice vectorial **FAISS** en disco (`vectorstore_index/`).

### 2. Agente conversacional con LangGraph (`agent.py`)
Implementa un grafo de tipo **Corrective RAG (CRAG)**:

```
        ┌────────────┐
        │  retrieve  │  <- busca los fragmentos más relevantes en FAISS
        └─────┬──────┘
              │
        ┌─────▼───────────┐
        │ grade_documents  │  <- un LLM evalúa si los fragmentos alcanzan
        └─────┬────────────┘     para responder la pregunta
              │
      ┌───────┴────────┐
      │                │
 (no alcanzan)     (alcanzan)
      │                │
┌─────▼──────┐         │
│transform_  │         │
│  query     │         │
└─────┬──────┘         │
      │                │
┌─────▼──────┐         │
│web_search  │         │   (búsqueda de respaldo con Tavily,
│ (Tavily)   │         │    solo si se configuró TAVILY_API_KEY)
└─────┬──────┘         │
      │                │
      └───────┬────────┘
              │
        ┌─────▼──────┐
        │  generate  │  <- redacta la respuesta final citando la fuente
        └────────────┘
```

Cada nodo del grafo va registrando su propio paso (`steps`), por lo que la interfaz
puede mostrar en tiempo real qué está haciendo el agente (recuperar → evaluar →
generar), igual que el patrón de streaming del ejemplo original del curso.

El estado del grafo se persiste con `SqliteSaver` (checkpoints por conversación),
igual que en el ejemplo base del curso.

### 3. Interfaz (`app.py`)
Aplicación **Gradio** con dos pestañas:
- **Cargar documentos**: sube archivos y reconstruye el índice vectorial.
- **Preguntar al agente**: escribe una pregunta y observa la traza del razonamiento,
  la respuesta final y las fuentes utilizadas.

---

## 💬 Ejemplos de preguntas y respuestas

Usando los documentos de ejemplo incluidos en `sample_docs/`:

| Pregunta | Fuente | Respuesta esperada |
|---|---|---|
| ¿Cuál fue el producto más vendido en diciembre de 2015? | `ventas_2015.csv` | Plan Pro, con 780 unidades vendidas e ingresos de USD 23.400 |
| ¿Qué lenguajes de programación se usan en el back-end de la plataforma de ventas? | `faq_tecnologia.json` | Python (FastAPI), PostgreSQL y Redis, con Celery para tareas asíncronas |
| ¿Cuántos días de vacaciones tengo por año? | `politica_rrhh.md` | 15 días hábiles por año trabajado |
| ¿Cuánto dura el proceso de onboarding? | `politica_rrhh.md` | 2 semanas, con actividades detalladas por día/semana |

Si la pregunta no puede responderse con los documentos internos y se configuró
`TAVILY_API_KEY`, el agente reformula la pregunta y busca en la web como respaldo,
indicándolo explícitamente en la respuesta.

---

## ⚙️ Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd agente-corporativo
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
```bash
cp .env.example .env
```
Edita `.env` y agrega tu `GEMINI_API_KEY` (obligatoria) y, si quieres respaldo con
búsqueda web, tu `TAVILY_API_KEY` (opcional).

### 4. Generar el índice vectorial con los documentos
El script procesa automáticamente `docs/` (documentación curada de la empresa, organizada
por categoría: `docs/company/`, `docs/product/`, `docs/ai/`, `docs/hr/`, etc.) y `sample_docs/`
(archivos sueltos o de prueba), combinando ambas carpetas en un solo índice. Formatos
soportados: PDF, DOCX, XLSX, CSV, PPTX, Markdown, JSON y HTML.
```bash
python ingestion.py
```

### 5. Ejecutar la aplicación
```bash
python app.py
```
Esto abrirá una interfaz web local donde puedes cargar más documentos o preguntarle
directamente al agente.

---

## ☁️ Despliegue en la nube

Este proyecto está pensado para desplegarse en servicios como **Hugging Face Spaces**,
**Render** o **Google Cloud Run**. Pasos generales:
1. Sube el repositorio a GitHub.
2. Crea un nuevo Space/servicio conectado al repositorio.
3. Configura las variables de entorno (`GEMINI_API_KEY`, `TAVILY_API_KEY`) como
   secretos del servicio.
4. Define el comando de arranque: `python app.py`.

> 📸 *Agrega aquí una imagen o video del agente ejecutándose en la nube, como pide
> el desafío.*

---

## 🛠️ Tecnologías utilizadas

- **Python** — lenguaje principal
- **LangChain** — carga y división de documentos, embeddings
- **LangGraph** — orquestación del agente como grafo de estados
- **Gemini (Google Generative AI)** — modelo de lenguaje y embeddings
- **FAISS** — índice vectorial para búsqueda semántica
- **Gradio** — interfaz de usuario
- **Tavily** (opcional) — búsqueda web de respaldo
- **pypdf, python-docx, python-pptx, pandas, BeautifulSoup** — lectores de cada
  formato de documento

---

## 📂 Estructura del repositorio

```
agente-corporativo/
├── app.py                  # Interfaz Gradio
├── agent.py                # Grafo LangGraph del agente (Corrective RAG)
├── ingestion.py             # Carga de documentos + creación del índice FAISS
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── docs/                    # Documentación curada de la empresa, por categoría
│   ├── company/
│   ├── product/
│   ├── user-guide/
│   ├── ai/
│   ├── api/
│   ├── admin/
│   ├── security/
│   ├── engineering/
│   ├── devops/
│   ├── support/
│   ├── business/
│   ├── legal/
│   └── hr/
└── sample_docs/             # Archivos sueltos / de prueba, subidos desde la interfaz
```

Cada fragmento recuperado del índice conserva dos metadatos útiles: `source` (ruta relativa,
ej. `product/Roadmap del Producto.md`) y `area` (la subcarpeta de primer nivel, ej. `product`),
lo que permite escalar de 40 a 97 documentos sin cambiar el código de ingestión — solo hay
que agregar archivos dentro de las subcarpetas correspondientes de `docs/`.

---

## ✅ Estado de la validación

- [x] Lee y procesa múltiples formatos de documento (PDF, Word, Excel, PowerPoint,
      Markdown, CSV, JSON, HTML).
- [x] Responde preguntas en lenguaje natural con base en esos documentos.
- [x] Interfaz accesible para cualquier colaborador (sin restricciones de acceso).
- [x] Documentación con arquitectura, ejemplos e instrucciones de ejecución.
