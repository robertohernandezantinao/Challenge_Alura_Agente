# Introducción a la API

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

---

# 1. Introducción

## Objetivo

Este documento presenta la API oficial de Nexa Knowledge AI.

Su propósito es proporcionar una visión general de la arquitectura, principios, convenciones y mecanismos de autenticación utilizados por la API, sirviendo como punto de partida para desarrolladores e integradores.

Los detalles específicos de cada recurso se documentan en los documentos individuales de la carpeta `docs/api/`.

---

# 2. ¿Qué es la API de Nexa Knowledge AI?

La API permite integrar Nexa Knowledge AI con aplicaciones externas, sistemas empresariales y servicios de terceros.

Mediante la API es posible automatizar operaciones relacionadas con:

- Usuarios.
- Organizaciones.
- Workspaces.
- Colecciones.
- Documentos.
- Agentes IA.
- Conversaciones.
- Auditoría.
- Configuración.

La API sigue un diseño consistente, orientado a recursos y preparado para evolucionar sin romper integraciones existentes.

---

# 3. Principios de diseño

La API ha sido diseñada siguiendo los siguientes principios.

## Consistencia

Todos los recursos utilizan convenciones comunes de nombres, respuestas y códigos HTTP.

---

## Seguridad

Cada solicitud requiere autenticación y autorización antes de acceder a cualquier recurso protegido.

---

## Escalabilidad

La API está preparada para soportar múltiples organizaciones y grandes volúmenes de solicitudes.

---

## Versionado

Las nuevas funcionalidades deberán incorporarse sin afectar la compatibilidad con integraciones existentes.

---

## Trazabilidad

Las operaciones relevantes podrán registrarse para fines de auditoría y monitoreo.

---

# 4. Arquitectura

La API forma parte de la arquitectura de microservicios de Nexa Knowledge AI.

```
Cliente

↓

API Gateway

↓

Servicio correspondiente

↓

Base de Datos

↓

Base Vectorial

↓

Servicios IA

↓

Respuesta
```

El API Gateway centraliza la autenticación, autorización, validaciones iniciales y el enrutamiento de las solicitudes.

---

# 5. Base URL

La URL dependerá del entorno.

Ejemplos:

Producción

```
https://api.nexaknowledge.ai/v1
```

Staging

```
https://staging-api.nexaknowledge.ai/v1
```

Desarrollo

```
http://localhost:8080/api/v1
```

Los valores exactos serán definidos durante el despliegue de cada entorno.

---

# 6. Versionado

La API utiliza versionado mediante la URL.

Ejemplo:

```
/api/v1
```

Las nuevas versiones mayores introducirán cambios incompatibles.

Las versiones menores mantendrán compatibilidad hacia atrás siempre que sea posible.

---

# 7. Formato de intercambio

Todas las solicitudes y respuestas utilizan JSON.

Ejemplo:

```json
{
  "id": "usr_123",
  "name": "Juan Pérez",
  "email": "juan@empresa.com"
}
```

Las fechas deberán utilizar el estándar ISO 8601.

Ejemplo:

```
2026-08-15T14:30:00Z
```

---

# 8. Autenticación

La API utiliza autenticación basada en tokens.

El cliente deberá enviar el token en cada solicitud protegida.

Ejemplo:

```
Authorization: Bearer <token>
```

Las credenciales nunca deberán incluirse en parámetros de consulta.

---

# 9. Autorización

La autorización se realiza utilizando el modelo oficial de permisos de Nexa Knowledge AI.

Antes de ejecutar cualquier operación, el sistema verifica:

- Identidad del usuario.
- Organización activa.
- Rol asignado.
- Permisos específicos.
- Alcance del recurso solicitado.

Si el usuario no dispone de autorización suficiente, la operación será rechazada.

---

# 10. Convenciones REST

Los recursos utilizan las operaciones HTTP estándar.

| Método | Operación |
|---------|-----------|
| GET | Consultar recursos |
| POST | Crear recursos |
| PUT | Reemplazar recursos |
| PATCH | Actualizar parcialmente |
| DELETE | Eliminar recursos |

---

