# Chat IA

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Público

---

# 1. Introducción

## Objetivo

El presente documento describe el funcionamiento del módulo **Chat IA** de Nexa Knowledge AI.

Su finalidad es explicar cómo los usuarios pueden interactuar con el Agente de Inteligencia Artificial para consultar información almacenada en la base de conocimiento de su organización utilizando lenguaje natural.

---

# 2. Alcance

Este documento aplica a todos los usuarios autorizados para utilizar el Chat IA dentro de un Workspace.

Las funcionalidades disponibles dependerán del rol asignado y de la configuración realizada por la organización.

---

# 3. ¿Qué es el Chat IA?

El Chat IA es la interfaz conversacional de Nexa Knowledge AI.

Permite realizar preguntas en lenguaje natural sobre la documentación empresarial almacenada en la plataforma.

El Agente IA analiza la consulta, recupera el contexto más relevante de la base de conocimiento y genera una respuesta fundamentada en los documentos autorizados para el usuario.

---

# 4. Objetivos del Chat IA

El Chat IA tiene como objetivos:

- Facilitar el acceso al conocimiento organizacional.
- Reducir los tiempos de búsqueda de información.
- Responder consultas utilizando documentación oficial.
- Mejorar la productividad de los colaboradores.
- Centralizar el acceso al conocimiento empresarial.
- Disminuir la dependencia de expertos para consultas repetitivas.

---

# 5. Acceso al Chat IA

El Chat IA puede abrirse desde el menú principal de la plataforma mediante la opción:

**Chat IA**

Al acceder, el usuario visualizará la interfaz conversacional y el historial de conversaciones disponibles, según sus permisos.

---

# 6. Interfaz del Chat

La interfaz puede incluir los siguientes elementos:

- Lista de conversaciones.
- Botón para iniciar una nueva conversación.
- Área de mensajes.
- Campo para escribir consultas.
- Botón de envío.
- Indicador de procesamiento.
- Información del Workspace activo.
- Opciones de configuración de la conversación.

La disposición puede variar según la versión de la plataforma.

---

# 7. Crear una Nueva Conversación

Para iniciar una conversación:

1. Acceder al módulo **Chat IA**.
2. Seleccionar **Nueva conversación**.
3. Escribir la primera consulta.
4. Enviar el mensaje.

La conversación quedará registrada en el historial del usuario.

---

# 8. Realizar una Consulta

Las consultas pueden formularse utilizando lenguaje natural.

Ejemplos:

- ¿Cuál es la política de vacaciones?
- ¿Cómo se configura un Workspace?
- ¿Qué permisos tiene un Supervisor?
- ¿Cuál es el procedimiento para realizar un respaldo?
- ¿Cómo funciona la arquitectura RAG?

No es necesario utilizar palabras clave específicas.

---

# 9. Procesamiento de la Consulta

Cuando un usuario envía una pregunta, la plataforma ejecuta un proceso similar al siguiente:

1. Validación del usuario.
2. Identificación del Workspace activo.
3. Verificación de permisos.
4. Recuperación de información relevante.
5. Construcción del contexto.
6. Generación de la respuesta mediante el modelo de IA.
7. Presentación de la respuesta al usuario.

Todo el proceso se realiza utilizando únicamente la información autorizada para el usuario.

---

# 10. Interpretación de las Respuestas

Las respuestas generadas por el Agente IA deben entenderse como una interpretación del contenido disponible en la base de conocimiento.

Cuando la documentación contiene información suficiente, la respuesta buscará ser:

- Clara.
- Precisa.
- Coherente.
- Basada en los documentos indexados.

Si la información no está disponible, el sistema podrá indicar que no dispone de evidencia suficiente para responder.

---

# 11. Contexto Documental

El Chat IA utiliza la documentación disponible en el Workspace activo como fuente principal para generar respuestas.

Esto significa que:

- No consulta documentos fuera del Workspace autorizado.
- No utiliza documentación perteneciente a otras organizaciones.
- Respeta las restricciones de acceso definidas por la plataforma.

El contexto utilizado dependerá de los documentos previamente cargados e indexados.

---

# 12. Historial de Conversaciones

