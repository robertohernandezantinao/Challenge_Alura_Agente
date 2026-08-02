# Gestión de Usuarios

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Público

---

# 1. Introducción

## Objetivo

El presente documento describe el funcionamiento del módulo de Gestión de Usuarios de Nexa Knowledge AI.

Su finalidad es proporcionar a administradores y usuarios autorizados una guía completa para administrar las cuentas de usuario de la plataforma, incluyendo su creación, edición, activación, desactivación y asignación de permisos.

---

# 2. Alcance

Este documento aplica a todos los usuarios con permisos para administrar cuentas dentro de una organización.

Las funcionalidades disponibles dependerán del rol asignado.

---

# 3. Objetivos del Módulo

La Gestión de Usuarios permite:

- Registrar nuevos usuarios.
- Modificar información existente.
- Asignar roles.
- Asociar usuarios a organizaciones.
- Gestionar acceso a Workspaces.
- Activar o desactivar cuentas.
- Consultar información de usuarios.
- Mantener la seguridad del acceso al sistema.

---

# 4. Acceso al Módulo

Los usuarios autorizados podrán acceder desde el menú principal mediante la opción:

**Administración → Usuarios**

Si el usuario no posee permisos suficientes, esta opción no estará disponible.

---

# 5. Listado de Usuarios

El módulo presenta un listado con los usuarios registrados dentro de la organización.

Generalmente la información incluye:

- Nombre completo.
- Correo electrónico.
- Estado de la cuenta.
- Rol asignado.
- Organización.
- Fecha de creación.
- Último acceso.

Dependiendo de la configuración del sistema podrán mostrarse columnas adicionales.

---

# 6. Búsqueda de Usuarios

La plataforma permite localizar usuarios mediante diferentes criterios.

Entre ellos:

- Nombre.
- Apellidos.
- Correo electrónico.
- Estado.
- Rol.
- Organización.

La búsqueda puede combinar varios filtros simultáneamente.

---

# 7. Filtros

El listado puede filtrarse utilizando diferentes criterios.

Ejemplos:

- Usuarios activos.
- Usuarios inactivos.
- Administradores.
- Usuarios estándar.
- Organización específica.
- Workspace específico.

Los filtros facilitan la administración cuando existen numerosos usuarios registrados.

---

# 8. Crear un Usuario

Para registrar un nuevo usuario:

1. Acceder al módulo **Usuarios**.
2. Seleccionar **Nuevo Usuario**.
3. Completar la información requerida.
4. Asignar la organización correspondiente.
5. Asignar el rol inicial.
6. Definir los Workspaces autorizados.
7. Confirmar la creación.

Una vez finalizado el proceso, el usuario quedará disponible para utilizar la plataforma conforme a los permisos asignados.

---

# 9. Información del Usuario

Cada usuario puede contener información como:

- Nombre.
- Apellidos.
- Correo electrónico.
- Identificador interno.
- Estado.
- Organización.
- Roles.
- Workspaces autorizados.
- Fecha de creación.
- Última actualización.

La información disponible dependerá de la configuración de la organización.

---

# 10. Editar un Usuario

Los administradores autorizados pueden modificar la información de una cuenta existente.

Entre los cambios permitidos se encuentran:

- Datos personales.
- Rol.
- Organización.
- Workspaces.
- Estado.
- Configuración general.

Toda modificación deberá respetar las políticas de seguridad de la organización.

---

# 11. Activar y Desactivar Usuarios

Las cuentas pueden encontrarse en distintos estados.

## Usuario Activo

Puede iniciar sesión y utilizar la plataforma.

## Usuario Inactivo

No podrá autenticarse hasta que sea reactivado.

La desactivación de una cuenta no elimina la información histórica asociada al usuario.

---

# 12. Eliminación de Usuarios

Como política general, Nexa Knowledge AI prioriza la desactivación de cuentas sobre su eliminación permanente.

Esto permite conservar:

- Historial de actividades.
- Auditorías.
- Conversaciones.
- Registros administrativos.

La eliminación definitiva solo podrá realizarse conforme a las políticas definidas por la organización.

---

# 13. Asignación de Organizaciones

Un usuario puede pertenecer a una o varias organizaciones, dependiendo de la configuración implementada.

Cada organización mantiene de forma independiente:

- Usuarios.
- Documentos.
- Configuraciones.
- Workspaces.
- Permisos.

El acceso del usuario estará limitado a las organizaciones autorizadas.

---

# 14. Asignación de Workspaces

Los administradores pueden definir los Workspaces a los que un usuario tendrá acceso.

Cada Workspace representa un entorno independiente de trabajo.

Los permisos asignados determinarán:

- Qué documentos puede consultar.
- Qué conversaciones puede visualizar.
- Qué recursos puede administrar.

---

# 15. Roles del Usuario

Cada usuario posee uno o varios roles.

El rol determina las acciones permitidas dentro de la plataforma.

Ejemplos:

- Administrador.
- Supervisor.
- Usuario estándar.
- Invitado.

La definición detallada de permisos se encuentra en el documento correspondiente al modelo de autorización.

---

# 16. Restablecimiento de Contraseña

Cuando sea necesario, un administrador podrá iniciar el proceso de restablecimiento de contraseña.

El procedimiento puede incluir:

- Envío de un enlace seguro.
- Validación de identidad.
- Definición de una nueva contraseña.
- Confirmación del cambio.

El procedimiento exacto dependerá del método de autenticación utilizado por la organización.

---

# 17. Historial del Usuario

La plataforma puede conservar información relacionada con la actividad de cada usuario.

Ejemplos:

- Fecha de creación.
- Último inicio de sesión.
- Cambios de estado.
- Cambios de rol.
- Modificaciones administrativas.

Esta información facilita los procesos de auditoría y administración.

---

# 18. Buenas Prácticas

Se recomienda:

- Crear únicamente las cuentas necesarias.
- Asignar el principio de mínimo privilegio.
- Revisar periódicamente los permisos.
- Desactivar usuarios que ya no requieran acceso.
- Mantener actualizada la información del usuario.
- Utilizar autenticación multifactor cuando esté disponible.

---

# 19. Problemas Frecuentes

| Situación | Acción recomendada |
|-----------|--------------------|
| El usuario no puede iniciar sesión | Verificar que la cuenta esté activa y que las credenciales sean correctas. |
| No aparecen Workspaces disponibles | Confirmar la asignación correspondiente. |
| No puede acceder a documentos | Revisar los permisos y el rol asignado. |
| No recibe el correo de activación | Verificar la dirección registrada y revisar la carpeta de correo no deseado. |
| El usuario no aparece en la lista | Revisar los filtros aplicados y la organización seleccionada. |

---

# 20. Seguridad

La administración de usuarios deberá cumplir las políticas de seguridad de NexaDigital S.A.S.

Se recomienda:

- Mantener el principio de mínimo privilegio.
- Registrar todas las acciones administrativas.
- Revisar periódicamente las cuentas activas.
- Eliminar accesos innecesarios.
- Proteger las credenciales de acceso.
- Auditar cambios relevantes en los usuarios.

---

# 21. Documentos Relacionados

Este documento complementa:

- Introducción.
- Primeros Pasos.
- Gestión de Roles.
- Gestión de Workspaces.
- Gestión de Documentos.
- Modelo de Permisos.
- Política de Seguridad.
- Manual del Administrador.

La presente documentación constituye la guía oficial para la administración de usuarios en Nexa Knowledge AI y define las operaciones necesarias para gestionar de forma segura y eficiente las cuentas de acceso dentro de la plataforma.