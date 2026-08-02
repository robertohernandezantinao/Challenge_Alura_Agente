# Gestión de Roles

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Público

---

# 1. Introducción

## Objetivo

El presente documento describe el funcionamiento del módulo de Gestión de Roles de Nexa Knowledge AI.

Su propósito es establecer las directrices para la creación, administración y asignación de roles dentro de la plataforma, permitiendo controlar de forma segura el acceso a funcionalidades y recursos conforme a las responsabilidades de cada usuario.

---

# 2. Alcance

Este documento aplica a todos los administradores y usuarios con permisos para gestionar roles dentro de una organización.

Las funcionalidades disponibles dependerán del nivel de privilegios asignado.

---

# 3. Conceptos Fundamentales

## Rol

Un rol es un conjunto de permisos que determina las acciones que un usuario puede realizar dentro de la plataforma.

En lugar de asignar permisos individuales a cada usuario, estos se agrupan en roles reutilizables.

---

## Permiso

Un permiso representa la autorización para ejecutar una acción específica sobre un recurso.

Ejemplos:

- Crear documentos.
- Eliminar documentos.
- Consultar conversaciones.
- Administrar usuarios.
- Configurar la organización.

---

## Recurso

Elemento de la plataforma sobre el cual pueden aplicarse permisos.

Ejemplos:

- Documentos.
- Usuarios.
- Workspaces.
- Conversaciones.
- Configuración.
- API.
- Organización.

---

# 4. Objetivos del Módulo

La Gestión de Roles permite:

- Crear roles personalizados.
- Modificar roles existentes.
- Asignar permisos.
- Revocar permisos.
- Asociar roles a usuarios.
- Mantener un control centralizado del acceso.
- Facilitar la administración de grandes organizaciones.

---

# 5. Acceso al Módulo

Los administradores podrán acceder mediante:

**Administración → Roles**

Si el usuario no posee privilegios suficientes, esta opción no estará disponible.

---

# 6. Listado de Roles

El módulo presenta todos los roles disponibles dentro de la organización.

Generalmente incluye:

- Nombre.
- Descripción.
- Estado.
- Número de usuarios asignados.
- Fecha de creación.
- Última modificación.

---

# 7. Roles Predeterminados

Una implementación estándar puede incluir roles como:

- Administrador.
- Supervisor.
- Usuario Estándar.
- Invitado.

La organización podrá crear roles adicionales según sus necesidades.

---

# 8. Crear un Rol

Para registrar un nuevo rol:

1. Acceder al módulo **Roles**.
2. Seleccionar **Nuevo Rol**.
3. Asignar un nombre.
4. Registrar una descripción.
5. Configurar los permisos.
6. Guardar los cambios.

El nuevo rol quedará disponible para ser asignado a los usuarios autorizados.

---

# 9. Configuración de Permisos

Cada rol puede contener permisos sobre diferentes recursos.

Ejemplos:

## Usuarios

- Ver usuarios.
- Crear usuarios.
- Editar usuarios.
- Desactivar usuarios.

## Documentos

- Consultar.
- Subir.
- Actualizar.
- Eliminar.

## Workspaces

- Crear.
- Modificar.
- Eliminar.
- Administrar miembros.

## Chat IA

- Realizar consultas.
- Consultar historial.
- Exportar conversaciones.

## Administración

- Configuración global.
- Auditorías.
- Parámetros del sistema.

La lista de permisos dependerá de la versión de la plataforma.

---

# 10. Editar un Rol

Los administradores podrán modificar:

- Nombre.
- Descripción.
- Permisos.
- Estado.

Los cambios afectarán a todos los usuarios que tengan asignado dicho rol.

---

# 11. Asignar Roles a Usuarios

Un rol puede asignarse durante:

- La creación del usuario.
- La edición del usuario.
- Procesos administrativos posteriores.

Una vez asignado, los permisos estarán disponibles inmediatamente o conforme a las políticas de la organización.

---

# 12. Usuarios con Múltiples Roles

La plataforma puede permitir que un usuario tenga más de un rol asignado.

Cuando esto ocurra, el sistema aplicará las reglas de autorización definidas por el modelo de permisos.

La política de resolución de permisos deberá ajustarse al documento **Modelo de Permisos**.

---

# 13. Desactivar un Rol

Cuando un rol deja de utilizarse podrá desactivarse.

La desactivación:

- Impide nuevas asignaciones.
- Conserva la información histórica.
- Mantiene la trazabilidad administrativa.

Los usuarios existentes podrán requerir una reasignación de roles antes de la desactivación definitiva.

---

# 14. Eliminación de Roles

Como buena práctica, los roles no deberían eliminarse cuando existan usuarios asociados.

Antes de eliminar un rol se recomienda:

- Verificar usuarios asignados.
- Reasignar permisos.
- Confirmar que no existan dependencias.
- Registrar la operación en la auditoría.

---

# 15. Buenas Prácticas

Se recomienda:

- Crear únicamente los roles necesarios.
- Evitar roles excesivamente amplios.
- Aplicar el principio de mínimo privilegio.
- Revisar periódicamente los permisos.
- Documentar los cambios realizados.
- Utilizar nombres descriptivos para los roles.

---

# 16. Auditoría

Todas las operaciones relacionadas con roles podrán registrarse en la auditoría del sistema.

Ejemplos:

- Creación de roles.
- Edición de permisos.
- Asignación a usuarios.
- Eliminación.
- Activación.
- Desactivación.

La auditoría permite garantizar la trazabilidad de las acciones administrativas.

---

# 17. Problemas Frecuentes

| Situación | Acción recomendada |
|-----------|--------------------|
| Un usuario no puede acceder a una función | Verificar el rol asignado y los permisos configurados. |
| Un cambio de permisos no tiene efecto | Confirmar que el rol fue actualizado correctamente y que el usuario ha renovado su sesión si es necesario. |
| No aparece un rol en la lista | Revisar los filtros aplicados y verificar que el rol no esté desactivado. |
| No es posible eliminar un rol | Comprobar si existen usuarios asociados o dependencias activas. |
| Un usuario tiene más permisos de los esperados | Revisar todos los roles asignados y la política de resolución de permisos. |

---

# 18. Seguridad

La gestión de roles constituye uno de los principales mecanismos de seguridad de la plataforma.

Toda organización deberá:

- Limitar el acceso administrativo.
- Revisar periódicamente los permisos.
- Registrar las modificaciones.
- Eliminar privilegios innecesarios.
- Auditar cambios críticos.

Una correcta administración de roles reduce significativamente el riesgo de accesos no autorizados.

---

# 19. Integración con el Modelo de Permisos

La Gestión de Roles implementa el modelo de autorización definido para Nexa Knowledge AI.

Los permisos efectivos de un usuario dependerán de:

- Los roles asignados.
- La organización.
- El Workspace activo.
- Las políticas de seguridad.
- Las restricciones configuradas por la empresa.

La definición técnica del modelo se encuentra documentada en **MODELO_DE_PERMISOS.md**.

---

# 20. Documentos Relacionados

Este documento complementa:

- Introducción.
- Primeros Pasos.
- Gestión de Usuarios.
- Gestión de Workspaces.
- Gestión de Documentos.
- Modelo de Permisos.
- Política de Seguridad.
- Manual del Administrador.
- Arquitectura Funcional.

La presente documentación constituye la guía oficial para la administración de roles en Nexa Knowledge AI y establece las prácticas recomendadas para implementar un modelo de autorización seguro, escalable y alineado con las necesidades operativas de las organizaciones que utilizan la plataforma.