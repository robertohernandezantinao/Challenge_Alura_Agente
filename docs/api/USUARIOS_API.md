# Usuarios API

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

---

# 1. Introducción

## Objetivo

Este documento define el recurso **Users** de la API de Nexa Knowledge AI.

Describe los endpoints disponibles para administrar usuarios dentro de una organización, incluyendo operaciones de consulta, creación, actualización, activación, desactivación y eliminación, así como las reglas de validación y seguridad asociadas.

---

# 2. Recurso

```
/users
```

Representa a los usuarios registrados en una organización.

Cada usuario posee:

- Identificador único.
- Información personal.
- Estado.
- Roles.
- Permisos.
- Organizaciones asociadas.
- Fecha de creación.
- Fecha de actualización.

---

# 3. Modelo de datos

```json
{
  "id": "usr_01HXYZ123ABC",
  "firstName": "Juan",
  "lastName": "Pérez",
  "email": "juan@empresa.com",
  "status": "ACTIVE",
  "roles": [
    "ADMIN"
  ],
  "organizationId": "org_001",
  "createdAt": "2026-07-20T10:30:00Z",
  "updatedAt": "2026-07-21T09:00:00Z"
}
```

---

# 4. Estados

| Estado | Descripción |
|----------|-------------|
| PENDING | Invitación enviada. |
| ACTIVE | Usuario activo. |
| INACTIVE | Usuario deshabilitado. |
| LOCKED | Cuenta bloqueada. |
| DELETED | Eliminado lógicamente. |

---

# 5. Endpoints

## Obtener usuarios

```
GET /users
```

Obtiene la lista de usuarios visibles para el usuario autenticado.

---

### Parámetros

| Parámetro | Tipo | Descripción |
|------------|------|-------------|
| page | Integer | Página. |
| pageSize | Integer | Tamaño de página. |
| sort | String | Ordenamiento. |
| q | String | Texto de búsqueda. |
| status | String | Estado. |
| role | String | Rol. |

---

### Respuesta

```json
{
  "success": true,
  "data": [
    {
      "id": "usr_001",
      "firstName": "Juan",
      "lastName": "Pérez",
      "email": "juan@empresa.com",
      "status": "ACTIVE"
    }
  ]
}
```

---

## Obtener usuario

```
GET /users/{id}
```

Obtiene la información completa de un usuario.

---

### Parámetros

| Nombre | Tipo |
|----------|------|
| id | UUID/String |

---

### Respuesta

```json
{
  "success": true,
  "data": {
    "id": "usr_001",
    "firstName": "Juan",
    "lastName": "Pérez",
    "email": "juan@empresa.com",
    "status": "ACTIVE",
    "roles": [
      "ADMIN"
    ]
  }
}
```

---

## Crear usuario

```
POST /users
```

Permite registrar un nuevo usuario.

---

### Solicitud

```json
{
  "firstName": "Ana",
  "lastName": "López",
  "email": "ana@empresa.com",
  "role": "EDITOR"
}
```

---

### Respuesta

```json
{
  "success": true,
  "data": {
    "id": "usr_245",
    "status": "PENDING"
  }
}
```

El sistema enviará automáticamente una invitación por correo electrónico.

---

## Actualizar usuario

```
PUT /users/{id}
```

Actualiza completamente la información del usuario.

---

### Solicitud

```json
{
  "firstName": "Ana María",
  "lastName": "López",
  "role": "ADMIN"
}
```

---

## Actualización parcial

```
PATCH /users/{id}
```

Permite modificar únicamente los campos enviados.

---

Ejemplo:

```json
{
  "status": "INACTIVE"
}
```

---

## Eliminar usuario

```
DELETE /users/{id}
```

Realiza la eliminación lógica del usuario.

---

### Respuesta

```
204 No Content
```

---

# 6. Gestión del estado

## Activar usuario

```
POST /users/{id}/activate
```

Activa una cuenta previamente deshabilitada.

---

## Desactivar usuario

```
POST /users/{id}/deactivate
```

