# Solución de Problemas

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Uso Interno

---

# 1. Introducción

## Objetivo

Este documento proporciona una guía estructurada para diagnosticar y resolver los problemas más frecuentes que pueden presentarse durante la operación de Nexa Knowledge AI.

Está dirigido a:

- Equipo de Soporte.
- Administradores.
- DevOps.
- Ingeniería.
- Personal técnico autorizado.

---

# 2. Metodología de Diagnóstico

Antes de intervenir cualquier incidente deberá seguirse el siguiente procedimiento.

## Paso 1

Identificar el problema.

Responder:

- ¿Qué ocurrió?
- ¿Cuándo ocurrió?
- ¿Quién fue afectado?
- ¿Es reproducible?

---

## Paso 2

Clasificar el incidente.

Ejemplos:

- Autenticación
- Documentos
- IA
- API
- Permisos
- Rendimiento
- Infraestructura

---

## Paso 3

Revisar registros.

Consultar:

- Logs del servicio.
- Auditoría.
- Eventos.
- Monitoreo.
- Alertas.

---

## Paso 4

Verificar el impacto.

Determinar si afecta:

- Un usuario.
- Un Workspace.
- Una organización.
- Toda la plataforma.

---

## Paso 5

Aplicar la solución correspondiente.

---

# 3. Problemas de Inicio de Sesión

## Síntoma

El usuario no puede iniciar sesión.

### Posibles causas

- Contraseña incorrecta.
- Cuenta bloqueada.
- Usuario inactivo.
- Token expirado.
- Problema con el proveedor de identidad.

### Diagnóstico

Verificar:

- Estado del usuario.
- Registros de autenticación.
- Disponibilidad del servicio Auth.
- Configuración del proveedor SSO.

### Solución

- Restablecer contraseña.
- Desbloquear usuario.
- Renovar sesión.
- Revisar configuración SSO.
- Consultar registros del servicio de autenticación.

---

# 4. Problemas de Permisos

## Síntoma

El usuario no puede acceder a un documento.

### Posibles causas

- Permisos insuficientes.
- Documento privado.
- Workspace incorrecto.
- Rol incorrectamente asignado.

### Diagnóstico

Verificar:

- Organización activa.
- Workspace.
- Rol.
- Permisos efectivos.
- Colección.
- Documento.

### Solución

Actualizar los permisos correspondientes.

Nunca conceder privilegios superiores sin autorización.

---

# 5. Problemas al Subir Documentos

## Síntoma

La carga falla.

### Posibles causas

- Formato no permitido.
- Archivo dañado.
- Tamaño excedido.
- Error de almacenamiento.
- Conectividad.

### Diagnóstico

Comprobar:

- Extensión.
- Tamaño.
- Logs del servicio Document Service.
- Disponibilidad del almacenamiento.

### Solución

- Subir nuevamente.
- Corregir el formato.
- Verificar almacenamiento.
- Revisar límites configurados.

---

# 6. Problemas de Procesamiento

## Síntoma

El documento permanece en estado "Procesando".

### Posibles causas

- Servicio detenido.
- Cola bloqueada.
- OCR fallido.
- Error interno.

### Diagnóstico

Revisar:

- Processing Service.
- Cola de eventos.
- Logs.
- Estado del documento.

### Solución

- Reiniciar procesamiento.
- Limpiar cola.
- Reprocesar documento.
- Validar recursos disponibles.

---

# 7. Problemas de Indexación

## Síntoma

El documento existe pero no responde consultas.

### Posibles causas

- Embeddings no generados.
- Error de indexación.
- Base vectorial indisponible.

### Diagnóstico

Comprobar:

- Estado del Embedding Service.
- Estado del Vector Search Service.
- Eventos de indexación.

### Solución

- Regenerar embeddings.
- Reindexar documento.
- Validar la base vectorial.

---

# 8. Problemas del Agente IA

## Síntoma

El agente responde incorrectamente.

### Posibles causas

- Contexto insuficiente.
- Documento incompleto.
- Recuperación semántica incorrecta.
- Error del proveedor LLM.

### Diagnóstico

Verificar:

- Chunks recuperados.
- Prompt generado.
- Estado del proveedor IA.
- Historial de conversación.

### Solución

- Reindexar documentos.
- Mejorar la consulta.
- Validar la configuración RAG.
- Repetir la solicitud.

---

# 9. Respuestas Sin Información

## Síntoma

El sistema responde:

"No se encontró información suficiente."

