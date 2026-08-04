# Prompt Engineering

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Interno

---

# 1. Introducción

## Objetivo

El presente documento define la estrategia oficial de **Prompt Engineering** utilizada por Nexa Knowledge AI.

Su propósito es establecer los principios, estructuras y buenas prácticas para diseñar las instrucciones enviadas a los Modelos de Lenguaje (LLM), garantizando respuestas coherentes, seguras, consistentes y alineadas con la documentación empresarial.

---

# 2. Alcance

Este documento aplica a:

- Ingenieros de Inteligencia Artificial.
- Arquitectos de Software.
- Desarrolladores Backend.
- Equipos de Integración.
- Administradores de la plataforma.

Toda modificación de los prompts del sistema deberá respetar las directrices establecidas en este documento.

---

# 3. ¿Qué es un Prompt?

Un **Prompt** es el conjunto de instrucciones que recibe un Modelo de Lenguaje para realizar una tarea específica.

En Nexa Knowledge AI, un prompt no se limita a la pregunta del usuario, sino que incorpora múltiples elementos que orientan el comportamiento del modelo.

---

# 4. Objetivos del Prompt Engineering

La estrategia de Prompt Engineering busca:

- Obtener respuestas precisas.
- Reducir respuestas incorrectas.
- Mantener consistencia entre consultas.
- Guiar el comportamiento del modelo.
- Aplicar las políticas de seguridad.
- Aprovechar correctamente el contexto recuperado por RAG.

---

# 5. Componentes del Prompt

Cada solicitud enviada al LLM puede estar compuesta por los siguientes elementos:

- Instrucciones del sistema.
- Configuración del agente.
- Contexto documental.
- Historial de conversación (si aplica).
- Consulta del usuario.
- Restricciones de seguridad.
- Parámetros de generación.

La combinación de estos elementos conforma el prompt final.

---

# 6. Prompt del Sistema

El Prompt del Sistema define el comportamiento general del Agente IA.

Entre sus responsabilidades se encuentran:

- Definir el rol del asistente.
- Establecer el idioma de respuesta.
- Determinar el tono de comunicación.
- Indicar restricciones de seguridad.
- Priorizar el uso de la documentación empresarial.
- Evitar respuestas fuera del contexto autorizado.

Este prompt permanece oculto para el usuario final.

---

# 7. Consulta del Usuario

La consulta del usuario representa la intención principal de la interacción.

Puede formularse utilizando lenguaje natural sin necesidad de seguir una estructura específica.

Ejemplos:

- ¿Cuál es la política de vacaciones?
- ¿Cómo funciona la indexación?
- ¿Quién puede crear un Workspace?
- Resume el procedimiento de onboarding.

El sistema interpreta automáticamente la intención antes de generar la respuesta.

---

# 8. Contexto Recuperado

Antes de invocar al LLM, la arquitectura RAG incorpora al prompt el contexto documental recuperado.

Este contexto:

- Proviene de documentos autorizados.
- Ha sido seleccionado por el Retriever.
- Puede haber sido reorganizado mediante Re-ranking.
- Representa la principal fuente de conocimiento utilizada por el modelo.

---

# 9. Instrucciones de Seguridad

Todo prompt incorpora instrucciones para reforzar la seguridad.

Entre ellas:

- Respetar los permisos del usuario.
- Utilizar únicamente el contexto proporcionado.
- No inventar procedimientos inexistentes.
- No divulgar información no autorizada.
- Indicar cuando no exista evidencia suficiente para responder.

Estas instrucciones reducen el riesgo de respuestas incorrectas o no autorizadas.

---

# 10. Construcción del Prompt

El proceso de construcción del prompt sigue, de forma general, las siguientes etapas:

1. Validación del usuario.
2. Recuperación del contexto.
3. Aplicación de reglas de seguridad.
4. Incorporación del historial (cuando corresponda).
5. Integración de la consulta.
6. Generación del prompt final.
7. Envío al LLM.

