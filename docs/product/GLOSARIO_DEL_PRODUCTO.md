# Glosario del Producto

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión:** 1.0

---

# 1. Introducción

## Objetivo

Este documento define el vocabulario oficial utilizado en Nexa Knowledge AI.

Su finalidad es garantizar que usuarios, administradores, desarrolladores, personal de soporte y Agentes IA utilicen una terminología consistente en toda la plataforma.

Todas las definiciones incluidas en este glosario constituyen la referencia oficial del producto.

---

# 2. Alcance

El glosario aplica a:

- Documentación funcional.
- Documentación técnica.
- Interfaces de usuario.
- APIs.
- Manuales.
- Centro de ayuda.
- FAQ.
- Agentes IA.
- Material comercial.
- Comunicaciones internas.

---

# 3. Términos Oficiales

## Agente IA

Entidad inteligente configurable capaz de comprender consultas en lenguaje natural, recuperar información autorizada y generar respuestas fundamentadas utilizando modelos de lenguaje y mecanismos de recuperación de contexto.

Un Agente IA puede especializarse en un dominio específico como Recursos Humanos, Ingeniería, Soporte o Legal.

---

## Auditoría

Registro cronológico de los eventos relevantes ocurridos dentro de la plataforma.

La auditoría permite garantizar trazabilidad, cumplimiento normativo y análisis de seguridad.

---

## Base de Conocimiento

Conjunto estructurado de documentos, fragmentos, metadatos y representaciones vectoriales disponibles para responder consultas mediante Inteligencia Artificial.

---

## Base Vectorial

Sistema especializado en almacenar embeddings y realizar búsquedas por similitud semántica.

La plataforma soporta múltiples proveedores de bases vectoriales.

---

## Chunk

Fragmento de contenido generado a partir de un documento durante el proceso de indexación.

Cada chunk representa una unidad mínima de conocimiento utilizada durante la recuperación de contexto.

---

## Chunking

Proceso mediante el cual un documento es dividido en múltiples fragmentos para facilitar la búsqueda semántica y mejorar la calidad de las respuestas generadas por IA.

---

## Colección

Agrupación lógica de documentos relacionados.

Las colecciones permiten organizar el conocimiento por temas, áreas o proyectos.

---

## Consulta

Pregunta realizada por un usuario a un Agente IA utilizando lenguaje natural.

Cada consulta forma parte de una conversación.

---

## Contexto

Conjunto de fragmentos recuperados por el sistema para responder una consulta.

El contexto es utilizado como entrada para el modelo de lenguaje.

---

## Conversación

Sesión continua de interacción entre un usuario y un Agente IA.

Puede contener múltiples consultas y respuestas relacionadas.

---

## Documento

Archivo cargado por una organización que contiene información susceptible de ser procesada e incorporada a la Base de Conocimiento.

---

## Embedding

Representación numérica de un fragmento de texto utilizada para medir similitud semántica.

Los embeddings permiten recuperar información relacionada aunque no existan coincidencias exactas entre palabras.

---

## Fuente

Documento o fragmento específico utilizado como respaldo para generar una respuesta.

Las fuentes permiten verificar el origen de la información presentada por el Agente IA.

---

## Hallucination (Alucinación)

Respuesta generada por un modelo de lenguaje que no está respaldada por la información disponible en la Base de Conocimiento o por herramientas autorizadas.

Nexa Knowledge AI implementa mecanismos para minimizar este comportamiento.

---

## Indexación

Proceso completo mediante el cual un documento es transformado en conocimiento consultable.

Incluye extracción, limpieza, chunking, generación de embeddings y almacenamiento vectorial.

---

## LLM (Large Language Model)

Modelo de Inteligencia Artificial entrenado para comprender y generar lenguaje natural.

El LLM utiliza el contexto recuperado para elaborar respuestas fundamentadas.

---

## Metadatos

Información descriptiva asociada a un recurso.

Ejemplos:

- Autor.
- Fecha de creación.
- Idioma.
- Etiquetas.
- Versión.
- Tipo de documento.

---

## Modelo de Lenguaje

Modelo de Inteligencia Artificial seleccionado para responder consultas.

La plataforma puede utilizar diferentes proveedores según la configuración de la organización.

---

## Organización

Empresa cliente que utiliza Nexa Knowledge AI.

Cada organización mantiene aislamiento completo respecto a las demás.

---

## Permiso

Autorización que permite ejecutar una operación específica sobre un recurso determinado.

---

## Prompt

Conjunto de instrucciones enviadas al modelo de lenguaje para generar una respuesta.

Incluye la consulta del usuario, el contexto recuperado y las instrucciones del Agente IA.

---

## RAG (Retrieval-Augmented Generation)

Arquitectura que combina recuperación de información con modelos de lenguaje para producir respuestas fundamentadas en documentos autorizados.

Es el mecanismo principal utilizado por Nexa Knowledge AI.

---

## Respuesta

Contenido generado por un Agente IA como resultado de una consulta.

Una respuesta puede incluir texto, referencias, fuentes y nivel de confianza.

---

## Rol

Conjunto de permisos asignados a un usuario.

Los roles determinan las operaciones que un usuario puede realizar.

---

## Vector Search

Proceso mediante el cual el sistema identifica los embeddings más similares a una consulta para recuperar información relevante.

---

## Workspace

Espacio de trabajo perteneciente a una organización.

Permite organizar documentos, usuarios, colecciones y Agentes IA según áreas funcionales o proyectos.

---

# 4. Acrónimos

| Acrónimo | Significado |
|----------|-------------|
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| ACL | Access Control List |
| DDD | Domain-Driven Design |
| ETL | Extract, Transform, Load |
| IAM | Identity and Access Management |
| JSON | JavaScript Object Notation |
| JWT | JSON Web Token |
| LLM | Large Language Model |
| MFA | Multi-Factor Authentication |
| OCR | Optical Character Recognition |
| RAG | Retrieval-Augmented Generation |
| REST | Representational State Transfer |
| RBAC | Role-Based Access Control |
| SSO | Single Sign-On |
| UI | User Interface |
| UX | User Experience |

---

# 5. Términos Reservados

Los siguientes nombres forman parte de la terminología oficial de Nexa Knowledge AI y deberán utilizarse de manera consistente en toda la documentación y en la interfaz del producto:

- Organización
- Workspace
- Colección
- Documento
- Base de Conocimiento
- Agente IA
- Conversación
- Consulta
- Respuesta
- Fuente
- Embedding
- Chunk
- Prompt
- Modelo de Lenguaje
- Base Vectorial

No deberán utilizarse sinónimos cuando exista un término oficial definido en este glosario.

---

# 6. Relación con otros documentos

Este glosario complementa los siguientes documentos:

- Base de Conocimiento del Producto.
- Arquitectura Funcional.
- Modelo de Dominio.
- Catálogo de Funcionalidades.
- Casos de Uso.
- Reglas de Negocio.
- Modelo de Permisos.

Toda la documentación futura deberá utilizar las definiciones establecidas en este documento para mantener un lenguaje ubicuo y consistente en toda la plataforma.