# Modelo de Permisos

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión:** 1.0

---

# 1. Introducción

## Objetivo

Este documento define el modelo oficial de autorización utilizado por Nexa Knowledge AI.

El objetivo del modelo es garantizar que cada usuario pueda acceder únicamente a los recursos y operaciones para los cuales ha sido autorizado.

Todas las verificaciones de permisos realizadas por la plataforma deberán respetar las reglas aquí descritas.

---

# 2. Principios del Modelo

El modelo de permisos de Nexa Knowledge AI se basa en los siguientes principios:

- Mínimo privilegio.
- Denegación por defecto.
- Herencia controlada.
- Segregación de funciones.
- Trazabilidad.
- Seguridad por diseño.
- Autorización explícita.
- Auditoría obligatoria.

---

# 3. Niveles de Seguridad

La autorización se evalúa en diferentes niveles.

1. Organización
2. Workspace
3. Colección
4. Documento
5. Agente IA
6. Conversación
7. Recurso específico

Cada nivel puede definir permisos propios.

---

# 4. Roles Predeterminados

La plataforma incorpora los siguientes roles base.

## Super Administrador

Responsable de la administración global de la plataforma.

Puede administrar cualquier organización y acceder a todas las funciones del sistema.

---

## Administrador

Administra una organización específica.

Responsabilidades:

- Usuarios
- Workspaces
- Documentos
- Colecciones
- Agentes IA
- Configuración
- Licencias

---

## Supervisor

Gestiona equipos y recursos asignados.

Puede administrar contenido sin modificar la configuración global de la organización.

---

## Editor

Puede crear y modificar contenido.

No puede administrar usuarios ni configuraciones críticas.

---

## Colaborador

Puede consultar información y participar en la creación de contenido según los permisos asignados.

---

## Lector

Acceso exclusivo de lectura.

No puede modificar recursos.

---

# 5. Recursos Protegidos

Los permisos pueden aplicarse sobre los siguientes recursos.

- Organización
- Usuario
- Workspace
- Colección
- Documento
- Agente IA
- Conversación
- Auditoría
- Configuración
- Integración
- Facturación

---

# 6. Operaciones

Cada recurso puede definir una o más operaciones autorizadas.

Operaciones estándar:

- Crear
- Leer
- Actualizar
- Eliminar
- Administrar
- Compartir
- Exportar
- Publicar
- Restaurar
- Configurar

---

# 7. Matriz General de Permisos

| Recurso | Lector | Colaborador | Editor | Supervisor | Administrador | Super Administrador |
|----------|:------:|:-----------:|:------:|:----------:|:-------------:|:-------------------:|
| Organizaciones | Leer | — | — | Leer | Administrar | Administrar |
| Usuarios | Leer | Leer | Leer | Administrar equipo | Administrar | Administrar |
| Workspaces | Leer | Leer | Crear / Editar | Administrar | Administrar | Administrar |
| Colecciones | Leer | Leer | Crear / Editar | Administrar | Administrar | Administrar |
| Documentos | Leer | Cargar | Crear / Editar | Administrar | Administrar | Administrar |
| Agentes IA | Usar | Usar | Crear / Editar | Administrar | Administrar | Administrar |
| Conversaciones | Administrar propias | Administrar propias | Administrar propias | Administrar propias | Administrar | Administrar |
| Auditoría | — | — | — | Lectura | Administrar | Administrar |
| Configuración | — | — | — | — | Administrar | Administrar |
| Facturación | — | — | — | — | Lectura | Administrar |

---

# 8. Permisos sobre Documentos

## Leer

Permite consultar el contenido de un documento.

Incluye:

- Visualización.
- Búsqueda.
- Consultas mediante IA.

---

## Crear

Permite cargar nuevos documentos.

---

## Actualizar

Permite modificar un documento existente.

---

## Eliminar

Permite realizar la eliminación lógica del documento.

---

## Restaurar

Permite recuperar versiones anteriores.

---

## Compartir

Permite otorgar acceso a otros usuarios autorizados.

---

# 9. Permisos sobre Agentes IA

## Crear Agente

Crear un nuevo agente especializado.

---

## Editar Agente

Modificar configuración.

---

## Publicar Agente

Habilitar el uso por otros usuarios.

---

## Desactivar Agente

Suspender temporalmente un agente.

---

## Eliminar Agente

Eliminar definitivamente un agente.

---

## Configurar Herramientas

Agregar o quitar herramientas autorizadas.

---

## Configurar Colecciones

Definir sobre qué conocimiento puede responder un agente.

---

## Configurar Modelo IA

Seleccionar el modelo de lenguaje utilizado.

---

# 10. Herencia de Permisos

Los permisos pueden heredarse.

Ejemplo.

```
Organización

↓

Workspace

↓

Colección

↓

Documento
```

Una autorización concedida sobre un Workspace podrá heredarse por sus colecciones y documentos, salvo que exista una regla específica que la restrinja.

---

# 11. Permisos Explícitos

Los permisos explícitos tienen prioridad sobre los heredados.

Ejemplo.

```
Workspace

Permite Leer

↓

Documento

Deniega Leer
```

Resultado:

El documento permanecerá inaccesible.

---

# 12. Evaluación de Autorización

Antes de ejecutar cualquier operación el sistema deberá verificar:

1. Usuario autenticado.
2. Organización activa.
3. Rol asignado.
4. Permiso explícito.
5. Permiso heredado.
6. Restricciones del recurso.
7. Estado del recurso.
8. Políticas de seguridad.

Solo si todas las verificaciones son satisfactorias se autorizará la operación.

---

# 13. Acceso mediante Agentes IA

Los Agentes IA nunca podrán responder utilizando información para la cual el usuario no tenga autorización.

Antes de recuperar contexto, el sistema deberá filtrar los documentos accesibles para el usuario.

Este comportamiento es obligatorio para todas las consultas.

---

# 14. Auditoría

Las siguientes operaciones deberán registrarse:

- Cambio de rol.
- Cambio de permisos.
- Creación de usuarios.
- Eliminación de usuarios.
- Publicación de agentes.
- Eliminación de documentos.
- Cambios en la configuración.
- Integraciones externas.
- Modificaciones sobre políticas de seguridad.

---

# 15. Escenarios de Ejemplo

## Escenario 1

**Pregunta:** ¿Puede un Lector eliminar documentos?

**Respuesta:** No. El rol Lector solo dispone de permisos de lectura.

---

## Escenario 2

**Pregunta:** ¿Puede un Editor crear un Agente IA?

**Respuesta:** Sí, siempre que la organización le haya concedido el permiso correspondiente.

---

## Escenario 3

**Pregunta:** ¿Puede un Colaborador cambiar el modelo de IA de un agente?

**Respuesta:** No. Esa operación requiere permisos de administración del agente.

---

## Escenario 4

**Pregunta:** ¿Puede un Supervisor consultar la auditoría?

**Respuesta:** Sí, si la organización le ha concedido acceso de lectura sobre el módulo de auditoría.

---

## Escenario 5

**Pregunta:** ¿Puede un Administrador exportar conversaciones?

**Respuesta:** Sí, siempre que las políticas de seguridad y retención de datos de la organización lo permitan.

---

# 16. Relación con otros documentos

Este documento complementa:

- Base de Conocimiento del Producto.
- Modelo de Dominio.
- Catálogo de Funcionalidades.
- Casos de Uso.
- Reglas de Negocio.

Las decisiones de autorización descritas en este documento prevalecen sobre cualquier comportamiento funcional no especificado en otros documentos.