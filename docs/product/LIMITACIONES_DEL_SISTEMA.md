# Limitaciones del Sistema

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

---

# 1. Introducción

## Objetivo

Este documento describe las limitaciones funcionales, técnicas, operativas y de seguridad de Nexa Knowledge AI.

Su finalidad es establecer claramente los límites del producto para evitar interpretaciones incorrectas sobre sus capacidades y proporcionar una referencia oficial para usuarios, administradores, desarrolladores, soporte técnico y Agentes IA.

---

# 2. Alcance

Las limitaciones descritas en este documento aplican a toda la plataforma, independientemente del plan contratado, salvo que se indique expresamente lo contrario.

Estas limitaciones podrán modificarse en futuras versiones del producto.

---

# 3. Limitaciones Generales

## LS-001

Nexa Knowledge AI únicamente puede responder utilizando información disponible en la Base de Conocimiento o mediante herramientas explícitamente autorizadas.

---

## LS-002

La plataforma no genera conocimiento corporativo inexistente.

Si una respuesta no puede fundamentarse con información disponible, el Agente IA deberá indicarlo explícitamente.

---

## LS-003

La calidad de las respuestas depende directamente de la calidad, actualidad y completitud de los documentos proporcionados por la organización.

---

## LS-004

La plataforma no reemplaza la validación humana en procesos críticos del negocio.

---

## LS-005

Las respuestas generadas constituyen apoyo para la toma de decisiones y no sustituyen las políticas internas de la organización.

---

# 4. Limitaciones Documentales

## LS-006

Solo podrán procesarse formatos oficialmente soportados por la plataforma.

---

## LS-007

Documentos protegidos mediante contraseñas no podrán indexarse hasta que sean desbloqueados.

---

## LS-008

Documentos corruptos o incompletos podrán ser rechazados durante el procesamiento.

---

## LS-009

Imágenes sin texto legible no podrán incorporarse a la Base de Conocimiento sin un proceso OCR compatible.

---

## LS-010

La plataforma no modifica el contenido original de los documentos cargados.

---

# 5. Limitaciones de Inteligencia Artificial

## LS-011

Los Agentes IA pueden interpretar incorrectamente consultas ambiguas.

Se recomienda formular preguntas claras y específicas.

---

## LS-012

Las respuestas pueden variar entre consultas similares debido al comportamiento probabilístico de los modelos de lenguaje.

---

## LS-013

El Agente IA no garantiza respuestas correctas cuando la información disponible sea contradictoria.

---

## LS-014

La plataforma no infiere políticas internas que no estén documentadas.

---

## LS-015

Los Agentes IA no accederán a documentos sin autorización, aunque el usuario los mencione explícitamente.

---

## LS-016

El sistema puede abstenerse de responder cuando no exista evidencia suficiente para construir una respuesta confiable.

---

# 6. Limitaciones de Seguridad

## LS-017

Los usuarios únicamente podrán acceder a la información autorizada por el modelo de permisos vigente.

---

## LS-018

Los Agentes IA respetarán exactamente las restricciones de acceso configuradas para cada usuario.

---

## LS-019

Las consultas podrán ser registradas para fines de auditoría y mejora del servicio, según la configuración de la organización.

---

## LS-020

La plataforma podrá bloquear temporalmente operaciones que representen riesgos para la seguridad.

---

# 7. Limitaciones Operativas

## LS-021

El procesamiento de documentos puede requerir un tiempo variable según:

- Tamaño del archivo.
- Cantidad de páginas.
- Complejidad del contenido.
- Carga del sistema.

---

## LS-022

Los documentos recién cargados no estarán disponibles para consultas hasta finalizar correctamente el proceso de indexación.

---

## LS-023

Las respuestas podrán demorarse durante tareas de mantenimiento o alta demanda.

---

## LS-024

La disponibilidad de determinadas funciones dependerá del plan contratado por la organización.

---

# 8. Limitaciones de Integraciones

## LS-025

Las integraciones externas dependerán de la disponibilidad de los servicios de terceros.

---

## LS-026

NexaDigital S.A.S. no controla los cambios realizados por proveedores externos sobre sus APIs.

---

## LS-027

Una integración revocada dejará de suministrar información inmediatamente.

---

## LS-028

Las credenciales de integración deberán mantenerse vigentes para garantizar el acceso continuo a los recursos externos.

---

# 9. Limitaciones del Modelo de Lenguaje

## LS-029

La precisión de las respuestas dependerá del modelo de lenguaje configurado.

---

## LS-030

Diferentes modelos podrán generar respuestas distintas utilizando el mismo contexto.

---

## LS-031

Las capacidades disponibles podrán variar según el proveedor del modelo de lenguaje.

---

# 10. Limitaciones de Rendimiento

## LS-032

Consultas sobre grandes volúmenes de información podrán requerir mayor tiempo de procesamiento.

---

## LS-033

La indexación masiva de documentos podrá ejecutarse mediante procesos en segundo plano.

---

## LS-034

El rendimiento general dependerá de la infraestructura contratada y de los recursos disponibles.

---

# 11. Limitaciones de Auditoría

## LS-035

La retención de registros de auditoría dependerá de las políticas configuradas por la organización y de la normativa aplicable.

---

## LS-036

Los registros eliminados conforme a las políticas de retención no podrán recuperarse.

---

# 12. Limitaciones Comerciales

## LS-037

Determinadas funcionalidades podrán estar disponibles únicamente en planes específicos.

---

## LS-038

Los límites de almacenamiento, usuarios y consultas dependerán del plan contratado.

---

## LS-039

La superación de los límites contratados podrá impedir temporalmente nuevas operaciones hasta ampliar el plan o liberar recursos.

---

# 13. Buenas Prácticas

Para obtener los mejores resultados se recomienda:

- Mantener la documentación actualizada.
- Organizar correctamente las colecciones.
- Utilizar nombres descriptivos para documentos.
- Configurar adecuadamente los permisos.
- Revisar periódicamente la Base de Conocimiento.
- Formular consultas claras y específicas.
- Verificar las fuentes utilizadas por el Agente IA.
- Revisar la auditoría de forma periódica.

---

# 14. Preguntas Frecuentes

## ¿El Agente IA puede responder sobre documentos eliminados?

No.

Solo responderá utilizando documentos disponibles y autorizados en la Base de Conocimiento.

---

## ¿Puede responder si un documento aún está procesándose?

No.

El documento deberá finalizar correctamente el proceso de indexación.

---

## ¿Puede responder utilizando información de Internet?

No de forma predeterminada.

Solo podrá hacerlo si la organización ha habilitado herramientas o integraciones externas autorizadas.

---

## ¿Puede acceder a documentos de otra organización?

No.

La plataforma implementa aislamiento completo entre organizaciones.

---

## ¿Puede inventar información faltante?

No.

Cuando no exista evidencia suficiente, el Agente IA deberá indicarlo explícitamente o solicitar mayor contexto.

---

# 15. Relación con otros documentos

Este documento complementa:

- Base de Conocimiento del Producto.
- Arquitectura Funcional.
- Modelo de Dominio.
- Catálogo de Funcionalidades.
- Casos de Uso.
- Reglas de Negocio.
- Modelo de Permisos.
- Glosario del Producto.
- Roadmap del Producto.

Las limitaciones aquí descritas establecen el alcance operativo del producto y deberán considerarse durante el diseño, implementación, uso y soporte de la plataforma.