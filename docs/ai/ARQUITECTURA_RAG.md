# Arquitectura RAG

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

---

# 1. Introducción

## Objetivo

Este documento describe la arquitectura **Retrieval-Augmented Generation (RAG)** implementada por Nexa Knowledge AI.

Su propósito es explicar cómo la plataforma transforma documentos empresariales en conocimiento consultable y cómo los Agentes IA generan respuestas fundamentadas utilizando únicamente información autorizada.

Este documento sirve como referencia para los equipos de Ingeniería, Producto, Soporte y para cualquier persona que necesite comprender el funcionamiento interno del sistema de recuperación de conocimiento.

---

# 2. ¿Qué es RAG?

Retrieval-Augmented Generation (RAG) es una arquitectura que combina dos procesos independientes:

1. Recuperación de información relevante.
2. Generación de respuestas mediante un Modelo de Lenguaje (LLM).

A diferencia de un chatbot tradicional, un sistema RAG no depende únicamente del conocimiento del modelo de IA.

Antes de responder, recupera información desde la Base de Conocimiento de la organización y utiliza ese contexto para construir una respuesta fundamentada.

---

# 3. Objetivos de la arquitectura

La arquitectura RAG de Nexa Knowledge AI tiene los siguientes objetivos:

- Reducir las alucinaciones del modelo.
- Garantizar respuestas fundamentadas.
- Mantener trazabilidad documental.
- Respetar los permisos de acceso.
- Escalar a grandes volúmenes de información.
- Facilitar la actualización continua del conocimiento.
- Permitir el uso de múltiples modelos de IA.

---

# 4. Componentes principales

La arquitectura está compuesta por los siguientes componentes:

- Gestor de Documentos.
- Servicio de Procesamiento.
- Motor de Extracción de Texto.
- Servicio de Chunking.
- Generador de Embeddings.
- Base Vectorial.
- Recuperador de Contexto.
- Orquestador RAG.
- Modelo de Lenguaje (LLM).
- Servicio de Auditoría.
- Agente IA.

Cada componente cumple una función específica dentro del flujo de consulta.

---

# 5. Flujo general de la arquitectura

```
Documento

↓

Procesamiento

↓

Extracción de texto

↓

Normalización

↓

Chunking

↓

Embeddings

↓

Base Vectorial

↓

Consulta del usuario

↓

Embedding de la consulta

↓

Búsqueda semántica

↓

Recuperación de contexto

↓

Construcción del Prompt

↓

Modelo de Lenguaje

↓

Respuesta

↓

Fuentes documentales
```

---

# 6. Proceso de indexación

La indexación transforma documentos en conocimiento recuperable.

Las etapas son:

## 6.1 Recepción del documento

El archivo es cargado por un usuario autorizado.

Se validan:

- Formato.
- Tamaño.
- Permisos.
- Integridad.

---

## 6.2 Extracción

El contenido textual es extraído utilizando el procesador correspondiente al tipo de archivo.

Ejemplos:

- PDF.
- Word.
- Excel.
- PowerPoint.
- Markdown.
- Texto plano.

---

## 6.3 Limpieza

El contenido es normalizado.

Durante esta etapa pueden eliminarse:

- Espacios innecesarios.
- Caracteres inválidos.
- Encabezados repetitivos.
- Pies de página redundantes.
- Elementos sin valor semántico.

---

## 6.4 Chunking

El documento se divide en fragmentos independientes denominados **Chunks**.

Cada Chunk conserva:

- Identificador único.
- Documento de origen.
- Página o sección.
- Posición.
- Metadatos.

---

## 6.5 Generación de Embeddings

Cada Chunk es transformado en un vector numérico mediante un modelo de embeddings.

Este vector representa el significado semántico del contenido.

---

## 6.6 Almacenamiento

Los embeddings y sus metadatos se almacenan en la Base Vectorial.

A partir de este momento el conocimiento queda disponible para futuras consultas.

---

# 7. Flujo de consulta

Cuando un usuario realiza una pregunta, el sistema ejecuta las siguientes etapas.

## Paso 1

Validar autenticación.

---

## Paso 2

Verificar permisos.

---

## Paso 3

Interpretar la consulta.

---

## Paso 4

Generar el embedding de la consulta.

---

## Paso 5

Buscar los Chunks más similares en la Base Vectorial.

---

## Paso 6

Filtrar resultados utilizando:

- Organización.
- Workspace.
- Colección.
- Documento.
- Permisos del usuario.

