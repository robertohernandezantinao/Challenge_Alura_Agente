# Códigos de Error

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Interno

---

# 1. Introducción

## Objetivo

El presente documento define la especificación oficial de los **Códigos de Error** utilizados por la API y los servicios internos de Nexa Knowledge AI.

Su propósito es proporcionar un estándar uniforme para identificar, comunicar y resolver errores producidos durante la interacción con la plataforma, facilitando el desarrollo de integraciones, la depuración y la operación del sistema.

---

# 2. Alcance

Este documento aplica a:

- API REST.
- Chat API.
- Webhooks.
- Gestión de Usuarios.
- Gestión de Documentos.
- Arquitectura RAG.
- Microservicios.
- Panel Web.
- Integraciones externas.

Todos los servicios deberán utilizar el formato de error definido en este documento.

---

# 3. Objetivos

La gestión de errores busca:

- Proporcionar mensajes consistentes.
- Facilitar el diagnóstico de incidencias.
- Estandarizar las respuestas de la API.
- Mejorar la experiencia de los desarrolladores.
- Reducir tiempos de resolución.
- Mantener la trazabilidad de los incidentes.

---

# 4. Formato General de Error

Las respuestas de error utilizan formato JSON.

Ejemplo:

```json
{
  "success": false,
  "error": {
    "code": "AUTH_001",
    "message": "Access Token inválido.",
    "details": "El token proporcionado no pudo ser validado.",
    "requestId": "req_845962",
    "timestamp": "2026-08-04T16:42:11Z"
  }
}
```

---

# 5. Estructura de la Respuesta

Cada respuesta de error incluye:

- Código interno.
- Mensaje descriptivo.
- Detalles adicionales (cuando corresponda).
- Identificador de la solicitud.
- Fecha y hora.
- Código HTTP asociado.

Esta estructura facilita la correlación con los registros de auditoría.

---

# 6. Códigos HTTP

La plataforma utiliza los siguientes códigos HTTP estándar:

| Código | Descripción |
|---------|-------------|
| 200 | Solicitud procesada correctamente. |
| 201 | Recurso creado correctamente. |
| 204 | Operación completada sin contenido de respuesta. |
| 400 | Solicitud inválida. |
| 401 | No autenticado. |
| 403 | Acceso denegado. |
| 404 | Recurso no encontrado. |
| 409 | Conflicto con el estado actual del recurso. |
| 413 | Solicitud demasiado grande. |
| 415 | Tipo de contenido no soportado. |
| 422 | Error de validación. |
| 429 | Demasiadas solicitudes. |
| 500 | Error interno del servidor. |
| 502 | Error de comunicación entre servicios. |
| 503 | Servicio temporalmente no disponible. |

---

# 7. Errores de Autenticación

| Código | Descripción |
|---------|-------------|
| AUTH_001 | Access Token inválido. |
| AUTH_002 | Token expirado. |
| AUTH_003 | Refresh Token inválido. |
| AUTH_004 | Firma del token inválida. |
| AUTH_005 | Usuario no autenticado. |
| AUTH_006 | Sesión revocada. |

---

# 8. Errores de Autorización

| Código | Descripción |
|---------|-------------|
| PERM_001 | Permisos insuficientes. |
| PERM_002 | Rol no autorizado. |
| PERM_003 | Workspace no autorizado. |
| PERM_004 | Organización no válida. |
| PERM_005 | Recurso restringido. |

---

# 9. Errores de Validación

| Código | Descripción |
|---------|-------------|
| VAL_001 | Campo obligatorio ausente. |
| VAL_002 | Formato inválido. |
| VAL_003 | Valor fuera de rango. |
| VAL_004 | Identificador inválido. |
| VAL_005 | Archivo no válido. |

---

# 10. Errores de Gestión Documental

| Código | Descripción |
|---------|-------------|
| DOC_001 | Documento inexistente. |
| DOC_002 | Documento en procesamiento. |
| DOC_003 | Error de indexación. |
| DOC_004 | Formato documental no soportado. |
| DOC_005 | Error durante la extracción de contenido. |