### Diagnóstico

Verificar:

- Existencia del documento.
- Permisos.
- Indexación.
- Procesamiento completo.

### Solución

Procesar nuevamente el documento o ampliar la documentación disponible.

---

# 10. Problemas de Rendimiento

## Síntoma

La plataforma responde lentamente.

### Posibles causas

- Sobrecarga.
- Alta concurrencia.
- Base vectorial lenta.
- Proveedor IA.
- Recursos insuficientes.

### Diagnóstico

Consultar:

- CPU.
- Memoria.
- Latencia.
- Métricas.
- Dashboards.

### Solución

- Escalar servicios.
- Revisar consultas.
- Incrementar recursos.
- Optimizar índices.

---

# 11. Problemas con la API

## Síntoma

La API devuelve errores.

### Posibles códigos

| Código | Significado |
|---------|-------------|
| 400 | Solicitud incorrecta |
| 401 | No autenticado |
| 403 | Sin permisos |
| 404 | Recurso inexistente |
| 409 | Conflicto |
| 429 | Demasiadas solicitudes |
| 500 | Error interno |

### Diagnóstico

Consultar:

- Logs.
- Request ID.
- Correlation ID.
- API Gateway.

---

# 12. Problemas de Integraciones

## Síntoma

Una integración externa deja de funcionar.

### Diagnóstico

Verificar:

- API Keys.
- Certificados.
- Conectividad.
- Versiones.
- Estado del proveedor.

### Solución

Actualizar credenciales o restablecer la integración.

---

# 13. Problemas de Base de Datos

## Síntoma

Errores de persistencia.

### Diagnóstico

Comprobar:

- Conectividad.
- Espacio disponible.
- Replicación.
- Estado del motor.

### Solución

- Restaurar servicio.
- Revisar conexiones.
- Recuperar desde backup cuando sea necesario.

---

# 14. Problemas de Almacenamiento

## Síntoma

No pueden descargarse documentos.

### Diagnóstico

Revisar:

- Servicio de almacenamiento.
- Permisos.
- Disponibilidad.
- Integridad del archivo.

### Solución

Restaurar almacenamiento o recuperar el documento desde una copia válida.

---

# 15. Problemas de Infraestructura

## Síntoma

Varios servicios presentan fallos simultáneamente.

### Diagnóstico

Consultar:

- Infraestructura.
- Balanceadores.
- Redes.
- Contenedores.
- Orquestador.

### Solución

Aplicar el procedimiento definido en el Plan de Recuperación ante Desastres cuando corresponda.

---

# 16. Herramientas de Diagnóstico

Durante el análisis de incidentes podrán utilizarse:

- Logs centralizados.
- Dashboards.
- Métricas.
- Trazas distribuidas.
- Auditoría.
- Monitoreo.
- Alertas.

---

# 17. Escalamiento

Cuando un incidente no pueda resolverse en el primer nivel de soporte deberá escalarse.

## Nivel 1

Soporte funcional.

---

## Nivel 2

Administradores de plataforma.

---

## Nivel 3

Ingeniería.

---

## Nivel 4

DevOps.

---

## Nivel 5

Arquitectura o Dirección Técnica.

---

# 18. Registro del Incidente

Todo incidente deberá documentarse indicando:

- Fecha.
- Hora.
- Usuario afectado.
- Organización.
- Workspace.
- Descripción.
- Causa.
- Solución aplicada.
- Responsable.
- Tiempo de resolución.

---

# 19. Buenas Prácticas

Se recomienda:

- Revisar primero los registros antes de actuar.
- No modificar configuraciones directamente en producción sin autorización.
- Validar siempre los permisos del usuario.
- Mantener la documentación actualizada.
- Ejecutar pruebas después de cada corrección.
- Registrar todas las acciones realizadas.
- Utilizar procedimientos estandarizados.
- Escalar oportunamente cuando el incidente exceda el alcance del equipo.

---

# 20. Documentos Relacionados

Este documento complementa:

- FAQ.
- Manual del Administrador.
- Gestión de Documentos.
- Arquitectura RAG.
- Funcionamiento del Agente IA.
- Política de Seguridad.
- Infraestructura.
- Backups.
- Recuperación ante Desastres.

La Guía de Solución de Problemas constituye el procedimiento oficial para el diagnóstico y resolución de incidencias en Nexa Knowledge AI, proporcionando un marco uniforme para garantizar una atención eficiente, documentada y alineada con las mejores prácticas operativas.