---

## Paso 7

Construir el contexto.

---

## Paso 8

Construir el Prompt.

---

## Paso 9

Enviar el Prompt al Modelo de Lenguaje.

---

## Paso 10

Generar la respuesta.

---

## Paso 11

Registrar auditoría.

---

## Paso 12

Presentar la respuesta junto con las fuentes utilizadas.

---

# 8. Chunking

El Chunking constituye una de las etapas más importantes de la arquitectura.

Su objetivo es dividir documentos extensos en unidades de conocimiento reutilizables.

Cada Chunk debe:

- Mantener coherencia semántica.
- Evitar fragmentar ideas relacionadas.
- Facilitar la recuperación contextual.
- Conservar referencias al documento original.

---

# 9. Embeddings

Los embeddings permiten medir similitud semántica entre documentos y consultas.

Características:

- Representan significado, no palabras exactas.
- Permiten búsquedas inteligentes.
- Son independientes del idioma cuando el modelo lo soporta.
- Mejoran la recuperación de contexto.

Los embeddings se regeneran automáticamente cuando cambia el contenido del documento.

---

# 10. Base Vectorial

La Base Vectorial almacena:

- Embeddings.
- Metadatos.
- Referencias documentales.

No almacena respuestas generadas.

Su única función es recuperar conocimiento relevante para cada consulta.

---

# 11. Recuperación de contexto

El Recuperador de Contexto selecciona los fragmentos más relevantes para responder una consulta.

Durante este proceso se consideran:

- Similitud semántica.
- Permisos del usuario.
- Organización.
- Workspace.
- Colección.
- Estado del documento.
- Calidad del contenido.

---

# 12. Construcción del Prompt

El Prompt enviado al Modelo de Lenguaje está compuesto por:

- Instrucciones del Agente IA.
- Consulta del usuario.
- Contexto recuperado.
- Restricciones de seguridad.
- Configuración del modelo.

El contenido del Prompt puede variar según el tipo de Agente IA.

---

# 13. Generación de respuestas

El Modelo de Lenguaje genera una respuesta utilizando exclusivamente:

- El Prompt recibido.
- El contexto recuperado.
- Las instrucciones del Agente IA.

El modelo no debe utilizar información ajena al contexto cuando la organización opere en modo RAG estricto.

---

# 14. Trazabilidad

Toda respuesta podrá mantener referencia a:

- Documento.
- Chunk.
- Página.
- Sección.
- Colección.
- Workspace.

Esto permite verificar el origen de la información.

---

# 15. Seguridad

La arquitectura incorpora controles de seguridad en todas las etapas.

Entre ellos:

- Validación de identidad.
- Control de permisos.
- Aislamiento por organización.
- Filtrado previo a la recuperación.
- Auditoría de consultas.
- Protección de credenciales.
- Cifrado de comunicaciones.

Un usuario nunca podrá recuperar contexto de documentos para los cuales no tenga autorización.

---

# 16. Estrategias para reducir alucinaciones

Nexa Knowledge AI implementa diversas estrategias para minimizar respuestas incorrectas.

Entre ellas:

- Recuperación de contexto antes de generar respuestas.
- Uso exclusivo de documentos autorizados.
- Trazabilidad documental.
- Instrucciones estrictas para el Agente IA.
- Validación de permisos.
- Actualización automática de embeddings.
- Priorización de contenido reciente cuando corresponda.

Si no existe suficiente información, el Agente IA deberá indicar que no dispone de evidencia suficiente para responder.

---

# 17. Beneficios de la arquitectura

La arquitectura RAG proporciona:

- Respuestas fundamentadas.
- Mayor precisión.
- Menor tasa de alucinaciones.
- Escalabilidad.
- Actualización continua del conocimiento.
- Independencia respecto al modelo de lenguaje.
- Trazabilidad completa.
- Seguridad basada en permisos.

---

# 18. Relación con otros documentos

Este documento complementa:

- Arquitectura Funcional.
- Base de Conocimiento del Producto.
- Gestión de Documentos.
- Funcionamiento del Agente IA.
- Modelo de Permisos.
- Reglas de Negocio.
- Arquitectura Técnica.
- Arquitectura de Microservicios.

La arquitectura RAG constituye el núcleo tecnológico de Nexa Knowledge AI y define el mecanismo oficial mediante el cual los documentos corporativos se transforman en conocimiento consultable mediante Inteligencia Artificial.