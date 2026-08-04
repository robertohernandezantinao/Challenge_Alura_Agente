# Guardrails

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Interno

---

# 1. Introducción

## Objetivo

El presente documento define la arquitectura de **Guardrails** implementada en Nexa Knowledge AI.

Su objetivo es establecer los mecanismos de control que garantizan que el Agente IA opere de forma segura, confiable y alineada con las políticas de la organización, evitando comportamientos no deseados y reduciendo los riesgos asociados al uso de Modelos de Lenguaje (LLM).

---

# 2. Alcance

Este documento aplica a:

- Arquitectos de Software.
- Ingenieros de Inteligencia Artificial.
- Equipos de Seguridad.
- Desarrolladores Backend.
- Administradores de la plataforma.

Los Guardrails forman parte obligatoria del flujo de procesamiento de todas las consultas realizadas al Agente IA.

---

# 3. ¿Qué son los Guardrails?

Los Guardrails son un conjunto de controles que supervisan el comportamiento del Agente IA antes, durante y después de la interacción con el Modelo de Lenguaje.

Su función consiste en garantizar que las respuestas:

- Respeten la documentación empresarial.
- Cumplan las políticas de seguridad.
- No expongan información restringida.
- Mantengan un comportamiento consistente.
- Respondan únicamente dentro del contexto autorizado.

---

# 4. Objetivos

La arquitectura de Guardrails busca:

- Proteger la información empresarial.
- Reducir respuestas incorrectas.
- Prevenir ataques sobre el modelo.
- Garantizar el cumplimiento de permisos.
- Mantener la calidad de las respuestas.
- Incrementar la confiabilidad del sistema.

---

# 5. Posición dentro de la Arquitectura

Los Guardrails intervienen en múltiples etapas del flujo RAG.

Flujo simplificado:

1. Usuario realiza una consulta.
2. Validación inicial.
3. Controles de entrada.
4. Recuperación documental.
5. Construcción del contexto.
6. Ejecución del LLM.
7. Validación de la respuesta.
8. Entrega al usuario.

Los controles se aplican tanto antes como después de la generación de la respuesta.

---

# 6. Validación de Entradas

Antes de procesar una consulta, el sistema verifica:

- Formato válido.
- Longitud permitida.
- Codificación correcta.
- Caracteres no válidos.
- Solicitudes maliciosas conocidas.
- Consistencia de la petición.

Las consultas que incumplan las políticas podrán ser rechazadas o registradas para auditoría.

---

# 7. Protección contra Prompt Injection

La plataforma implementa mecanismos para reducir el impacto de ataques de **Prompt Injection**.

Entre ellos:

- Aislamiento del Prompt del Sistema.
- Separación entre instrucciones y contexto.
- Filtrado de instrucciones maliciosas.
- Restricción de cambios de comportamiento.
- Validación de solicitudes sospechosas.

El objetivo es impedir que el usuario modifique el comportamiento interno del agente.

---

# 8. Protección de Información Sensible

Los Guardrails impiden que el modelo divulgue información protegida.

Se controla especialmente:

- Credenciales.
- Tokens.
- Secretos.
- Información confidencial.
- Datos restringidos por permisos.
- Información perteneciente a otros Workspaces.

La protección se mantiene incluso si el usuario intenta obtener dicha información mediante instrucciones indirectas.

---

# 9. Validación del Contexto

Antes de enviar información al LLM, el sistema verifica que:

- Todos los fragmentos pertenezcan al Workspace correspondiente.
- Los permisos sean válidos.
- No existan duplicados.
- El contexto sea coherente.
- Se respete la ventana máxima permitida.

---

# 10. Validación de Salidas

Una vez generada la respuesta, los Guardrails realizan una revisión final.

Entre otros aspectos se verifica:

- Consistencia con la documentación.
- Ausencia de información restringida.
- Cumplimiento de políticas internas.
- Formato esperado.
- Calidad mínima de la respuesta.

Solo las respuestas aprobadas son entregadas al usuario.

---

# 11. Gestión de Errores

Cuando una respuesta no supera las validaciones, el sistema puede:

- Regenerar la respuesta.
- Solicitar nueva recuperación documental.
- Reducir el contexto.
- Informar que no existe información suficiente.
- Registrar el incidente para análisis posterior.

---

# 12. Registro y Auditoría

Toda intervención relevante de los Guardrails puede registrarse para auditoría.

Los registros pueden incluir:

- Fecha y hora.
- Usuario.
- Workspace.
- Consulta.
- Tipo de validación aplicada.
- Resultado de la validación.
- Motivo del rechazo (cuando corresponda).

Estos registros facilitan la investigación de incidentes y la mejora continua.

---

# 13. Configuración

Los Guardrails son configurables mediante parámetros administrativos.

Es posible definir:

- Reglas de validación.
- Límites de longitud.
- Políticas de respuesta.
- Umbrales de confianza.
- Reglas de filtrado.
- Comportamientos específicos por organización.

La configuración puede adaptarse a las necesidades de cada cliente.

---

# 14. Escalabilidad

La arquitectura está diseñada para incorporar nuevos mecanismos de control sin modificar el resto del sistema.

Esto permite añadir:

- Nuevos detectores de amenazas.
- Validaciones específicas por industria.
- Controles regulatorios.
- Políticas de cumplimiento normativo.
- Integraciones con herramientas externas de seguridad.

---

# 15. Limitaciones

Los Guardrails reducen significativamente los riesgos, pero no eliminan completamente todas las posibilidades de respuestas incorrectas.

Por ello deben complementarse con:

- Documentación de calidad.
- Configuración adecuada del sistema.
- Monitoreo continuo.
- Evaluaciones periódicas del Agente IA.

---

# 16. Buenas Prácticas

Se recomienda:

- Revisar periódicamente las reglas de validación.
- Mantener actualizadas las políticas de seguridad.
- Registrar eventos relevantes.
- Evaluar incidentes de forma continua.
- Ajustar los controles según la evolución de los modelos de IA.

---

# 17. Integración con Otros Componentes

Los Guardrails interactúan con:

- Arquitectura RAG.
- Prompt Engineering.
- Modelos LLM.
- Embeddings.
- Re-ranking.
- Gestión del Contexto.
- Gestión de Usuarios.
- Gestión de Roles.
- Auditoría.
- Seguridad.

Constituyen la principal capa de control del comportamiento del Agente IA.

---

# 18. Glosario

| Término | Descripción |
|----------|-------------|
| Guardrails | Conjunto de controles que regulan el comportamiento del Agente IA. |
| Prompt Injection | Ataque que intenta modificar las instrucciones internas del modelo. |
| Validación | Proceso mediante el cual se verifica el cumplimiento de las políticas definidas. |
| Contexto | Información enviada al modelo para generar una respuesta. |
| Auditoría | Registro de eventos relacionados con la operación del sistema. |
| Política | Regla utilizada para controlar el comportamiento del Agente IA. |

---

# 19. Documentos Relacionados

Este documento complementa:

- Introducción a la IA.
- Arquitectura RAG.
- Modelos LLM.
- Embeddings.
- Prompt Engineering.
- Re-ranking.
- Gestión del Contexto.
- Evaluación del Sistema IA.
- Política de Seguridad.
- Arquitectura Técnica.

La presente documentación constituye la guía oficial sobre la arquitectura de Guardrails de Nexa Knowledge AI y establece los controles técnicos y funcionales que permiten proteger la información empresarial, validar el comportamiento del Agente IA y garantizar que todas las respuestas generadas sean seguras, consistentes y alineadas con las políticas de la organización.