# 11. Convenciones de nombres

Los endpoints utilizan:

- Sustantivos.
- Plural.
- Minúsculas.
- Guiones cuando sea necesario.

Ejemplos:

```
/users
```

```
/documents
```

```
/workspaces
```

```
/collections
```

---

# 12. Respuestas

Las respuestas seguirán una estructura uniforme.

Ejemplo exitoso:

```json
{
  "success": true,
  "data": {}
}
```

Ejemplo con error:

```json
{
  "success": false,
  "error": {
    "code": "DOCUMENT_NOT_FOUND",
    "message": "El documento no existe."
  }
}
```

---

# 13. Códigos HTTP

| Código | Significado |
|---------|-------------|
| 200 | Operación exitosa |
| 201 | Recurso creado |
| 204 | Sin contenido |
| 400 | Solicitud inválida |
| 401 | No autenticado |
| 403 | Acceso denegado |
| 404 | Recurso inexistente |
| 409 | Conflicto |
| 422 | Error de validación |
| 429 | Límite excedido |
| 500 | Error interno |

---

# 14. Paginación

Los recursos que devuelven listas utilizarán paginación.

Parámetros habituales:

```
?page=1
```

```
?pageSize=25
```

Las respuestas incluirán información sobre:

- Página actual.
- Tamaño de página.
- Total de registros.
- Total de páginas.

---

# 15. Ordenamiento

Los recursos podrán ordenarse mediante parámetros de consulta.

Ejemplo:

```
?sort=name
```

```
?sort=-createdAt
```

El prefijo `-` indica orden descendente.

---

# 16. Filtrado

La API admite filtros sobre los recursos.

Ejemplos:

```
?status=ACTIVE
```

```
?workspace=ws_001
```

```
?role=ADMIN
```

Los filtros disponibles dependerán de cada endpoint.

---

# 17. Búsqueda

Algunos recursos permiten búsquedas por texto.

Ejemplo:

```
?q=manual onboarding
```

La búsqueda podrá combinarse con filtros y paginación.

---

# 18. Idempotencia

Las operaciones de creación críticas podrán soportar claves de idempotencia para evitar duplicados cuando un cliente reintente una solicitud.

Ejemplo:

```
Idempotency-Key: 5d81d5f4-a1e3-41e0-bfd0-xxxxxxxx
```

---

# 19. Rate Limiting

Para proteger la plataforma se podrán aplicar límites de solicitudes.

Cuando un cliente supere el límite configurado recibirá una respuesta:

```
429 Too Many Requests
```

El tiempo de espera podrá indicarse mediante encabezados HTTP.

---

# 20. Auditoría

Las operaciones relevantes podrán registrarse automáticamente.

Entre ellas:

- Inicio de sesión.
- Creación de usuarios.
- Carga de documentos.
- Eliminación de recursos.
- Cambios de permisos.
- Configuración.
- Consultas realizadas por Agentes IA.

La auditoría forma parte del modelo de seguridad de la plataforma.

---

# 21. Seguridad

Toda integración deberá cumplir las políticas de seguridad definidas por NexaDigital S.A.S.

Se recomienda:

- Utilizar HTTPS.
- Proteger los tokens.
- Rotar credenciales periódicamente.
- Validar certificados.
- Implementar tiempos de expiración adecuados.
- Aplicar el principio de mínimo privilegio.

---

# 22. Evolución de la API

La API evolucionará siguiendo los siguientes principios:

- Compatibilidad hacia atrás siempre que sea posible.
- Versionado explícito.
- Deprecación gradual.
- Documentación previa a la liberación.
- Comunicación anticipada de cambios importantes.

---

# 23. Documentos relacionados

Este documento introduce la API oficial y se complementa con:

- Usuarios API.
- Documentos API.
- Workspaces API.
- Colecciones API.
- Agentes IA API.
- Conversaciones API.
- Arquitectura Técnica.
- Arquitectura de Microservicios.
- Manual del Administrador.
- Modelo de Permisos.

Cada documento describe en detalle un conjunto específico de recursos y operaciones disponibles para la integración con Nexa Knowledge AI.