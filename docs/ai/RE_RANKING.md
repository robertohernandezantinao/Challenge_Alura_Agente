# Re-ranking

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Interno

---

# 1. Introducción

## Objetivo

El presente documento define el funcionamiento del proceso de **Re-ranking** dentro de la arquitectura RAG de Nexa Knowledge AI.

Su objetivo es describir cómo la plataforma reorganiza los resultados obtenidos durante la búsqueda semántica para seleccionar el contexto más relevante que será enviado al Modelo de Lenguaje (LLM).

---

# 2. Alcance

Este documento aplica a:

- Arquitectos de Software.
- Ingenieros de Inteligencia Artificial.
- Desarrolladores Backend.
- Administradores de la plataforma.
- Equipos responsables del motor de búsqueda.

---

# 3. ¿Qué es el Re-ranking?

El **Re-ranking** es el proceso mediante el cual los documentos o fragmentos recuperados inicialmente por el Retriever son evaluados nuevamente para determinar cuáles representan mejor la intención del usuario.

Este proceso mejora significativamente la precisión de las respuestas generadas por el sistema.

---

# 4. Objetivos

El proceso de Re-ranking busca:

- Incrementar la relevancia del contexto.
- Reducir información poco útil.
- Eliminar resultados redundantes.
- Priorizar fragmentos más precisos.
- Optimizar el uso de la ventana de contexto del LLM.
- Mejorar la calidad de las respuestas.

---

# 5. Posición dentro de la Arquitectura

El Re-ranking se ubica entre el proceso de recuperación documental y la construcción del contexto.

Flujo simplificado:

1. Consulta del usuario.
2. Generación del embedding.
3. Recuperación inicial (Retriever).
4. Re-ranking.
5. Construcción del contexto.
6. Envío al LLM.
7. Generación de la respuesta.

---

# 6. Entrada del Proceso

El Re-ranking recibe:

- Consulta original del usuario.
- Lista inicial de fragmentos recuperados.
- Puntajes de similitud.
- Metadatos asociados.
- Configuración de recuperación.

Esta información constituye la base para una nueva evaluación de relevancia.

---

# 7. Criterios de Relevancia

El sistema puede considerar diversos factores para ordenar los resultados:

- Similitud semántica.
- Coincidencia con la intención de la consulta.
- Calidad del contenido.
- Actualidad del documento.
- Prioridad documental.
- Nivel de confianza.
- Eliminación de duplicados.

Los criterios pueden evolucionar conforme se optimiza la plataforma.

---

# 8. Eliminación de Redundancia

Es frecuente que distintos fragmentos contengan información similar.

El proceso de Re-ranking identifica estas situaciones para:

- Reducir duplicidad.
- Aprovechar mejor la ventana de contexto.
- Incrementar la diversidad de información enviada al LLM.

---

# 9. Selección del Contexto

Una vez reorganizados los resultados, el sistema selecciona únicamente los fragmentos más relevantes.

Esta selección debe:

- Mantener coherencia temática.
- Cubrir la intención de la consulta.
- Respetar los límites de contexto del modelo.
- Evitar información innecesaria.

---

# 10. Beneficios

La incorporación de Re-ranking proporciona:

- Mayor precisión.
- Menor cantidad de respuestas incorrectas.
- Mejor aprovechamiento del contexto.
- Reducción de ruido documental.
- Incremento de la calidad percibida por el usuario.

---

# 11. Integración con la Arquitectura RAG

El Re-ranking trabaja conjuntamente con:

- Embeddings.
- Base Vectorial.
- Retriever.
- Gestión del Contexto.
- Prompt Engineering.
- Modelos LLM.

Su función consiste en preparar el mejor conjunto posible de información antes de la generación de la respuesta.

---

# 12. Consideraciones de Rendimiento

El proceso debe ejecutarse con un impacto mínimo sobre el tiempo de respuesta.

Para ello la plataforma busca:

- Optimizar algoritmos.
- Reducir operaciones innecesarias.
- Balancear precisión y velocidad.
- Minimizar el consumo de recursos.

---

# 13. Seguridad

Durante el Re-ranking no pueden incorporarse documentos que no hayan superado previamente las validaciones de seguridad.

El proceso respeta:

- Organización.
- Workspace.
- Roles.
- Permisos.
- Estado documental.

La relevancia nunca prevalece sobre las restricciones de acceso.

---

# 14. Escalabilidad

La arquitectura permite incorporar distintos mecanismos de Re-ranking sin modificar el resto del sistema.

Entre ellos:

- Modelos basados en Transformers.
- Cross-Encoders.
- Algoritmos híbridos.
- Métodos estadísticos.
- Modelos especializados por dominio.

Esta flexibilidad facilita la evolución tecnológica de la plataforma.

---

# 15. Buenas Prácticas

Se recomienda:

- Mantener criterios de evaluación consistentes.
- Revisar periódicamente los algoritmos utilizados.
- Medir la calidad de las respuestas.
- Ajustar parámetros utilizando métricas objetivas.
- Evitar favorecer documentos únicamente por antigüedad o tamaño.

---

# 16. Limitaciones

El Re-ranking no puede:

- Recuperar documentos inexistentes.
- Compensar una mala indexación.
- Sustituir la búsqueda semántica.
- Corregir errores presentes en la documentación.
- Eliminar completamente la ambigüedad de una consulta.

Su función consiste únicamente en mejorar el orden de los resultados recuperados.

---

# 17. Métricas

La calidad del Re-ranking puede evaluarse mediante indicadores como:

- Precisión.
- Recall.
- NDCG (Normalized Discounted Cumulative Gain).
- MRR (Mean Reciprocal Rank).
- Tiempo de respuesta.
- Satisfacción del usuario.

Estas métricas permiten optimizar continuamente el sistema.

---

# 18. Glosario

| Término | Descripción |
|----------|-------------|
| Re-ranking | Reordenamiento de resultados recuperados para maximizar su relevancia. |
| Retriever | Componente encargado de recuperar candidatos iniciales. |
| Contexto | Conjunto de fragmentos enviados al LLM. |
| Relevancia | Grado en que un fragmento responde a la intención del usuario. |
| Cross-Encoder | Modelo utilizado para evaluar la relación entre consulta y documento con alta precisión. |
| NDCG | Métrica utilizada para evaluar la calidad del ordenamiento de resultados. |

---

# 19. Documentos Relacionados

Este documento complementa:

- Introducción a la IA.
- Arquitectura RAG.
- Modelos LLM.
- Embeddings.
- Prompt Engineering.
- Guardrails.
- Gestión del Contexto.
- Evaluación del Sistema IA.
- Funcionamiento del Agente IA.

La presente documentación constituye la guía oficial del mecanismo de Re-ranking de Nexa Knowledge AI y define cómo la plataforma reorganiza los resultados recuperados mediante búsqueda semántica para construir un contexto de alta calidad, optimizando la precisión, consistencia y confiabilidad de las respuestas generadas por el Agente IA.