Cada usuario podrá consultar las conversaciones previamente realizadas, según la configuración de la organización.

El historial permite:

- Reanudar conversaciones.
- Revisar respuestas anteriores.
- Consultar preguntas realizadas.
- Mantener continuidad en una sesión de trabajo.

La disponibilidad del historial dependerá de las políticas definidas por la organización.

---

# 13. Calidad de las Consultas

Para obtener mejores respuestas se recomienda:

- Formular preguntas específicas.
- Incluir suficiente contexto.
- Evitar varias preguntas distintas en un mismo mensaje.
- Utilizar terminología utilizada por la organización.
- Formular preguntas relacionadas con un único tema.

Las consultas claras permiten mejorar la recuperación de información y la calidad de las respuestas.

---

# 14. Limitaciones

El Chat IA responde únicamente utilizando la información disponible en la base de conocimiento autorizada.

Por esta razón:

- No inventa procedimientos inexistentes.
- No reemplaza documentación oficial.
- No responde sobre información que no haya sido incorporada al sistema.
- No puede acceder a documentos sin autorización.
- No modifica documentos automáticamente.

La calidad de las respuestas depende directamente de la calidad y actualización de la documentación disponible.

---

# 15. Buenas Prácticas

Se recomienda:

- Mantener actualizada la documentación.
- Formular preguntas concretas.
- Revisar la respuesta antes de utilizarla en procesos críticos.
- Utilizar conversaciones independientes para temas diferentes.
- Reportar respuestas inesperadas al administrador o al equipo de soporte.

Estas prácticas contribuyen a obtener resultados más consistentes.

---

# 16. Seguridad

Durante el uso del Chat IA:

- Las respuestas respetan los permisos del usuario.
- Solo se consulta documentación autorizada.
- Las conversaciones pueden registrarse para fines de auditoría.
- La información debe tratarse conforme a las políticas de seguridad de la organización.

Los usuarios no deberán compartir información confidencial fuera de los canales autorizados.

---

# 17. Problemas Frecuentes

| Situación | Acción recomendada |
|-----------|--------------------|
| No obtengo respuesta | Verificar la conexión y volver a intentar la consulta. |
| La respuesta no contiene la información esperada | Confirmar que los documentos estén cargados e indexados en el Workspace correspondiente. |
| El Agente IA indica que no encontró información | Revisar si la documentación existe y si el usuario tiene permisos para acceder a ella. |
| No aparecen conversaciones anteriores | Verificar las políticas de retención del historial y los permisos asignados. |
| La respuesta parece incompleta | Reformular la pregunta incluyendo más contexto o dividirla en consultas más específicas. |

---

# 18. Recomendaciones para Obtener Mejores Respuestas

Para mejorar la calidad de las respuestas se recomienda:

- Utilizar nombres completos de documentos o procesos cuando sean conocidos.
- Referirse a políticas, manuales o procedimientos específicos.
- Formular una pregunta por mensaje.
- Evitar términos ambiguos.
- Utilizar el vocabulario oficial de la organización.

Una documentación bien estructurada y actualizada incrementa significativamente la precisión de las respuestas del Agente IA.

---

# 19. Integración con Otros Módulos

El Chat IA interactúa con diferentes componentes de la plataforma:

- Gestión de Usuarios.
- Gestión de Roles.
- Gestión de Workspaces.
- Gestión de Documentos.
- Arquitectura RAG.
- Motor de Indexación.
- Auditoría.
- Configuración Global.

Estas integraciones permiten ofrecer respuestas seguras, contextualizadas y alineadas con la información oficial de la organización.

---

# 20. Documentos Relacionados

Este documento complementa:

- Introducción.
- Primeros Pasos.
- Gestión de Usuarios.
- Gestión de Roles.
- Gestión de Workspaces.
- Gestión de Documentos.
- Arquitectura RAG.
- Funcionamiento del Agente IA.
- Manual del Administrador.
- FAQ.

El presente documento constituye la guía oficial de uso del Chat IA de Nexa Knowledge AI y establece las prácticas recomendadas para interactuar con el Agente de Inteligencia Artificial, realizar consultas sobre la base de conocimiento empresarial y obtener respuestas fundamentadas en la documentación autorizada de la organización.