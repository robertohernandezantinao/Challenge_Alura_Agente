# Recuperación ante Desastres

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Uso Interno

---

# 1. Introducción

## Objetivo

Este documento establece el Plan Oficial de Recuperación ante Desastres (Disaster Recovery Plan - DRP) de Nexa Knowledge AI.

Su propósito es definir los procedimientos necesarios para restaurar la operación de la plataforma frente a incidentes graves que comprometan la disponibilidad, integridad o continuidad del servicio.

Este plan complementa las políticas de Infraestructura, Backups y Seguridad.

---

# 2. Alcance

El plan aplica a todos los componentes críticos de la plataforma:

- Infraestructura Cloud.
- API Gateway.
- Microservicios.
- Base de Datos Relacional.
- Base Vectorial.
- Almacenamiento de documentos.
- Servicios de IA.
- Sistemas de autenticación.
- Sistemas de monitoreo.
- Redes.
- Configuración global.

---

# 3. Objetivos

El plan busca:

- Reducir el tiempo de inactividad.
- Minimizar la pérdida de información.
- Recuperar los servicios críticos.
- Garantizar la continuidad operativa.
- Mantener la confianza de los clientes.
- Reducir el impacto económico y operativo.

---

# 4. Definiciones

## Desastre

Evento que provoca una interrupción significativa de la plataforma y que requiere procedimientos extraordinarios para restablecer la operación.

---

## Incidente

Evento que afecta parcial o totalmente uno o varios servicios.

No todos los incidentes constituyen un desastre.

---

## Recuperación

Proceso mediante el cual los servicios vuelven a un estado operativo aceptable.

---

# 5. Clasificación de Incidentes

## Nivel 1 — Bajo

Ejemplos:

- Fallo de un servicio no crítico.
- Error de configuración menor.
- Interrupciones de corta duración.

Impacto limitado.

---

## Nivel 2 — Medio

Ejemplos:

- Caída parcial de un microservicio.
- Problemas de autenticación.
- Errores de indexación.

Puede afectar a un grupo de usuarios.

---

## Nivel 3 — Alto

Ejemplos:

- Caída de varios servicios.
- Fallo de la base de datos.
- Pérdida temporal de conectividad.
- Errores masivos de procesamiento.

Impacto elevado sobre la operación.

---

## Nivel 4 — Crítico

Ejemplos:

- Caída completa de producción.
- Corrupción de datos.
- Ataque de ransomware.
- Pérdida total del centro de datos.
- Compromiso grave de seguridad.

Requiere activar inmediatamente este plan.

---

# 6. Análisis de Impacto al Negocio (BIA)

Los componentes se clasifican según su criticidad.

| Componente | Criticidad |
|------------|------------|
| API Gateway | Crítica |
| Autenticación | Crítica |
| Base de Datos | Crítica |
| Base Vectorial | Alta |
| Documentos | Alta |
| Servicio IA | Alta |
| Auditoría | Media |
| Monitoreo | Alta |
| Notificaciones | Baja |

---

# 7. Objetivos de Recuperación

## Recovery Time Objective (RTO)

Tiempo máximo permitido para restablecer un servicio.

## Recovery Point Objective (RPO)

Cantidad máxima aceptable de información que podría perderse.

Los valores específicos deberán definirse según el SLA de cada cliente y el entorno de despliegue.

---

# 8. Equipo de Respuesta

## Director del Incidente

Responsable de coordinar toda la recuperación.

---

## Equipo DevOps

Responsable de:

- Infraestructura.
- Redes.
- Despliegues.
- Recuperación técnica.

---

## Equipo de Ingeniería

Responsable de:

- Validación funcional.
- Corrección de errores.
- Restauración de servicios.

---

## Equipo de Seguridad

Responsable de:

- Investigación.
- Contención.
- Evidencias.
- Validación posterior.

---

## Soporte

Responsable de:

- Comunicación con clientes.
- Seguimiento de incidencias.
- Confirmación de recuperación.

---

# 9. Activación del Plan

El plan deberá activarse cuando ocurra alguno de los siguientes escenarios:

- Pérdida total de producción.
- Corrupción de bases de datos.
- Ataque informático grave.
- Indisponibilidad prolongada.
- Pérdida de infraestructura.
- Fallo masivo de servicios críticos.

La activación deberá ser autorizada por el responsable designado.

---

# 10. Procedimiento General

