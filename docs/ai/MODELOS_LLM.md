# Modelos LLM

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Público

---

# 1. Introducción

## Objetivo

El presente documento describe el papel de los **Large Language Models (LLM)** dentro de la arquitectura de Nexa Knowledge AI.

Su propósito es definir cómo los modelos de lenguaje participan en la comprensión de consultas, el razonamiento sobre el contexto recuperado y la generación de respuestas fundamentadas en la documentación empresarial.

---

# 2. Alcance

Este documento aplica a:

- Arquitectos de Software.
- Ingenieros de Inteligencia Artificial.
- Desarrolladores Backend.
- Equipos de Integración.
- Administradores de la plataforma.
- Consultores técnicos.

No describe un proveedor específico de modelos de IA, sino la arquitectura general adoptada por la plataforma.

---

# 3. ¿Qué es un LLM?

Un **Large Language Model (LLM)** es un modelo de Inteligencia Artificial entrenado para comprender y generar lenguaje natural.

En Nexa Knowledge AI, el LLM constituye el componente responsable de transformar una consulta y un contexto documental en una respuesta clara, coherente y útil para el usuario.

El modelo no accede directamente a la documentación empresarial; recibe únicamente el contexto previamente seleccionado por la arquitectura RAG.

---

# 4. Responsabilidades del LLM

Dentro de la plataforma, el LLM tiene las siguientes responsabilidades:

- Comprender la intención del usuario.
- Interpretar el contexto proporcionado.
- Relacionar la información recuperada.
- Elaborar respuestas en lenguaje natural.
- Mantener coherencia durante la conversación.
- Adaptar el lenguaje al contexto empresarial.
- Respetar las instrucciones definidas por el sistema.

El modelo no reemplaza los mecanismos de recuperación documental ni la validación de permisos.

---

# 5. Posición dentro de la Arquitectura

El LLM forma parte de la etapa final del flujo RAG.

Flujo simplificado:

1. Usuario envía una consulta.
2. Se validan permisos.
3. El Retriever recupera información relevante.
4. El Re-ranking reorganiza los resultados.
5. Se construye el contexto.
6. El LLM recibe la consulta junto con el contexto.
7. Se genera la respuesta.
8. El usuario recibe el resultado.

---

# 6. Información que Recibe el Modelo

El modelo recibe únicamente la información necesaria para responder la consulta.

Normalmente incluye:

- Consulta del usuario.
- Contexto documental recuperado.
- Instrucciones del sistema.
- Configuración del agente.
- Idioma de respuesta.
- Restricciones de seguridad.

No recibe la totalidad de la base documental de la organización.

---

# 7. Información que No Debe Recibir

Por razones de seguridad y eficiencia, el LLM no debe recibir:

- Documentos sin autorización.
- Información perteneciente a otros Workspaces.
- Datos protegidos por restricciones de acceso.
- Información irrelevante para la consulta.
- Fragmentos duplicados.
- Contexto innecesario que reduzca la calidad de la respuesta.

---

# 8. Integración con la Arquitectura RAG

El LLM depende completamente del proceso de recuperación implementado por la arquitectura RAG.

Esto implica que:

- No realiza búsquedas directamente.
- No consulta la base vectorial.
- No decide qué documentos recuperar.
- Utiliza exclusivamente el contexto preparado por el sistema.

La calidad de las respuestas depende directamente de la calidad del contexto recibido.

---

# 9. Generación de Respuestas

Una vez recibido el contexto, el modelo:

1. Analiza la consulta.
2. Comprende la información recuperada.
3. Relaciona los conceptos relevantes.
4. Genera una respuesta coherente.
5. Devuelve el resultado a la plataforma.

El proceso se ejecuta de manera transparente para el usuario.

---

# 10. Ventana de Contexto

Todo LLM posee una capacidad máxima para procesar información simultáneamente.

Esta capacidad se conoce como **ventana de contexto**.

La plataforma optimiza el contenido enviado al modelo para:

- Maximizar la relevancia.
- Reducir información redundante.
- Mantener tiempos de respuesta adecuados.
- Mejorar la precisión.

La gestión del contexto se documenta en **Gestión del Contexto.md**.