---

# 11. Errores del Chat IA

| Código | Descripción |
|---------|-------------|
| CHAT_001 | Conversación inexistente. |
| CHAT_002 | Mensaje inválido. |
| CHAT_003 | Contexto insuficiente. |
| CHAT_004 | Error al generar la respuesta. |
| CHAT_005 | Conversación finalizada. |

---

# 12. Errores de la Arquitectura RAG

| Código | Descripción |
|---------|-------------|
| RAG_001 | Error durante la recuperación documental. |
| RAG_002 | No se encontró contexto suficiente. |
| RAG_003 | Error en Re-ranking. |
| RAG_004 | Error en Embeddings. |
| RAG_005 | Error de Base Vectorial. |

---

# 13. Errores de Integración

| Código | Descripción |
|---------|-------------|
| API_001 | Endpoint inexistente. |
| API_002 | Método HTTP no permitido. |
| API_003 | Versión de API no soportada. |
| API_004 | Content-Type inválido. |
| API_005 | Solicitud mal formada. |

---

# 14. Errores de Webhooks

| Código | Descripción |
|---------|-------------|
| WEBHOOK_001 | Endpoint no disponible. |
| WEBHOOK_002 | Firma inválida. |
| WEBHOOK_003 | Timeout durante la entrega. |
| WEBHOOK_004 | Error permanente del receptor. |
| WEBHOOK_005 | Reintentos agotados. |

---

# 15. Errores de Infraestructura

| Código | Descripción |
|---------|-------------|
| SYS_001 | Error interno del servidor. |
| SYS_002 | Servicio temporalmente indisponible. |
| SYS_003 | Error de base de datos. |
| SYS_004 | Error de comunicación entre microservicios. |
| SYS_005 | Tiempo de espera agotado. |

---

# 16. Manejo de Errores

Las aplicaciones consumidoras deben:

- Interpretar el código HTTP.
- Analizar el código interno.
- Mostrar mensajes adecuados al usuario.
- Registrar el Request ID.
- Implementar reintentos únicamente cuando sea apropiado.

---

# 17. Auditoría

Todos los errores relevantes generan registros con:

- Código de error.
- Servicio involucrado.
- Usuario autenticado (si aplica).
- Organización.
- Workspace.
- Fecha y hora.
- Request ID.
- Información diagnóstica.

Estos registros permiten realizar investigaciones posteriores.

---

# 18. Buenas Prácticas

Se recomienda:

- No exponer información sensible en los mensajes de error.
- Utilizar códigos internos estables.
- Mantener mensajes claros y consistentes.
- Registrar todos los errores críticos.
- Correlacionar errores mediante el Request ID.
- Documentar cualquier nuevo código antes de utilizarlo.

---

# 19. Glosario

| Término | Descripción |
|----------|-------------|
| Código HTTP | Código estándar utilizado en la respuesta HTTP. |
| Código Interno | Identificador propio de Nexa Knowledge AI para clasificar errores. |
| Request ID | Identificador único asociado a una solicitud. |
| Validación | Proceso de comprobación de datos antes de su procesamiento. |
| Timeout | Tiempo máximo permitido para completar una operación. |
| Auditoría | Registro de eventos utilizados para diagnóstico y trazabilidad. |

---

# 20. Documentos Relacionados

Este documento complementa:

- Introducción API.
- Autenticación.
- Gestión de Tokens.
- Chat API.
- Webhooks.
- Rate Limits.
- Política de Seguridad.
- Arquitectura Técnica.
- Monitorización.
- Gestión de Incidentes.

La presente documentación constituye la especificación oficial de los códigos de error de Nexa Knowledge AI y establece un modelo uniforme para la identificación, comunicación y gestión de errores en todos los componentes de la plataforma, garantizando consistencia, trazabilidad y facilidad de integración para desarrolladores y administradores.