1. Detectar el incidente.
2. Clasificar la gravedad.
3. Activar el DRP.
4. Contener el impacto.
5. Analizar la causa.
6. Restaurar los servicios.
7. Validar el funcionamiento.
8. Comunicar la recuperación.
9. Documentar el incidente.

---

# 11. Recuperación por Componente

## API Gateway

Procedimiento:

- Restaurar configuración.
- Verificar certificados.
- Validar reglas de enrutamiento.
- Confirmar disponibilidad.

---

## Base de Datos

Procedimiento:

- Restaurar el último backup válido.
- Aplicar registros de transacciones si están disponibles.
- Verificar consistencia.
- Validar integridad.

---

## Base Vectorial

Procedimiento:

- Restaurar respaldo.
- Validar índices.
- Regenerar embeddings cuando sea necesario.
- Sincronizar metadatos.

---

## Documentos

Procedimiento:

- Restaurar almacenamiento.
- Validar versiones.
- Confirmar permisos.
- Ejecutar verificaciones de integridad.

---

## Servicio IA

Procedimiento:

- Restaurar configuración.
- Validar conectividad con el proveedor LLM.
- Verificar la arquitectura RAG.
- Ejecutar pruebas funcionales.

---

# 12. Recuperación de Infraestructura

En caso de pérdida completa de infraestructura:

1. Aprovisionar nuevos recursos mediante Infrastructure as Code.
2. Restaurar configuraciones.
3. Restaurar bases de datos.
4. Restaurar almacenamiento documental.
5. Desplegar microservicios.
6. Validar integraciones.
7. Ejecutar pruebas.

---

# 13. Failover

Cuando exista infraestructura redundante se recomienda:

- Cambio automático.
- Balanceadores redundantes.
- Bases de datos replicadas.
- Replicación de almacenamiento.
- Replicación geográfica cuando sea posible.

El objetivo es minimizar la interrupción del servicio.

---

# 14. Comunicación Durante el Incidente

Durante un incidente deberán mantenerse canales oficiales de comunicación.

La información comunicada incluirá:

- Estado actual.
- Servicios afectados.
- Acciones en curso.
- Tiempo estimado de recuperación.
- Confirmación de restablecimiento.

Toda comunicación deberá ser clara, precisa y verificable.

---

# 15. Validación Posterior

Antes de declarar finalizado el incidente deberán verificarse:

- Disponibilidad de los servicios.
- Integridad de los datos.
- Correcta autenticación.
- Funcionamiento de los Agentes IA.
- Acceso a documentos.
- Recuperación de auditoría.
- Integraciones externas.

---

# 16. Informe Post Incidente

Todo desastre deberá generar un informe que incluya:

- Fecha.
- Hora.
- Causa.
- Impacto.
- Componentes afectados.
- Tiempo de recuperación.
- Medidas adoptadas.
- Lecciones aprendidas.
- Acciones preventivas.

---

# 17. Simulacros

Se recomienda realizar simulacros periódicos para validar la eficacia del plan.

Los ejercicios deberán contemplar escenarios como:

- Caída total del entorno de producción.
- Restauración de bases de datos.
- Recuperación documental.
- Recuperación de la Base Vectorial.
- Pérdida de un microservicio crítico.
- Fallo del proveedor de IA.

Cada simulacro deberá documentarse y utilizarse para mejorar el plan.

---

# 18. Mejora Continua

El Plan de Recuperación deberá revisarse:

- Después de cada incidente grave.
- Tras cambios significativos de arquitectura.
- Al incorporar nuevos servicios críticos.
- Como mínimo una vez al año.

Las lecciones aprendidas deberán traducirse en mejoras del procedimiento.

---

# 19. Buenas Prácticas

Se recomienda:

- Mantener respaldos actualizados.
- Automatizar la recuperación cuando sea posible.
- Probar regularmente los procedimientos.
- Evitar dependencias de un único proveedor.
- Mantener documentación actualizada.
- Supervisar continuamente la infraestructura.
- Capacitar periódicamente al personal.

---

# 20. Documentos Relacionados

Este documento complementa:

- Infraestructura.
- Backups.
- Política de Seguridad.
- Configuración Global.
- Arquitectura Técnica.
- Arquitectura de Microservicios.
- Manual del Administrador.
- Cumplimiento Normativo.

El Plan de Recuperación ante Desastres constituye el procedimiento oficial para restaurar la operación de Nexa Knowledge AI frente a eventos críticos, garantizando la continuidad del negocio, la protección de la información y la recuperación controlada de todos los servicios esenciales de la plataforma.