# Reglas de Negocio

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión:** 1.0

---

# 1. Introducción

## 1.1 Objetivo

Este documento define las reglas de negocio que gobiernan el comportamiento funcional de Nexa Knowledge AI.

Las reglas aquí descritas son obligatorias para todos los módulos de la plataforma y deben respetarse independientemente de la tecnología utilizada para su implementación.

Estas reglas garantizan la consistencia de los datos, la seguridad de la información y el correcto funcionamiento del producto.

---

# 2. Convenciones

Cada regla posee un identificador único.

Formato:

RN-XXX

Ejemplo:

RN-001

Las reglas pueden ser utilizadas como referencia en:

- Desarrollo
- QA
- Casos de uso
- APIs
- Manuales
- Soporte
- Auditorías
- Agentes IA

---

# 3. Organizaciones

## RN-001

Toda organización debe poseer un identificador único.

---

## RN-002

El nombre de una organización puede repetirse únicamente si pertenece a clientes diferentes y no genera conflictos operativos.

---

## RN-003

Una organización debe tener al menos un usuario con rol Administrador.

---

## RN-004

Una organización suspendida no podrá iniciar nuevas sesiones.

Los usuarios existentes perderán acceso hasta que la organización sea reactivada.

---

## RN-005

La eliminación de una organización deberá respetar la política de retención de datos definida por NexaDigital S.A.S.

---

# 4. Usuarios

## RN-006

Todo usuario debe pertenecer al menos a una organización.

---

## RN-007

El correo electrónico de un usuario debe ser único dentro de una misma organización.

---

## RN-008

Un usuario puede pertenecer a múltiples organizaciones.

Cada organización mantiene sus propios permisos y configuraciones.

---

## RN-009

Un usuario desactivado no podrá autenticarse.

---

## RN-010

Un usuario eliminado no podrá recuperarse una vez finalizado el período de retención definido por la organización.

---

# 5. Roles y Permisos

## RN-011

Todo usuario debe tener al menos un rol asignado.

---

## RN-012

Los permisos siempre serán evaluados antes de ejecutar cualquier operación.

---

## RN-013

La ausencia de un permiso implica denegación automática del acceso.

---

## RN-014

Los permisos heredados no podrán modificar permisos explícitamente denegados.

---

## RN-015

Los cambios de permisos deberán registrarse en la auditoría.

---

# 6. Workspaces

## RN-016

Todo Workspace pertenece exactamente a una organización.

---

## RN-017

Un Workspace no puede pertenecer simultáneamente a dos organizaciones.

---

## RN-018

Todo documento debe pertenecer a un Workspace.

---

## RN-019

La eliminación de un Workspace requerirá confirmar el tratamiento de los documentos asociados.

---

# 7. Colecciones

## RN-020

Toda colección pertenece a un único Workspace.

---

## RN-021

Un documento puede pertenecer únicamente a una colección principal.

---

## RN-022

Una colección vacía podrá mantenerse para futuras cargas.

---

# 8. Documentos

## RN-023

Solo podrán cargarse formatos oficialmente soportados.

---

## RN-024

Todo documento cargado iniciará automáticamente el proceso de indexación, salvo que la organización haya configurado un procesamiento manual.

---

## RN-025

Un documento con errores de procesamiento no podrá utilizarse para responder consultas.

---

## RN-026

Toda actualización de un documento generará una nueva versión.

---

## RN-027

La eliminación lógica de un documento no eliminará inmediatamente su historial.

---

## RN-028

Los metadatos deberán mantenerse sincronizados con la versión vigente del documento.

---

# 9. Procesamiento Inteligente

## RN-029

Todo documento deberá completar correctamente el proceso de extracción antes de generar embeddings.

---

## RN-030

Los fragmentos deberán conservar una referencia al documento de origen.

---

## RN-031

Cada fragmento deberá poseer exactamente un embedding activo.

---

## RN-032

Si un documento cambia de versión, los embeddings anteriores deberán invalidarse antes de generar los nuevos.

---

## RN-033

El sistema no podrá indexar documentos corruptos.

---

