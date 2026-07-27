# Backups

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Uso Interno

---

# 1. Introducción

## Objetivo

Este documento establece la política oficial de copias de seguridad (Backups) de Nexa Knowledge AI.

Su propósito es garantizar la disponibilidad, integridad y recuperación de la información crítica de la plataforma frente a fallos técnicos, errores humanos, incidentes de seguridad o desastres.

---

# 2. Alcance

Esta política aplica a todos los componentes críticos de la plataforma, incluyendo:

- Base de datos relacional.
- Base vectorial.
- Documentos almacenados.
- Configuración del sistema.
- Secretos y certificados.
- Archivos de auditoría.
- Variables de configuración.
- Infraestructura como código (IaC).

---

# 3. Objetivos

La estrategia de respaldos busca:

- Evitar pérdida de información.
- Garantizar la continuidad del negocio.
- Reducir el tiempo de recuperación.
- Cumplir requisitos legales y contractuales.
- Proteger la información crítica.

---

# 4. Principios

Toda política de respaldo deberá cumplir los siguientes principios:

- Automatización.
- Integridad.
- Disponibilidad.
- Cifrado.
- Verificación periódica.
- Trazabilidad.
- Recuperación comprobada.

---

# 5. Información Respaldada

## Base de Datos Relacional

Se respaldan:

- Usuarios.
- Organizaciones.
- Workspaces.
- Colecciones.
- Conversaciones.
- Configuración.
- Auditoría.
- Roles y permisos.

---

## Base Vectorial

Se respaldan:

- Embeddings.
- Índices vectoriales.
- Metadatos.
- Configuración de indexación.

Cuando la arquitectura lo permita, los embeddings podrán regenerarse a partir de los documentos originales, aunque se recomienda mantener respaldos para reducir tiempos de recuperación.

---

## Documentos

Se respaldan:

- Archivos originales.
- Versiones.
- Documentos archivados.
- Exportaciones.

---

## Configuración

Incluye:

- Variables de entorno.
- Configuración global.
- Parámetros de la plataforma.
- Configuración de organizaciones.

---

## Secretos

Se respaldan de forma segura:

- Certificados.
- Claves API.
- Tokens.
- Credenciales de integración.

Los secretos deberán almacenarse cifrados y con acceso restringido.

---

# 6. Tipos de Backups

## Backup Completo

Incluye toda la información del sistema.

Frecuencia recomendada:

- Semanal.

---

## Backup Incremental

Incluye únicamente los cambios desde el último respaldo.

Frecuencia recomendada:

- Diaria.

---

## Backup Diferencial

Puede utilizarse cuando la estrategia de recuperación lo requiera.

Incluye todos los cambios desde el último backup completo.

---

# 7. Frecuencia Recomendada

| Componente | Frecuencia |
|------------|------------|
| Base de datos | Diaria |
| Base vectorial | Diaria |
| Documentos | Diaria |
| Configuración | Diaria |
| Secretos | Tras cada modificación |
| Auditoría | Diaria |

La frecuencia podrá ajustarse según los acuerdos de nivel de servicio (SLA).

---

# 8. Retención

Se recomienda mantener las copias durante los siguientes periodos:

| Tipo | Tiempo |
|-------|---------|
| Diario | 30 días |
| Semanal | 12 semanas |
| Mensual | 12 meses |
| Anual | Según políticas corporativas |

La organización podrá establecer periodos de retención superiores cuando existan requisitos regulatorios.

---

# 9. Almacenamiento

Las copias de seguridad deberán almacenarse:

- En ubicaciones independientes.
- En almacenamiento redundante.
- Con acceso restringido.
- En diferentes zonas geográficas cuando sea posible.

No deberán almacenarse únicamente en el mismo servidor de producción.

---

# 10. Cifrado

Todos los respaldos deberán mantenerse cifrados.

Se aplicará cifrado:

## En tránsito

Durante la transferencia entre sistemas.

