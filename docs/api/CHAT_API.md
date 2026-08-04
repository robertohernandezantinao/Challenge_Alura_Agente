# Chat API

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Interno

---

# 1. Introducción

## Objetivo

El presente documento define la especificación oficial de la **Chat API** de Nexa Knowledge AI.

Su propósito es describir los servicios REST que permiten a aplicaciones externas interactuar con el Agente IA mediante conversaciones en lenguaje natural, utilizando la arquitectura RAG y respetando las políticas de autenticación, autorización y seguridad de la plataforma.

---

# 2. Alcance

La Chat API está disponible para:

- Aplicaciones Web.
- Aplicaciones móviles.
- Sistemas corporativos.
- Integraciones SaaS.
- Automatizaciones.
- Bots empresariales.
- Clientes autorizados.

Todo acceso requiere autenticación válida y permisos suficientes.

---

# 3. Características

La API permite:

- Crear conversaciones.
- Enviar consultas.
- Obtener respuestas del Agente IA.
- Recuperar historial.
- Gestionar conversaciones.
- Obtener metadatos de las respuestas.
- Utilizar respuestas en tiempo real (Streaming).
- Integrar el Agente IA en aplicaciones externas.

---

# 4. Arquitectura

La Chat API interactúa con los siguientes componentes:

- Gateway API
- Servicio de Autenticación
- Gestión de Usuarios
- Gestión de Roles
- Arquitectura RAG
- Base Vectorial
- Modelos LLM
- Guardrails
- Auditoría
- Monitorización

Cada consulta atraviesa todas las capas de seguridad antes de ser procesada.

---

# 5. Flujo General

El flujo de una consulta es:

1. Cliente envía la pregunta.
2. Validación del Access Token.
3. Verificación de permisos.
4. Recuperación documental (RAG).
5. Construcción del contexto.
6. Generación mediante el LLM.
7. Validación por Guardrails.
8. Envío de la respuesta.

---

# 6. Endpoint para Enviar Consultas

## POST /api/v1/chat/messages

Permite enviar una consulta al Agente IA.

### Headers

Authorization

Bearer {AccessToken}

Content-Type

application/json

---

### Ejemplo de solicitud

```json
{
  "conversationId": "conv_12345",
  "message": "¿Cuál es la política de vacaciones?",
  "workspaceId": "workspace_01"
}
```

---

### Ejemplo de respuesta

```json
{
  "messageId": "msg_98452",
  "conversationId": "conv_12345",
  "answer": "La política de vacaciones establece...",
  "sources": [
    {
      "document": "POLITICAS_INTERNAS.pdf",
      "page": 18
    }
  ],
  "createdAt": "2026-08-04T12:15:23Z"
}
```

---

# 7. Crear Conversación

## POST /api/v1/chat/conversations

Permite crear una nueva conversación.

### Respuesta

```json
{
  "conversationId": "conv_12345",
  "createdAt": "2026-08-04T12:00:00Z"
}
```

---

# 8. Obtener Conversaciones

## GET /api/v1/chat/conversations

Obtiene el listado de conversaciones del usuario autenticado.

Puede utilizar paginación.

---

# 9. Obtener una Conversación

## GET /api/v1/chat/conversations/{conversationId}

Devuelve:

- Información general.
- Fecha de creación.
- Última actualización.
- Cantidad de mensajes.
- Estado.

---

# 10. Historial de Mensajes

## GET /api/v1/chat/conversations/{conversationId}/messages

Obtiene todos los mensajes asociados a una conversación.

Cada mensaje puede incluir:

- Usuario.
- Consulta.
- Respuesta.
- Fecha.
- Documentos utilizados.
- Tiempo de respuesta.

---

# 11. Eliminar Conversación

## DELETE /api/v1/chat/conversations/{conversationId}

Permite eliminar una conversación.

La eliminación deberá respetar las políticas de retención de datos definidas por la organización.

---

# 12. Streaming

La Chat API puede transmitir respuestas de forma progresiva.

Beneficios:

- Menor tiempo de espera percibido.
- Mejor experiencia de usuario.
- Procesamiento continuo.
- Compatible con respuestas extensas.

El protocolo utilizado dependerá de la implementación (por ejemplo, Server-Sent Events o WebSockets).

---

# 13. Contexto Conversacional

La API puede mantener el contexto entre mensajes de una misma conversación.

El historial utilizado dependerá de:

- Configuración del Workspace.
- Límite de contexto del LLM.
- Políticas de la organización.

---

# 14. Fuentes Documentales

Las respuestas pueden incluir referencias a los documentos utilizados.

Información disponible:

- Documento.
- Página.
- Fragmento.
- Nivel de relevancia.
- Identificador documental.

Esto mejora la trazabilidad y la confianza en las respuestas.

---

# 15. Manejo de Errores

La API devuelve códigos HTTP estándar.

Ejemplos:

| Código | Descripción |
|----------|-------------|
| 200 | Consulta procesada correctamente. |
| 400 | Solicitud inválida. |
| 401 | Token inválido o expirado. |
| 403 | Acceso denegado. |
| 404 | Conversación inexistente. |
| 429 | Límite de consultas excedido. |
| 500 | Error interno del servidor. |

---

# 16. Rate Limits

La cantidad de consultas permitidas puede depender de:

- Plan contratado.
- Organización.
- Usuario.
- Tipo de integración.
- Capacidad disponible.

Los límites son administrados por el Gateway API.

---

# 17. Seguridad

Todas las solicitudes deben cumplir:

- HTTPS obligatorio.
- Token válido.
- Permisos suficientes.
- Workspace autorizado.
- Validación mediante Guardrails.
- Registro para auditoría.

Las respuestas nunca podrán contener información fuera del contexto autorizado.

---

# 18. Buenas Prácticas

Se recomienda:

- Reutilizar conversaciones cuando exista continuidad temática.
- Gestionar correctamente los errores HTTP.
- Respetar los límites de consumo.
- Implementar reintentos únicamente para errores transitorios.
- Mantener actualizado el Access Token.
- Utilizar Streaming para respuestas extensas.

---

# 19. Glosario

| Término | Descripción |
|----------|-------------|
| Conversación | Conjunto de mensajes relacionados entre sí. |
| Message | Consulta individual enviada al Agente IA. |
| Streaming | Recepción progresiva de la respuesta generada por el modelo. |
| Contexto | Información utilizada por el LLM para responder. |
| Fuente | Documento utilizado para construir la respuesta. |
| Conversation ID | Identificador único de una conversación. |

---

# 20. Documentos Relacionados

Este documento complementa:

- Introducción API.
- Autenticación.
- Gestión de Tokens.
- Usuarios API.
- Documentos API.
- Webhooks.
- Códigos de Error.
- Rate Limits.
- Arquitectura RAG.
- Funcionamiento del Agente IA.
- Gestión del Contexto.
- Guardrails.

La presente documentación constituye la especificación oficial de la Chat API de Nexa Knowledge AI y define los servicios, flujos, mecanismos de autenticación y buenas prácticas necesarios para integrar de forma segura y eficiente las capacidades conversacionales del Agente IA en aplicaciones empresariales y sistemas externos.