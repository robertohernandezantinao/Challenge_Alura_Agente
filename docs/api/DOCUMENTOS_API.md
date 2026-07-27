# Documentos API

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

---

# 1. Introducción

## Objetivo

Este documento define el recurso **Documents** de la API de Nexa Knowledge AI.

Describe todos los endpoints relacionados con la gestión documental, incluyendo carga de archivos, actualización, procesamiento, indexación, consulta, versionado, eliminación y administración de metadatos.

Este recurso constituye el punto de entrada oficial para alimentar la Base de Conocimiento utilizada por la arquitectura RAG.

---

# 2. Recurso

```
/documents
```

Representa los documentos almacenados dentro de una colección perteneciente a un Workspace.

Cada documento contiene:

- Archivo original.
- Contenido extraído.
- Metadatos.
- Versiones.
- Estado de procesamiento.
- Información de auditoría.
- Referencias para indexación.

---

# 3. Modelo de datos

```json
{
  "id": "doc_01HY89XABC123",
  "name": "Manual de Onboarding.pdf",
  "description": "Manual para nuevos colaboradores",
  "workspaceId": "ws_001",
  "collectionId": "col_010",
  "status": "AVAILABLE",
  "version": 3,
  "language": "es",
  "size": 2456780,
  "mimeType": "application/pdf",
  "createdBy": "usr_001",
  "createdAt": "2026-07-20T09:15:00Z",
  "updatedAt": "2026-07-22T16:45:00Z"
}
```

---

# 4. Estados del documento

| Estado | Descripción |
|----------|-------------|
| UPLOADING | Archivo en transferencia. |
| VALIDATING | Validación inicial. |
| PROCESSING | Extracción de contenido. |
| INDEXING | Generación de embeddings. |
| AVAILABLE | Disponible para consultas. |
| FAILED | Error durante el procesamiento. |
| ARCHIVED | Archivado. |
| DELETED | Eliminado lógicamente. |

---

# 5. Endpoints

## Obtener documentos

```
GET /documents
```

Obtiene los documentos visibles para el usuario autenticado.

---

### Parámetros

| Parámetro | Tipo | Descripción |
|------------|------|-------------|
| page | Integer | Página. |
| pageSize | Integer | Tamaño de página. |
| workspaceId | String | Workspace. |
| collectionId | String | Colección. |
| status | String | Estado. |
| q | String | Texto de búsqueda. |
| sort | String | Ordenamiento. |

---

### Respuesta

```json
{
  "success": true,
  "data": [
    {
      "id": "doc_001",
      "name": "Manual.pdf",
      "status": "AVAILABLE",
      "version": 2
    }
  ]
}
```

---

## Obtener documento

```
GET /documents/{id}
```

Devuelve la información completa de un documento.

---

## Crear documento

```
POST /documents
```

Permite cargar un nuevo documento.

La solicitud utiliza **multipart/form-data**.

---

### Parámetros

| Campo | Tipo |
|---------|------|
| file | Archivo |
| workspaceId | String |
| collectionId | String |
| name | String |
| description | String |

---

### Respuesta

```json
{
  "success": true,
  "data": {
    "id": "doc_010",
    "status": "PROCESSING"
  }
}
```

La indexación comenzará automáticamente.

---

## Actualizar documento

```
PUT /documents/{id}
```

Reemplaza completamente la información del documento.

---

## Actualización parcial

```
PATCH /documents/{id}
```

Permite modificar únicamente los metadatos enviados.

Ejemplo:

```json
{
  "description": "Nueva descripción"
}
```

---

## Eliminar documento

```
DELETE /documents/{id}
```

Realiza una eliminación lógica.

---

### Respuesta

```
204 No Content
```

---

# 6. Gestión de versiones

## Obtener versiones

```
GET /documents/{id}/versions
```

Devuelve todas las versiones disponibles.

---

## Crear nueva versión

```
POST /documents/{id}/versions
```

Carga una nueva versión del archivo.

Cada nueva versión inicia nuevamente el flujo de procesamiento e indexación.

---

## Restaurar versión

```
POST /documents/{id}/versions/{version}/restore
```

Restaura una versión anterior del documento.

---

# 7. Procesamiento

## Obtener estado

```
GET /documents/{id}/processing
```

Devuelve el estado actual del procesamiento.

---

Ejemplo:

```json
{
  "status": "INDEXING",
  "progress": 82
}
```

---

## Reprocesar documento

```
POST /documents/{id}/reprocess
```

Inicia nuevamente el procesamiento completo.

---

# 8. Indexación

## Obtener estado de indexación

```
GET /documents/{id}/index
```

Consulta el estado de la Base Vectorial para el documento.

---

## Reindexar

```
POST /documents/{id}/index
```