---

## En reposo

Mientras permanezcan almacenados.

Las claves de cifrado deberán gestionarse mediante un sistema seguro de administración de secretos.

---

# 11. Automatización

Todos los procesos de respaldo deberán ejecutarse automáticamente.

Las tareas incluirán:

- Generación.
- Validación.
- Compresión.
- Cifrado.
- Transferencia.
- Registro.
- Notificación de resultados.

Se evitarán procesos manuales salvo en situaciones excepcionales.

---

# 12. Verificación

Cada respaldo deberá verificarse automáticamente para comprobar:

- Integridad.
- Tamaño esperado.
- Consistencia.
- Disponibilidad.
- Finalización correcta.

Los respaldos corruptos deberán descartarse y regenerarse.

---

# 13. Restauración

La restauración podrá realizarse de forma:

## Completa

Recupera todo el entorno.

---

## Parcial

Recupera únicamente recursos específicos.

Ejemplos:

- Un documento.
- Una colección.
- Un Workspace.
- Una base de datos.
- Una conversación.

---

# 14. Procedimiento General de Restauración

1. Identificar el incidente.
2. Seleccionar el respaldo adecuado.
3. Validar su integridad.
4. Restaurar el componente afectado.
5. Verificar la consistencia.
6. Validar el funcionamiento del sistema.
7. Registrar la operación.

---

# 15. Objetivos de Recuperación

La organización deberá definir los siguientes indicadores:

## RPO (Recovery Point Objective)

Tiempo máximo aceptable de pérdida de información.

---

## RTO (Recovery Time Objective)

Tiempo máximo permitido para recuperar el servicio.

Los valores concretos dependerán del nivel de servicio contratado y de la criticidad del entorno.

---

# 16. Auditoría

Todas las operaciones de respaldo deberán registrar:

- Fecha.
- Hora.
- Responsable (si aplica).
- Tipo de backup.
- Resultado.
- Duración.
- Tamaño.
- Componentes incluidos.

---

# 17. Monitoreo

El sistema supervisará automáticamente:

- Ejecución de respaldos.
- Errores.
- Espacio disponible.
- Integridad.
- Tiempo de ejecución.
- Fallos repetitivos.

Las incidencias deberán generar alertas al equipo responsable.

---

# 18. Pruebas de Recuperación

Las copias de seguridad deberán probarse periódicamente.

Las pruebas deberán verificar:

- Restauración completa.
- Restauración parcial.
- Integridad de la información.
- Funcionamiento de la aplicación.
- Consistencia entre servicios.

No se considerará válida una estrategia de backup que no haya sido probada.

---

# 19. Responsabilidades

## Equipo DevOps

- Supervisar los respaldos.
- Automatizar procesos.
- Verificar la ejecución.
- Mantener la infraestructura.

---

## Administradores

- Revisar informes.
- Autorizar restauraciones críticas.
- Validar políticas de retención.

---

## Equipo de Seguridad

- Verificar el cifrado.
- Auditar accesos.
- Revisar el cumplimiento de las políticas.

---

# 20. Buenas Prácticas

Se recomienda:

- Automatizar todos los respaldos.
- Mantener copias fuera del entorno principal.
- Cifrar toda la información.
- Probar periódicamente la recuperación.
- Documentar cada restauración.
- Supervisar continuamente la ejecución.
- Mantener varias generaciones de respaldos.
- Revisar periódicamente la política de retención.

---

# 21. Documentos Relacionados

Este documento complementa:

- Infraestructura.
- Recuperación ante Desastres.
- Política de Seguridad.
- Configuración Global.
- Manual del Administrador.
- Arquitectura Técnica.
- Arquitectura de Microservicios.

La política de Backups constituye uno de los pilares de continuidad operativa de Nexa Knowledge AI y garantiza que la información crítica pueda recuperarse de forma segura, íntegra y controlada ante cualquier incidente que afecte a la plataforma.