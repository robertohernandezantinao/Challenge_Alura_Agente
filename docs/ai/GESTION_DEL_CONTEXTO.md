# Gestión del Contexto

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Interno

---

# 1. Introducción

## Objetivo

El presente documento define la estrategia oficial de **Gestión del Contexto** utilizada por Nexa Knowledge AI.

Su finalidad es describir cómo la plataforma construye, organiza, optimiza y administra la información enviada al Modelo de Lenguaje (LLM), garantizando respuestas precisas, consistentes y fundamentadas en la documentación empresarial autorizada.

---

# 2. Alcance

Este documento aplica a:

- Arquitectos de Software.
- Ingenieros de Inteligencia Artificial.
- Desarrolladores Backend.
- Administradores de la plataforma.
- Equipos responsables de la arquitectura RAG.

La Gestión del Contexto constituye una etapa crítica dentro del flujo de generación de respuestas del Agente IA.

---

# 3. ¿Qué es el Contexto?

El **contexto** es el conjunto de información que el sistema entrega al Modelo de Lenguaje para responder una consulta.

Está compuesto por información previamente seleccionada mediante los mecanismos de recuperación documental y validada conforme a las políticas de seguridad de la plataforma.

El modelo únicamente puede generar respuestas utilizando el contexto recibido.

---

# 4. Objetivos

La Gestión del Contexto busca:

- Maximizar la precisión de las respuestas.
- Reducir información irrelevante.
- Optimizar el uso de la ventana de contexto del LLM.
- Disminuir el consumo de tokens.
- Mantener la coherencia documental.
- Respetar los permisos de acceso.

---

# 5. Componentes del Contexto

El contexto puede estar compuesto por:

- Consulta del usuario.
- Fragmentos recuperados.
- Historial conversacional.
- Metadatos relevantes.
- Instrucciones del sistema.
- Configuración del agente.

Cada componente aporta información específica para la generación de la respuesta.

---

# 6. Construcción del Contexto

El proceso de construcción del contexto comprende las siguientes etapas:

1. Recepción de la consulta.
2. Validación de identidad.
3. Recuperación documental.
4. Re-ranking.
5. Eliminación de redundancias.
6. Aplicación de filtros.
7. Organización del contenido.
8. Envío al LLM.

Este proceso es completamente transparente para el usuario.

---

# 7. Selección de Fragmentos

No todos los fragmentos recuperados son enviados al modelo.

La plataforma selecciona únicamente aquellos que:

- Responden directamente a la consulta.
- Poseen alta relevancia.
- Cumplen las políticas de seguridad.
- Aportan información complementaria.
- Se ajustan a la capacidad disponible del modelo.

---

# 8. Organización del Contexto

Una vez seleccionados los fragmentos, el sistema organiza la información siguiendo criterios como:

- Relevancia.
- Coherencia temática.
- Orden lógico.
- Prioridad documental.
- Eliminación de duplicados.

Esta organización mejora la comprensión por parte del modelo.

---

# 9. Ventana de Contexto

Cada Modelo de Lenguaje dispone de una capacidad máxima para procesar información.

La Gestión del Contexto controla:

- Cantidad máxima de fragmentos.
- Longitud del contenido.
- Número de tokens.
- Distribución del contexto.

El objetivo consiste en aprovechar al máximo la capacidad disponible sin degradar el rendimiento.

---

# 10. Gestión del Historial

Cuando existe una conversación previa, el sistema puede incorporar parte del historial.

La inclusión del historial depende de:

- Relevancia.
- Continuidad de la conversación.
- Capacidad disponible.
- Configuración del agente.

El historial nunca reemplaza al contexto documental.

---

# 11. Optimización de Tokens

La plataforma procura reducir el consumo innecesario de tokens mediante:

- Eliminación de duplicados.
- Fragmentos compactos.
- Contexto altamente relevante.
- Priorización documental.
- Exclusión de información irrelevante.

Estas prácticas reducen costes y mejoran los tiempos de respuesta.

---

# 12. Priorización del Conocimiento

Cuando existen múltiples documentos relacionados con una consulta, la plataforma puede priorizar información según criterios como:

- Vigencia del documento.
- Nivel de aprobación.
- Tipo documental.
- Calidad del contenido.
- Relevancia para la consulta.

Esta priorización mejora la confiabilidad de las respuestas.

---

# 13. Seguridad

Antes de construir el contexto se verifican:

- Organización.
- Workspace.
- Usuario autenticado.
- Roles.
- Permisos.
- Estado del documento.

Ningún fragmento no autorizado podrá incorporarse al contexto.

---

# 14. Escalabilidad

La arquitectura permite adaptar dinámicamente la construcción del contexto para:

- Distintos modelos LLM.
- Diferentes ventanas de contexto.
- Organizaciones con grandes volúmenes documentales.
- Nuevos algoritmos de recuperación.
- Estrategias híbridas de búsqueda.

Esta flexibilidad facilita la evolución tecnológica de la plataforma.

---

# 15. Limitaciones

La Gestión del Contexto depende de:

- La calidad de la documentación.
- La precisión de la búsqueda semántica.
- La correcta segmentación de documentos.
- La capacidad del modelo utilizado.

Un contexto insuficiente puede afectar la calidad de la respuesta generada.

---

# 16. Buenas Prácticas

Se recomienda:

- Mantener documentos actualizados.
- Evitar duplicidad de contenido.
- Utilizar una segmentación adecuada.
- Optimizar los criterios de recuperación.
- Revisar periódicamente la calidad del contexto generado.

Estas prácticas incrementan la precisión del sistema.

---

# 17. Integración con Otros Componentes

La Gestión del Contexto interactúa directamente con:

- Arquitectura RAG.
- Embeddings.
- Base Vectorial.
- Retriever.
- Re-ranking.
- Prompt Engineering.
- Modelos LLM.
- Guardrails.
- Chat IA.

Constituye el puente entre la recuperación documental y la generación de respuestas.

---

# 18. Métricas

La calidad del contexto puede evaluarse mediante indicadores como:

- Relevancia promedio.
- Cobertura de la consulta.
- Consumo de tokens.
- Tiempo de construcción.
- Precisión de las respuestas.
- Nivel de satisfacción del usuario.

Estas métricas permiten optimizar continuamente el sistema.

---

# 19. Glosario

| Término | Descripción |
|----------|-------------|
| Contexto | Información enviada al LLM para responder una consulta. |
| Token | Unidad de procesamiento utilizada por el modelo de lenguaje. |
| Chunk | Fragmento de documento utilizado durante la recuperación. |
| Historial | Conversaciones previas incorporadas al contexto. |
| Re-ranking | Proceso de reorganización de los resultados recuperados. |
| Ventana de Contexto | Cantidad máxima de información que el LLM puede procesar en una interacción. |

---

# 20. Documentos Relacionados

Este documento complementa:

- Introducción a la IA.
- Arquitectura RAG.
- Modelos LLM.
- Embeddings.
- Prompt Engineering.
- Re-ranking.
- Guardrails.
- Evaluación del Sistema IA.
- Funcionamiento del Agente IA.

La presente documentación constituye la guía oficial de Gestión del Contexto de Nexa Knowledge AI y define los procesos utilizados para seleccionar, organizar y optimizar la información enviada al Modelo de Lenguaje, garantizando respuestas fundamentadas, eficientes y alineadas con la arquitectura RAG y las políticas de seguridad de la plataforma.