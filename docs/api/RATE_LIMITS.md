# Rate Limits

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Interno

---

# 1. Introducción

## Objetivo

El presente documento define la política oficial de **Rate Limiting** implementada por Nexa Knowledge AI.

Su finalidad es establecer los mecanismos utilizados para controlar el número de solicitudes que pueden realizar usuarios, organizaciones, aplicaciones e integraciones a la API, garantizando la estabilidad, disponibilidad y uso equitativo de los recursos de la plataforma.

---

# 2. Alcance

Este documento aplica a:

- API REST.
- Chat API.
- Webhooks.
- Integraciones externas.
- Aplicaciones Web.
- Aplicaciones móviles.
- Microservicios.
- Clientes empresariales.

Todas las solicitudes dirigidas a la API están sujetas a las políticas descritas en este documento.

---

# 3. Objetivos

La política de Rate Limiting busca:

- Proteger la infraestructura.
- Evitar abusos.
- Garantizar disponibilidad.
- Distribuir equitativamente los recursos.
- Reducir ataques automatizados.
- Mantener tiempos de respuesta estables.

---

# 4. Conceptos

El **Rate Limit** representa la cantidad máxima de solicitudes permitidas durante un período determinado.

Los límites pueden aplicarse considerando:

- Usuario.
- Organización.
- Workspace.
- API Token.
- Dirección IP.
- Plan contratado.
- Endpoint específico.

---

# 5. Algoritmos de Control

La plataforma puede utilizar distintos algoritmos según el tipo de servicio.

## Token Bucket

Permite absorber ráfagas cortas de tráfico mientras mantiene un límite promedio de solicitudes.

Características:

- Alto rendimiento.
- Adecuado para APIs públicas.
- Recuperación progresiva de capacidad.

---

## Sliding Window

Controla el número de solicitudes realizadas dentro de una ventana temporal móvil.

Beneficios:

- Mayor precisión.
- Distribución uniforme del tráfico.
- Reducción de picos de consumo.

---

## Fixed Window

Utilizado en determinados escenarios administrativos donde la simplicidad es prioritaria.

---

# 6. Niveles de Aplicación

Los límites pueden configurarse a diferentes niveles.

## Usuario

Cantidad máxima de solicitudes permitidas por usuario autenticado.

---

## Organización

Límite agregado para todos los usuarios pertenecientes a una organización.

---

## API Token

Control independiente para integraciones específicas.

---

## Dirección IP

Protección frente a abuso antes de la autenticación.

---

## Endpoint

Determinados servicios pueden disponer de límites específicos.

---

# 7. Políticas por Plan

Los límites dependen del plan contratado.

Ejemplo:

| Plan | Consultas por minuto | Consultas por día |
|------|---------------------:|------------------:|
| Free | Configurable | Configurable |
| Professional | Configurable | Configurable |
| Business | Configurable | Configurable |
| Enterprise | Definido mediante contrato |

Los valores concretos serán administrados mediante la configuración de la plataforma.

---

# 8. Cabeceras HTTP

Cuando una solicitud es aceptada, la API puede devolver información relacionada con los límites aplicados.

Ejemplo:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 76
X-RateLimit-Reset: 1722783600
```

Estas cabeceras permiten al cliente conocer el consumo de su cuota.

---

# 9. Exceso del Límite

Cuando un cliente supera el límite permitido, la plataforma responde con:

```
HTTP 429
Too Many Requests
```

Ejemplo:

```json
{
  "success": false,
  "error": {
    "code": "RATE_001",
    "message": "Rate limit excedido.",
    "details": "Intente nuevamente cuando finalice el período de espera."
  }
}
```

---

# 10. Retry-After

Cuando corresponda, la respuesta incluirá la cabecera:

```
Retry-After
```

Indicando el tiempo aproximado que el cliente deberá esperar antes de realizar una nueva solicitud.

---

# 11. Excepciones

Determinados procesos pueden disponer de políticas especiales.

Ejemplos:

- Procesamiento documental.
- Migraciones.
- Sincronizaciones masivas.
- Integraciones Enterprise.
- Procesos internos.

Las excepciones deben estar autorizadas y registradas.

---

# 12. Monitorización

La plataforma supervisa continuamente:

- Solicitudes por minuto.
- Solicitudes por organización.
- Solicitudes por endpoint.
- Errores 429.
- Consumo de cuotas.
- Tendencias de uso.

Estos indicadores permiten ajustar dinámicamente la configuración.

---

# 13. Auditoría

Todos los eventos relevantes relacionados con Rate Limiting pueden registrarse.

Información registrada:

- Usuario.
- Organización.
- Endpoint.
- Fecha y hora.
- Cantidad de solicitudes.
- Resultado.
- Dirección IP.

Estos registros facilitan investigaciones y análisis de capacidad.

---

# 14. Seguridad

El Rate Limiting constituye un mecanismo adicional de protección frente a:

- Ataques de fuerza bruta.
- Denegación de servicio.
- Automatizaciones maliciosas.
- Consumo excesivo de recursos.
- Integraciones defectuosas.

Debe combinarse con otras políticas de seguridad de la plataforma.

---

# 15. Buenas Prácticas para Clientes

Las aplicaciones consumidoras deben:

- Respetar las respuestas HTTP 429.
- Implementar reintentos con espera progresiva (Exponential Backoff).
- Evitar consultas repetitivas innecesarias.
- Utilizar caché cuando sea posible.
- Distribuir las solicitudes de forma uniforme.
- Supervisar las cabeceras de Rate Limit.

---

# 16. Buenas Prácticas para Administradores

Se recomienda:

- Ajustar límites según la capacidad disponible.
- Supervisar tendencias de uso.
- Revisar periódicamente los umbrales.
- Definir políticas diferenciadas por plan.
- Analizar eventos de abuso.
- Documentar cualquier excepción.

---

# 17. Limitaciones

El Rate Limiting:

- No sustituye mecanismos de autenticación.
- No reemplaza controles de autorización.
- No elimina completamente ataques distribuidos.
- Debe complementarse con monitoreo, firewalls y políticas de seguridad.

---

# 18. Integración con Otros Componentes

La política de Rate Limiting interactúa con:

- Gateway API.
- Autenticación.
- Gestión de Tokens.
- Chat API.
- Webhooks.
- Monitorización.
- Auditoría.
- Seguridad.
- Arquitectura de Microservicios.

Constituye uno de los principales mecanismos para proteger la disponibilidad de la plataforma.

---

# 19. Glosario

| Término | Descripción |
|----------|-------------|
| Rate Limit | Número máximo de solicitudes permitidas durante un período. |
| Token Bucket | Algoritmo de control de tráfico basado en disponibilidad de tokens. |
| Sliding Window | Algoritmo que evalúa solicitudes dentro de una ventana temporal móvil. |
| Retry-After | Cabecera HTTP que indica cuándo puede repetirse una solicitud. |
| Quota | Cantidad máxima de operaciones permitidas. |
| HTTP 429 | Código de respuesta utilizado cuando se supera el límite permitido. |

---

# 20. Documentos Relacionados

Este documento complementa:

- Introducción API.
- Autenticación.
- Gestión de Tokens.
- Chat API.
- Webhooks.
- Códigos de Error.
- Política de Seguridad.
- Arquitectura Técnica.
- Monitorización.
- Infraestructura.

La presente documentación constituye la especificación oficial de la política de Rate Limiting de Nexa Knowledge AI y establece los mecanismos necesarios para controlar el consumo de la API, proteger la infraestructura y garantizar un servicio estable, seguro y escalable para todos los usuarios e integraciones de la plataforma.