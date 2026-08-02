# Gestión de Workspaces

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Público

---

# 1. Introducción

## Objetivo

El presente documento describe el funcionamiento del módulo de Gestión de Workspaces de Nexa Knowledge AI.

Su propósito es definir la administración de los espacios de trabajo donde las organizaciones almacenan documentos, administran usuarios autorizados y realizan consultas mediante Inteligencia Artificial.

---

# 2. Alcance

Este documento aplica a administradores y usuarios con permisos para crear, administrar o utilizar Workspaces dentro de una organización.

Las funcionalidades disponibles dependerán del rol asignado.

---

# 3. ¿Qué es un Workspace?

Un Workspace es un espacio de trabajo independiente dentro de una organización.

Cada Workspace agrupa un conjunto específico de:

- Documentos.
- Usuarios.
- Conversaciones.
- Configuraciones.
- Recursos.
- Permisos.

Su objetivo es organizar el conocimiento empresarial por áreas, proyectos o departamentos, manteniendo el aislamiento lógico entre la información.

---

# 4. Beneficios de Utilizar Workspaces

El uso de Workspaces permite:

- Organizar la información por departamentos.
- Separar proyectos independientes.
- Restringir el acceso a información sensible.
- Facilitar la administración documental.
- Mejorar la calidad de las respuestas del Agente IA.
- Reducir la exposición innecesaria de información.

---

# 5. Acceso al Módulo

Los usuarios autorizados podrán acceder mediante:

**Administración → Workspaces**

Dependiendo del rol asignado, las opciones disponibles podrán variar.

---

# 6. Listado de Workspaces

El sistema muestra un listado de los Workspaces disponibles dentro de la organización.

Generalmente incluye:

- Nombre.
- Descripción.
- Estado.
- Número de documentos.
- Número de usuarios.
- Fecha de creación.
- Responsable.
- Última actualización.

---

# 7. Crear un Workspace

Para crear un nuevo Workspace:

1. Acceder al módulo **Workspaces**.
2. Seleccionar **Nuevo Workspace**.
3. Registrar el nombre.
4. Ingresar una descripción.
5. Definir el responsable.
6. Configurar las opciones iniciales.
7. Guardar la información.

Una vez creado, el Workspace estará disponible para incorporar usuarios y documentos.

---

# 8. Configuración General

Cada Workspace puede disponer de configuraciones propias, entre ellas:

- Nombre.
- Descripción.
- Estado.
- Idioma principal.
- Zona horaria.
- Configuración de indexación.
- Configuración del Agente IA.
- Límites operativos.

Las opciones disponibles dependerán de la versión de la plataforma.

---

# 9. Administración de Miembros

Los administradores podrán gestionar los usuarios que participan en un Workspace.

Las operaciones disponibles incluyen:

- Agregar usuarios.
- Eliminar usuarios.
- Cambiar permisos.
- Asignar roles.
- Consultar miembros.

Cada usuario únicamente visualizará la información correspondiente a los Workspaces autorizados.

---

# 10. Organización de Documentos

Los documentos almacenados en un Workspace constituyen su base de conocimiento.

Dentro de cada Workspace es posible administrar:

- Manuales.
- Políticas.
- Procedimientos.
- Informes.
- Documentación técnica.
- Hojas de cálculo.
- Presentaciones.

Toda la información permanece asociada al Workspace donde fue incorporada.

---

# 11. Aislamiento de Información

Cada Workspace mantiene un aislamiento lógico respecto de los demás.

Esto implica que:

- Los documentos no se comparten automáticamente.
- Las conversaciones permanecen independientes.
- Los permisos son específicos.
- Las búsquedas se realizan únicamente sobre la documentación autorizada.

Este aislamiento contribuye a preservar la confidencialidad de la información.

---

# 12. Uso del Agente IA

Las consultas realizadas por los usuarios utilizan únicamente la información disponible en el Workspace activo.

Durante el procesamiento de una consulta:

