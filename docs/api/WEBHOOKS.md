# Webhooks

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Interno

---

# 1. Introducción

## Objetivo

El presente documento define la arquitectura oficial de **Webhooks** de Nexa Knowledge AI.

Su finalidad es establecer el mecanismo mediante el cual la plataforma notifica automáticamente eventos relevantes a sistemas externos, permitiendo integraciones en tiempo real de forma segura, confiable y escalable.

---

# 2. Alcance

Este documento aplica a:

- API REST.
- Integraciones empresariales.
- Aplicaciones SaaS.
- Sistemas ERP.
- Sistemas CRM.
- Plataformas BPM.
- Automatizaciones.
- Microservicios.

Todo Webhook deberá cumplir las políticas de autenticación y seguridad definidas por la plataforma.

---

# 3. Objetivos

La arquitectura de Webhooks busca:

- Notificar eventos en tiempo real.
- Reducir consultas innecesarias a la API.
- Facilitar integraciones empresariales.
- Garantizar la entrega de eventos.
- Mantener la trazabilidad de las notificaciones.
- Proporcionar un mecanismo escalable de integración.

---

# 4. Arquitectura General

El flujo general es:

1. Ocurre un evento en Nexa Knowledge AI.
2. El evento es validado.
3. Se construye el payload.
4. Se firma digitalmente la solicitud.
5. Se envía una petición HTTP POST al endpoint registrado.
6. Se espera la respuesta del sistema receptor.
7. Se registra el resultado.
8. Si es necesario, se ejecutan reintentos automáticos.

---

# 5. Registro de Webhooks

Cada organización puede registrar uno o varios Webhooks.

La configuración incluye:

- Nombre.
- URL destino.
- Eventos suscritos.
- Estado (Activo/Inactivo).
- Clave secreta para firma.
- Política de reintentos.

Solo usuarios con privilegios administrativos pueden gestionar Webhooks.

---

# 6. Eventos Disponibles

La plataforma puede generar eventos como:

### Usuarios

- user.created
- user.updated
- user.deleted
- user.locked

### Documentos

- document.created
- document.updated
- document.deleted
- document.indexed
- document.processing.completed
- document.processing.failed

### Workspaces

- workspace.created
- workspace.updated
- workspace.deleted

### Conversaciones

- conversation.created
- conversation.deleted

### Chat IA

- chat.request.received
- chat.response.generated
- chat.response.failed

### Administración

- organization.updated
- role.updated
- permissions.updated

La lista de eventos puede ampliarse en futuras versiones.

---

# 7. Formato del Payload

Las notificaciones utilizan JSON.

Ejemplo:

```json
{
  "event": "document.indexed",
  "eventId": "evt_456321",
  "timestamp": "2026-08-04T15:42:18Z",
  "organizationId": "org_001",
  "workspaceId": "workspace_12",
  "data": {
    "documentId": "doc_8452",
    "name": "MANUAL_RRHH.pdf",
    "status": "Indexed"
  }
}
```

---

# 8. Encabezados HTTP

Cada solicitud incluye encabezados estándar.

Ejemplo:

```
Content-Type: application/json
User-Agent: NexaKnowledgeAI-Webhooks
X-Nexa-Event: document.indexed
X-Nexa-Delivery: evt_456321
X-Nexa-Signature: SHA256=...
```

Estos encabezados facilitan la validación y trazabilidad de cada entrega.

---

# 9. Firma de Solicitudes

Todas las solicitudes pueden firmarse utilizando una clave secreta compartida.

La firma permite:

- Verificar autenticidad.
- Detectar modificaciones.
- Evitar suplantaciones.
- Validar integridad del payload.

La verificación debe realizarse antes de procesar el evento.

---

# 10. Confirmación de Recepción

El endpoint receptor debe responder con un código HTTP exitoso.

Ejemplo:

```
HTTP 200 OK
```

o

```
HTTP 204 No Content
```

Cualquier otro código puede activar el mecanismo de reintentos.

---

# 11. Reintentos Automáticos

Cuando una entrega falla, el sistema puede ejecutar reintentos automáticos.

Las políticas pueden configurarse considerando:

- Número máximo de intentos.
- Intervalo entre reintentos.
- Backoff exponencial.
- Tiempo máximo de espera.

Cada intento queda registrado para auditoría.

---

# 12. Manejo de Errores

Algunos escenarios contemplados son:

- Endpoint no disponible.
- Timeout.
- Error SSL/TLS.
- Error de autenticación.
- Respuesta HTTP 4xx.
- Respuesta HTTP 5xx.

Dependiendo del error, el sistema decidirá si reintenta o descarta la entrega.

---

# 13. Seguridad

Los Webhooks deben cumplir las siguientes políticas:

- HTTPS obligatorio.
- Certificados válidos.
- Firma digital obligatoria cuando esté habilitada.
- Validación del origen.
- Protección frente a ataques de repetición.
- Registro completo de eventos.

Nunca deben enviarse credenciales sensibles dentro del payload.

---

# 14. Monitorización

La plataforma registra información sobre:

- Entregas exitosas.
- Entregas fallidas.
- Latencia.
- Reintentos.
- Tiempo de respuesta.
- Estado de cada endpoint.

Estos indicadores permiten supervisar el funcionamiento de las integraciones.

---

# 15. Auditoría

Cada entrega genera un registro con información como:

- Identificador del evento.
- Fecha.
- Organización.
- Endpoint destino.
- Código HTTP recibido.
- Duración.
- Número de intento.
- Resultado final.

La auditoría facilita el análisis de incidentes y el cumplimiento normativo.

---

# 16. Buenas Prácticas

Se recomienda:

- Procesar rápidamente las solicitudes recibidas.
- Responder con códigos HTTP adecuados.
- Validar siempre la firma digital.
- Implementar idempotencia utilizando el identificador del evento.
- Registrar los eventos recibidos.
- Evitar operaciones largas durante la recepción del Webhook.

---

# 17. Limitaciones

Los Webhooks no garantizan procesamiento inmediato por parte del sistema receptor.

Las aplicaciones consumidoras deben:

- Gestionar duplicados.
- Implementar tolerancia a fallos.
- Registrar eventos.
- Reprocesar entregas cuando sea necesario.

---

# 18. Integración con Otros Componentes

Los Webhooks interactúan con:

- Gateway API.
- Autenticación.
- Gestión de Usuarios.
- Gestión de Documentos.
- Chat IA.
- Auditoría.
- Monitorización.
- Seguridad.
- Microservicios.

Constituyen uno de los principales mecanismos de integración con sistemas externos.

---

# 19. Glosario

| Término | Descripción |
|----------|-------------|
| Webhook | Notificación HTTP enviada automáticamente cuando ocurre un evento. |
| Evento | Acción que desencadena una notificación. |
| Payload | Información enviada al sistema receptor. |
| Endpoint | URL que recibe el Webhook. |
| Firma Digital | Mecanismo para verificar autenticidad e integridad de la solicitud. |
| Reintento | Nuevo intento de entrega tras un fallo. |

---

# 20. Documentos Relacionados

Este documento complementa:

- Introducción API.
- Autenticación.
- Gestión de Tokens.
- Chat API.
- Usuarios API.
- Documentos API.
- Códigos de Error.
- Rate Limits.
- Arquitectura de Microservicios.
- Política de Seguridad.
- Monitorización.

La presente documentación constituye la especificación oficial de la arquitectura de Webhooks de Nexa Knowledge AI y establece los mecanismos necesarios para implementar integraciones en tiempo real, garantizando la entrega confiable de eventos, la seguridad de las comunicaciones y la interoperabilidad con sistemas empresariales externos.