Todo este proceso es transparente para el usuario.

---

# 11. Consistencia de las Respuestas

Los prompts deben diseñarse para producir respuestas consistentes.

Para ello se recomienda:

- Utilizar instrucciones claras.
- Evitar contradicciones.
- Mantener una estructura uniforme.
- Priorizar la documentación oficial.
- Reducir la ambigüedad.

---

# 12. Manejo del Historial

Cuando la conversación lo requiera, el prompt podrá incluir información de interacciones anteriores.

El historial permite:

- Mantener el contexto conversacional.
- Evitar preguntas repetitivas.
- Mejorar la continuidad de la conversación.

La cantidad de historial utilizada dependerá de la ventana de contexto disponible.

---

# 13. Manejo de Ambigüedad

Cuando una consulta sea ambigua, el sistema debe intentar:

- Utilizar el contexto disponible.
- Interpretar la intención del usuario.
- Solicitar aclaraciones cuando sea necesario.
- Evitar realizar suposiciones injustificadas.

---

# 14. Prevención de Alucinaciones

Para minimizar respuestas incorrectas, el Prompt Engineering incorpora estrategias como:

- Priorizar la documentación recuperada.
- Limitar la generación fuera del contexto.
- Solicitar que el modelo indique cuando no exista evidencia suficiente.
- Restringir respuestas basadas en conocimiento no documentado.

Estas prácticas mejoran la confiabilidad del sistema.

---

# 15. Plantillas de Prompt

La plataforma puede utilizar plantillas reutilizables para distintos escenarios.

Ejemplos:

- Preguntas y respuestas.
- Resúmenes.
- Comparación de documentos.
- Explicación de procedimientos.
- Extracción de información.
- Generación de listas.
- Asistencia técnica.

Cada plantilla adapta la estructura del prompt según el tipo de tarea.

---

# 16. Buenas Prácticas

Se recomienda:

- Mantener prompts simples y claros.
- Evitar instrucciones redundantes.
- Priorizar la información relevante.
- Mantener separados el contexto y las instrucciones.
- Revisar periódicamente la calidad de los prompts.
- Documentar cada modificación significativa.

---

# 17. Seguridad

Toda modificación en los prompts del sistema deberá:

- Ser revisada por el equipo responsable.
- Mantener la trazabilidad de los cambios.
- Respetar las políticas de seguridad.
- Evitar la exposición de información sensible.
- Preservar el comportamiento esperado del Agente IA.

---

# 18. Integración con Otros Componentes

Prompt Engineering trabaja conjuntamente con:

- Arquitectura RAG.
- Modelos LLM.
- Embeddings.
- Re-ranking.
- Guardrails.
- Gestión del Contexto.
- Chat IA.
- Configuración del Agente.

Estos componentes colaboran para construir el prompt final enviado al modelo.

---

# 19. Glosario

| Término | Descripción |
|----------|-------------|
| Prompt | Conjunto de instrucciones enviadas al modelo de lenguaje. |
| Prompt del Sistema | Instrucciones internas que definen el comportamiento del agente. |
| Prompt del Usuario | Consulta realizada por el usuario. |
| Contexto | Información recuperada de la base documental. |
| Historial | Conversaciones previas utilizadas para mantener continuidad. |
| Plantilla | Estructura reutilizable para construir prompts. |

---

# 20. Documentos Relacionados

Este documento complementa:

- Introducción a la IA.
- Arquitectura RAG.
- Modelos LLM.
- Embeddings.
- Re-ranking.
- Guardrails.
- Gestión del Contexto.
- Funcionamiento del Agente IA.
- Arquitectura Técnica.

La presente documentación constituye la guía oficial de Prompt Engineering de Nexa Knowledge AI y define los principios, estructuras y prácticas utilizadas para construir prompts seguros, consistentes y alineados con la arquitectura RAG, garantizando que las respuestas del Agente IA se fundamenten en la documentación empresarial autorizada y respeten las políticas de funcionamiento de la plataforma.