Genera nuevamente:

- Chunks.
- Embeddings.
- Índices vectoriales.

No modifica el archivo original.

---

# 9. Metadatos

## Obtener metadatos

```
GET /documents/{id}/metadata
```

---

## Actualizar metadatos

```
PATCH /documents/{id}/metadata
```

Ejemplo:

```json
{
  "author": "Carlos Ruiz",
  "department": "Ingeniería",
  "tags": [
    "backend",
    "arquitectura"
  ]
}
```

---

# 10. Etiquetas

## Obtener etiquetas

```
GET /documents/{id}/tags
```

---

## Agregar etiqueta

```
POST /documents/{id}/tags
```

---

## Eliminar etiqueta

```
DELETE /documents/{id}/tags/{tag}
```

---

# 11. Descarga

## Descargar documento

```
GET /documents/{id}/download
```

Devuelve el archivo original cuando el usuario posee permisos suficientes.

---

# 12. Vista previa

```
GET /documents/{id}/preview
```

Obtiene una vista previa del contenido cuando el formato del archivo lo permite.

---

# 13. Búsqueda

```
GET /documents/search
```

Permite localizar documentos mediante:

- Nombre.
- Texto.
- Etiquetas.
- Autor.
- Colección.
- Workspace.
- Metadatos.

---

Ejemplo

```
GET /documents/search?q=manual onboarding
```

---

# 14. Validaciones

Antes de aceptar un documento, la plataforma verifica:

- Formato permitido.
- Tamaño máximo.
- Integridad del archivo.
- Existencia del Workspace.
- Existencia de la colección.
- Permisos del usuario.
- Restricciones de seguridad.

---

# 15. Permisos requeridos

| Operación | Permiso |
|------------|----------|
| Consultar documentos | documents.read |
| Crear documentos | documents.create |
| Actualizar documentos | documents.update |
| Eliminar documentos | documents.delete |
| Descargar documentos | documents.download |
| Reindexar | documents.reindex |
| Gestionar versiones | documents.version |

---

# 16. Auditoría

Todas las operaciones relevantes generan registros de auditoría.

Entre ellas:

- Carga.
- Actualización.
- Eliminación.
- Descarga.
- Reprocesamiento.
- Reindexación.
- Restauración.
- Cambio de metadatos.
- Cambio de etiquetas.

Cada registro almacena:

- Usuario.
- Fecha.
- Dirección IP.
- Operación.
- Resultado.

---

# 17. Códigos de error

| Código | Descripción |
|----------|-------------|
| DOCUMENT_NOT_FOUND | Documento inexistente. |
| INVALID_FILE | Archivo inválido. |
| FILE_TOO_LARGE | Tamaño excedido. |
| UNSUPPORTED_FORMAT | Formato no permitido. |
| PROCESSING_ERROR | Error de procesamiento. |
| INDEXING_ERROR | Error durante la indexación. |
| VERSION_NOT_FOUND | Versión inexistente. |
| ACCESS_DENIED | Acceso denegado. |

---

# 18. Flujo completo

```
POST /documents

↓

Archivo recibido

↓

Validación

↓

Extracción

↓

Chunking

↓

Embeddings

↓

Base Vectorial

↓

Estado AVAILABLE

↓

Disponible para consultas RAG
```

---

# 19. Integración con la arquitectura RAG

Cada documento aprobado sigue el flujo oficial definido por la arquitectura RAG:

1. Recepción del archivo.
2. Extracción del contenido.
3. Normalización.
4. División en Chunks.
5. Generación de Embeddings.
6. Almacenamiento en la Base Vectorial.
7. Asociación de metadatos.
8. Disponibilidad para recuperación semántica.

Los Agentes IA únicamente utilizarán documentos que hayan alcanzado el estado **AVAILABLE**.

---

# 20. Buenas prácticas

Se recomienda:

- Mantener nombres descriptivos.
- Actualizar documentos en lugar de crear duplicados.
- Completar los metadatos.
- Utilizar etiquetas consistentes.
- Organizar los documentos por colección.
- Revisar periódicamente el estado de indexación.
- Reindexar únicamente cuando sea necesario.

---

# 21. Relación con otros documentos

Este documento complementa:

- Introducción API.
- Usuarios API.
- Gestión de Documentos.
- Arquitectura RAG.
- Funcionamiento del Agente IA.
- Arquitectura Técnica.
- Modelo de Permisos.
- Manual del Administrador.

El recurso **Documents** representa el núcleo funcional de Nexa Knowledge AI, ya que constituye el mecanismo oficial mediante el cual el conocimiento empresarial ingresa a la plataforma, es procesado por la arquitectura RAG y queda disponible para los Agentes IA de forma segura, trazable y escalable.