# 10. Base de Conocimiento

## RN-034

La Base de Conocimiento solo contendrá documentos procesados correctamente.

---

## RN-035

Todo contenido indexado deberá mantener su trazabilidad hacia el documento original.

---

## RN-036

Las respuestas generadas deberán poder identificar las fuentes utilizadas.

---

# 11. Agentes IA

## RN-037

Todo Agente IA deberá operar únicamente sobre la información autorizada.

---

## RN-038

Un Agente IA no podrá acceder a documentos para los cuales el usuario no posee permisos.

---

## RN-039

Cada Agente IA deberá tener un modelo de lenguaje configurado.

---

## RN-040

Los parámetros de generación deberán permanecer dentro de los límites definidos por la organización.

---

## RN-041

Las instrucciones del Agente IA deberán almacenarse versionadas.

---

# 12. Consultas

## RN-042

Toda consulta deberá quedar asociada a una conversación.

---

## RN-043

Toda respuesta deberá indicar las fuentes cuando la configuración del asistente así lo permita.

---

## RN-044

Las consultas podrán limitarse por Workspace, Colección o Documento.

---

## RN-045

El sistema podrá rechazar consultas que incumplan las políticas de uso de la plataforma.

---

# 13. Conversaciones

## RN-046

Cada conversación pertenece a un único usuario.

---

## RN-047

Una conversación podrá contener múltiples consultas.

---

## RN-048

Las conversaciones archivadas permanecerán disponibles en modo lectura.

---

## RN-049

La eliminación de una conversación deberá respetar las políticas de auditoría y retención de datos.

---

# 14. Auditoría

## RN-050

Toda acción administrativa deberá registrarse.

---

## RN-051

Toda modificación de permisos deberá registrarse.

---

## RN-052

Toda carga de documentos deberá registrarse.

---

## RN-053

Toda eliminación lógica deberá registrarse.

---

## RN-054

Las consultas realizadas por los Agentes IA podrán registrarse según la configuración de la organización.

---

# 15. Seguridad

## RN-055

Todo acceso deberá autenticarse antes de acceder a cualquier recurso protegido.

---

## RN-056

Toda comunicación deberá realizarse mediante conexiones cifradas.

---

## RN-057

Las credenciales nunca deberán almacenarse en texto plano.

---

## RN-058

Las sesiones expiradas deberán invalidarse automáticamente.

---

## RN-059

Los intentos reiterados de autenticación fallida podrán provocar el bloqueo temporal de la cuenta.

---

# 16. Facturación

## RN-060

Los límites del plan contratado deberán aplicarse antes de permitir nuevas operaciones.

---

## RN-061

Una organización con suscripción vencida podrá ver restringidas determinadas funcionalidades según su plan.

---

## RN-062

Toda modificación del plan deberá registrarse en el historial de suscripciones.

---

# 17. Integraciones

## RN-063

Toda integración deberá autenticarse mediante un mecanismo autorizado.

---

## RN-064

Las integraciones externas deberán respetar los permisos de la organización.

---

## RN-065

La revocación de una integración deberá impedir inmediatamente nuevos accesos.

---

# 18. Reglas Generales

## RN-066

Todas las operaciones deberán respetar el modelo de permisos vigente.

---

## RN-067

Toda información utilizada por un Agente IA deberá provenir de la Base de Conocimiento o de herramientas explícitamente autorizadas.

---

## RN-068

Las respuestas generadas por IA nunca deberán omitir las restricciones de seguridad definidas por la organización.

---

## RN-069

Toda operación crítica deberá generar un evento de auditoría.

---

## RN-070

Toda nueva funcionalidad incorporada al producto deberá definir sus propias reglas de negocio antes de pasar a producción.

---

# 19. Relación con otros documentos

Este documento complementa:

- Base de Conocimiento del Producto.
- Arquitectura Funcional.
- Modelo de Dominio.
- Catálogo de Funcionalidades.
- Casos de Uso.

Las reglas aquí definidas prevalecen sobre cualquier comportamiento no especificado en otros documentos y constituyen la referencia oficial para el funcionamiento del producto.