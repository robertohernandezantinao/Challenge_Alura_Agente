# Manual del Administrador

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

---

# 1. Introducción

## Objetivo

Este documento define las responsabilidades, procedimientos y buenas prácticas para la administración de Nexa Knowledge AI.

Está dirigido a administradores de plataforma, administradores de organización y personal autorizado encargado de mantener la operación del sistema.

Su propósito es garantizar una administración segura, consistente y alineada con las políticas de NexaDigital S.A.S.

---

# 2. Perfil del Administrador

El Administrador es responsable de configurar, mantener y supervisar la plataforma dentro de su ámbito de responsabilidad.

Dependiendo del modelo de despliegue, podrán existir distintos niveles de administración.

## Administrador Global

Responsable de la plataforma completa.

Puede administrar:

- Organizaciones.
- Configuración global.
- Seguridad.
- Integraciones.
- Infraestructura lógica.
- Parámetros generales.

---

## Administrador de Organización

Responsable de una organización específica.

Puede administrar:

- Usuarios.
- Roles.
- Workspaces.
- Colecciones.
- Documentos.
- Agentes IA.
- Configuración propia de la organización.

No puede modificar configuraciones globales de la plataforma.

---

# 3. Responsabilidades

El administrador deberá:

- Mantener la plataforma operativa.
- Gestionar usuarios.
- Administrar permisos.
- Supervisar la seguridad.
- Mantener organizada la Base de Conocimiento.
- Revisar auditorías.
- Resolver incidencias administrativas.
- Garantizar el cumplimiento de las políticas internas.

---

# 4. Panel de Administración

El panel administrativo centraliza todas las funciones de gestión.

Incluye módulos para:

- Organizaciones.
- Usuarios.
- Roles.
- Permisos.
- Workspaces.
- Colecciones.
- Documentos.
- Agentes IA.
- Auditoría.
- Configuración.
- Monitoreo.

---

# 5. Gestión de Organizaciones

Desde este módulo es posible:

- Crear organizaciones.
- Editar información general.
- Activar organizaciones.
- Suspender organizaciones.
- Eliminar organizaciones según las políticas establecidas.
- Consultar estadísticas generales.

Cada organización mantiene aislamiento lógico respecto de las demás.

---

# 6. Gestión de Usuarios

El administrador puede:

- Invitar usuarios.
- Editar información.
- Restablecer contraseñas.
- Activar cuentas.
- Desactivar cuentas.
- Bloquear usuarios.
- Desbloquear usuarios.
- Eliminar usuarios.

Todas las acciones quedan registradas en el sistema de auditoría.

---

# 7. Gestión de Roles y Permisos

El sistema implementa un modelo de autorización basado en roles.

Las funciones principales incluyen:

- Asignar roles.
- Revocar roles.
- Revisar permisos efectivos.
- Aplicar el principio de mínimo privilegio.
- Validar accesos.

Los permisos deben revisarse periódicamente.

---

# 8. Gestión de Workspaces

El administrador puede:

- Crear nuevos Workspaces.
- Modificar su configuración.
- Asignar responsables.
- Definir usuarios autorizados.
- Archivar Workspaces.
- Eliminar Workspaces cuando corresponda.

Cada Workspace representa un espacio independiente de trabajo.

---

# 9. Gestión de Colecciones

Las colecciones permiten organizar la documentación.

El administrador podrá:

- Crear colecciones.
- Editarlas.
- Asignar permisos.
- Cambiar responsables.
- Archivar colecciones.
- Eliminar colecciones.

Se recomienda mantener una estructura simple y coherente.

---

# 10. Gestión de Documentos

Entre las funciones disponibles:

- Cargar documentos.
- Aprobar publicaciones.
- Actualizar versiones.
- Reprocesar documentos.
- Reindexar contenido.
- Archivar documentos.
- Restaurar versiones.
- Eliminar documentos.