---

# 11. Selección del Modelo

La arquitectura de Nexa Knowledge AI permite utilizar distintos proveedores o versiones de modelos de lenguaje.

La selección puede considerar criterios como:

- Calidad de las respuestas.
- Tiempo de respuesta.
- Coste operativo.
- Idiomas soportados.
- Capacidad de contexto.
- Disponibilidad.
- Compatibilidad con la infraestructura.

La plataforma está diseñada para minimizar la dependencia de un proveedor específico.

---

# 12. Seguridad

El uso del LLM debe respetar las políticas de seguridad de la organización.

En particular:

- El modelo solo recibe información autorizada.
- No puede omitir controles de acceso.
- No accede directamente a la base documental.
- Opera bajo las restricciones definidas por la plataforma.
- Su actividad puede registrarse para fines de auditoría.

---

# 13. Limitaciones

Los LLM presentan limitaciones inherentes que deben considerarse.

Entre ellas:

- Pueden interpretar incorrectamente consultas ambiguas.
- Dependen del contexto recibido.
- No verifican automáticamente la veracidad de la información proporcionada.
- No sustituyen documentación oficial.
- No conocen documentos que no hayan sido recuperados por el sistema.

Por este motivo, la calidad de la respuesta depende tanto del modelo como del proceso de recuperación.

---

# 14. Buenas Prácticas

Para obtener el mejor rendimiento del LLM se recomienda:

- Utilizar un contexto limpio y relevante.
- Evitar información duplicada.
- Mantener la documentación actualizada.
- Aplicar técnicas de Prompt Engineering.
- Implementar mecanismos de Re-ranking.
- Definir instrucciones claras para el modelo.

---

# 15. Casos de Uso

Los LLM pueden utilizarse para:

- Responder preguntas sobre documentación.
- Explicar procedimientos internos.
- Resumir documentos.
- Comparar políticas.
- Guiar a nuevos colaboradores.
- Localizar información empresarial.
- Asistir en procesos de soporte.

Estos casos de uso siempre estarán condicionados por la documentación disponible y los permisos del usuario.

---

# 16. Integración con Otros Componentes

El LLM trabaja conjuntamente con:

- Arquitectura RAG.
- Embeddings.
- Base Vectorial.
- Retriever.
- Re-ranking.
- Guardrails.
- Gestión del Contexto.
- Chat IA.
- Gestión de Documentos.

Cada componente aporta información necesaria para producir respuestas confiables.

---

# 17. Consideraciones de Escalabilidad

La plataforma permite evolucionar el uso de LLM mediante:

- Actualización de versiones del modelo.
- Incorporación de nuevos proveedores.
- Balanceo de carga entre modelos.
- Optimización del consumo de tokens.
- Ajuste dinámico del contexto.
- Configuración por organización o Workspace.

Esta flexibilidad facilita la evolución tecnológica sin modificar la arquitectura funcional del producto.

---

# 18. Glosario

| Término | Descripción |
|----------|-------------|
| LLM | Large Language Model utilizado para comprender y generar lenguaje natural. |
| Token | Unidad mínima de procesamiento utilizada por un modelo de lenguaje. |
| Contexto | Información enviada al modelo para generar una respuesta. |
| Prompt | Conjunto de instrucciones entregadas al LLM. |
| Inferencia | Proceso mediante el cual el modelo genera una respuesta. |
| Ventana de Contexto | Cantidad máxima de información que el modelo puede procesar en una única interacción. |

---

# 19. Documentos Relacionados

Este documento complementa:

- Introducción a la IA.
- Arquitectura RAG.
- Funcionamiento del Agente IA.
- Embeddings.
- Prompt Engineering.
- Re-ranking.
- Guardrails.
- Gestión del Contexto.
- Evaluación del Sistema IA.

La presente documentación constituye la guía oficial sobre el uso de Modelos de Lenguaje (LLM) en Nexa Knowledge AI y define su papel dentro de la arquitectura RAG, las responsabilidades que asumen durante la generación de respuestas, las limitaciones inherentes a este tipo de modelos y las buenas prácticas para su integración segura, eficiente y escalable en la plataforma.