Impide nuevos inicios de sesión.

---

## Bloquear usuario

```
POST /users/{id}/lock
```

Bloquea temporalmente la cuenta.

---

## Desbloquear usuario

```
POST /users/{id}/unlock
```

Restablece el acceso.

---

# 7. Gestión de roles

## Obtener roles

```
GET /users/{id}/roles
```

---

## Asignar rol

```
POST /users/{id}/roles
```

Solicitud:

```json
{
  "role": "EDITOR"
}
```

---

## Eliminar rol

```
DELETE /users/{id}/roles/{role}
```

---

# 8. Gestión de organizaciones

Cuando un usuario pertenece a múltiples organizaciones.

## Obtener organizaciones

```
GET /users/{id}/organizations
```

---

## Asociar organización

```
POST /users/{id}/organizations
```

---

## Eliminar asociación

```
DELETE /users/{id}/organizations/{organizationId}
```

---

# 9. Cambio de contraseña

```
POST /users/{id}/password
```

---

Solicitud

```json
{
  "currentPassword": "********",
  "newPassword": "********"
}
```

---

# 10. Restablecimiento de contraseña

```
POST /users/password/reset
```

Envía un correo para recuperación.

---

# 11. Perfil del usuario autenticado

```
GET /users/me
```

Obtiene la información del usuario autenticado.

---

## Actualizar perfil

```
PATCH /users/me
```

Permite modificar:

- Nombre.
- Apellidos.
- Idioma.
- Zona horaria.
- Preferencias.

---

# 12. Validaciones

La API validará:

- Correo electrónico válido.
- Correo único dentro de la organización.
- Longitud máxima de nombres.
- Roles válidos.
- Estado permitido.
- Organización existente.

---

# 13. Permisos requeridos

| Operación | Permiso |
|------------|----------|
| Consultar usuarios | users.read |
| Crear usuario | users.create |
| Editar usuario | users.update |
| Eliminar usuario | users.delete |
| Gestionar roles | users.roles |
| Gestionar organizaciones | organizations.manage |

---

# 14. Auditoría

Las siguientes operaciones generan registros de auditoría:

- Creación.
- Actualización.
- Eliminación.
- Cambio de rol.
- Cambio de permisos.
- Cambio de contraseña.
- Activación.
- Desactivación.
- Bloqueo.

Cada registro almacena:

- Usuario ejecutor.
- Fecha.
- Dirección IP.
- Operación.
- Resultado.

---

# 15. Códigos de error

| Código | Descripción |
|----------|-------------|
| USER_NOT_FOUND | Usuario inexistente. |
| EMAIL_ALREADY_EXISTS | Correo duplicado. |
| INVALID_ROLE | Rol inválido. |
| USER_LOCKED | Usuario bloqueado. |
| INVALID_STATUS | Estado inválido. |
| ORGANIZATION_NOT_FOUND | Organización inexistente. |
| ACCESS_DENIED | Acceso denegado. |

---

# 16. Ejemplo de flujo

## Crear usuario

```
POST /users
```

↓

```
201 Created
```

↓

Correo de invitación enviado.

↓

Usuario acepta invitación.

↓

Configura contraseña.

↓

Cuenta pasa a estado ACTIVE.

---

# 17. Buenas prácticas

- Aplicar el principio de mínimo privilegio.
- Evitar asignar roles administrativos innecesarios.
- Desactivar usuarios que ya no pertenezcan a la organización.
- Revisar periódicamente los permisos asignados.
- Utilizar autenticación multifactor cuando esté disponible.
- Registrar todas las operaciones administrativas.

---

# 18. Relación con otros documentos

Este documento complementa:

- Introducción API.
- Documentos API.
- Modelo de Permisos.
- Manual del Administrador.
- Gestión de Usuarios.
- Arquitectura Técnica.
- Política de Seguridad.

El recurso **Users** constituye la base para la autenticación, autorización y administración de identidades dentro de Nexa Knowledge AI y debe implementarse conforme a las reglas de seguridad definidas por la plataforma.