1. El usuario envía una pregunta.
2. El sistema identifica el Workspace activo.
3. Se recuperan documentos autorizados.
4. El motor RAG selecciona el contexto relevante.
5. El Agente IA genera una respuesta.

Esto garantiza que las respuestas se fundamenten exclusivamente en la documentación correspondiente.

---

# 13. Configuración de Permisos

Cada Workspace posee un conjunto independiente de permisos.

Los administradores pueden controlar:

- Usuarios autorizados.
- Roles disponibles.
- Acceso a documentos.
- Acceso al Chat IA.
- Administración del Workspace.

Las configuraciones deberán respetar el modelo general de autorización de la plataforma.

---

# 14. Estados del Workspace

Un Workspace puede encontrarse en diferentes estados.

## Activo

Disponible para todos los usuarios autorizados.

## Inactivo

No admite nuevas operaciones hasta ser reactivado.

## Archivado

Se conserva para consulta o auditoría, sin utilizarse como Workspace operativo.

---

# 15. Búsqueda de Workspaces

Cuando existan múltiples espacios de trabajo, la plataforma permite realizar búsquedas mediante:

- Nombre.
- Responsable.
- Estado.
- Fecha de creación.
- Etiquetas.
- Área de negocio.

También pueden aplicarse filtros combinados para facilitar la administración.

---

# 16. Buenas Prácticas

Se recomienda:

- Crear un Workspace por área o proyecto.
- Evitar mezclar documentación de diferentes unidades de negocio.
- Asignar responsables claramente identificados.
- Revisar periódicamente los miembros.
- Eliminar accesos innecesarios.
- Mantener una estructura documental organizada.
- Utilizar nombres descriptivos y consistentes.

---

# 17. Problemas Frecuentes

| Situación | Acción recomendada |
|-----------|--------------------|
| No aparece un Workspace | Verificar los permisos del usuario y la organización seleccionada. |
| No puedo acceder a los documentos | Confirmar que el usuario pertenezca al Workspace. |
| El Agente IA no encuentra información | Verificar que los documentos estén correctamente cargados e indexados. |
| No puedo agregar usuarios | Confirmar que el rol posea permisos administrativos. |
| El Workspace está inactivo | Solicitar su reactivación a un administrador autorizado. |

---

# 18. Seguridad

La administración de Workspaces deberá seguir las políticas de seguridad definidas por la organización.

Se recomienda:

- Limitar el acceso únicamente a usuarios autorizados.
- Revisar periódicamente la membresía.
- Registrar cambios administrativos.
- Evitar compartir Workspaces innecesariamente.
- Mantener la documentación actualizada.
- Auditar las actividades relevantes.

---

# 19. Ciclo de Vida del Workspace

El ciclo de vida habitual comprende:

1. Creación.
2. Configuración inicial.
3. Incorporación de usuarios.
4. Carga de documentos.
5. Indexación.
6. Uso operativo.
7. Mantenimiento.
8. Archivado o eliminación conforme a las políticas de la organización.

Cada etapa deberá documentarse adecuadamente para garantizar la trazabilidad.

---

# 20. Integración con Otros Módulos

El módulo de Workspaces interactúa con:

- Gestión de Usuarios.
- Gestión de Roles.
- Gestión de Documentos.
- Chat IA.
- Arquitectura RAG.
- Administración.
- Auditoría.

Estas integraciones permiten ofrecer una administración coherente y segura del conocimiento empresarial.

---

# 21. Documentos Relacionados

Este documento complementa:

- Introducción.
- Primeros Pasos.
- Gestión de Usuarios.
- Gestión de Roles.
- Gestión de Documentos.
- Arquitectura RAG.
- Funcionamiento del Agente IA.
- Manual del Administrador.
- Política de Seguridad.

La presente documentación constituye la guía oficial para la administración de Workspaces en Nexa Knowledge AI y define las prácticas recomendadas para organizar, proteger y gestionar la información empresarial utilizada por el Agente de Inteligencia Artificial.