El administrador deberá supervisar periódicamente el estado de procesamiento e indexación.

---

# 11. Gestión de Agentes IA

Los administradores podrán:

- Crear Agentes IA.
- Configurar instrucciones.
- Asociar colecciones.
- Asignar modelos de lenguaje.
- Definir parámetros de recuperación.
- Activar o desactivar Agentes.
- Supervisar su funcionamiento.

Cada Agente IA podrá estar especializado en un dominio específico.

---

# 12. Supervisión del procesamiento

El panel permite consultar el estado de:

- Procesamiento documental.
- Extracción de contenido.
- Chunking.
- Generación de embeddings.
- Indexación.
- Sincronización de la Base Vectorial.

Los documentos con errores deberán revisarse antes de estar disponibles para los usuarios.

---

# 13. Auditoría

El administrador puede consultar los registros de auditoría relacionados con:

- Inicios de sesión.
- Cambios de configuración.
- Creación de usuarios.
- Cambios de permisos.
- Carga de documentos.
- Eliminaciones.
- Consultas administrativas.
- Eventos de seguridad.

La auditoría facilita el cumplimiento normativo y el análisis de incidentes.

---

# 14. Monitoreo

El panel proporciona indicadores sobre:

- Usuarios activos.
- Organizaciones.
- Workspaces.
- Documentos indexados.
- Procesamientos pendientes.
- Consultas realizadas.
- Uso de Agentes IA.
- Estado de los servicios.

Estos indicadores permiten detectar problemas de forma temprana.

---

# 15. Seguridad

El administrador deberá garantizar:

- Uso obligatorio de autenticación multifactor cuando la política lo requiera.
- Rotación periódica de credenciales administrativas.
- Revisión de permisos.
- Gestión segura de accesos privilegiados.
- Eliminación de cuentas inactivas.
- Protección de información sensible.

---

# 16. Buenas prácticas

Se recomienda:

- Revisar periódicamente la auditoría.
- Mantener actualizada la documentación.
- Eliminar usuarios inactivos.
- Validar permisos antes de conceder accesos.
- Organizar correctamente las colecciones.
- Evitar documentos duplicados.
- Supervisar la indexación.
- Revisar los indicadores de salud del sistema.

---

# 17. Problemas frecuentes

## Un documento no aparece en las consultas

Verifique:

- Estado de procesamiento.
- Estado de indexación.
- Permisos.
- Workspace.
- Colección.
- Configuración del Agente IA.

---

## Un usuario no puede acceder

Compruebe:

- Estado de la cuenta.
- Organización activa.
- Rol asignado.
- Permisos efectivos.
- Configuración de autenticación.

---

## Un Agente IA responde incorrectamente

Revise:

- Documentación disponible.
- Configuración del Agente.
- Colecciones asociadas.
- Estado de indexación.
- Recuperación de contexto.

---

# 18. Lista de verificación operativa

Se recomienda realizar las siguientes tareas de forma periódica.

## Diariamente

- Revisar errores de procesamiento.
- Supervisar documentos pendientes.
- Verificar incidencias críticas.

---

## Semanalmente

- Revisar usuarios activos.
- Analizar registros de auditoría.
- Comprobar el estado de los Agentes IA.

---

## Mensualmente

- Revisar permisos.
- Archivar documentación obsoleta.
- Validar la organización de Workspaces y Colecciones.
- Revisar indicadores de uso.

---

# 19. Relación con otros documentos

Este documento complementa:

- Configuración Global.
- Modelo de Permisos.
- Gestión de Usuarios.
- Gestión de Documentos.
- Arquitectura RAG.
- Arquitectura Técnica.
- Política de Seguridad.
- Solución de Problemas.
- FAQ.

El Manual del Administrador constituye la guía oficial para la operación administrativa de Nexa Knowledge AI y define las responsabilidades y procedimientos necesarios para garantizar una plataforma segura, organizada y disponible para todos los usuarios autorizados.