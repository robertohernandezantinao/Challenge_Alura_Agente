# Configuración Global

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

---

# 1. Introducción

## Objetivo

Este documento define la configuración global de Nexa Knowledge AI.

Describe todos los parámetros que afectan el comportamiento general de la plataforma y que únicamente pueden ser modificados por administradores con privilegios globales.

Su propósito es garantizar una administración centralizada, segura y consistente del sistema.

---

# 2. Alcance

La Configuración Global afecta a todas las organizaciones alojadas en la plataforma.

Incluye parámetros relacionados con:

- Seguridad.
- Autenticación.
- Inteligencia Artificial.
- Arquitectura RAG.
- Almacenamiento.
- Auditoría.
- Integraciones.
- Notificaciones.
- Límites operativos.
- Variables generales del sistema.

---

# 3. Responsables

La modificación de la Configuración Global está restringida a:

- Super Administradores.
- Administradores Globales.
- Personal autorizado por NexaDigital S.A.S.

Todas las modificaciones generan registros de auditoría.

---

# 4. Principios

Toda configuración deberá cumplir los siguientes principios:

- Seguridad por defecto.
- Mínimo privilegio.
- Alta disponibilidad.
- Escalabilidad.
- Trazabilidad.
- Compatibilidad.
- Facilidad de mantenimiento.

---

# 5. Configuración de Autenticación

Desde este módulo pueden definirse los mecanismos de autenticación disponibles.

## Métodos soportados

- Usuario y contraseña.
- OAuth 2.0.
- OpenID Connect.
- SAML 2.0.
- Microsoft Entra ID.
- Google Workspace.

Cada organización podrá habilitar únicamente los métodos autorizados.

---

## Políticas de contraseña

Configuraciones disponibles:

- Longitud mínima.
- Longitud máxima.
- Complejidad requerida.
- Tiempo de expiración.
- Historial de contraseñas.
- Intentos fallidos permitidos.
- Bloqueo automático.

---

## Autenticación Multifactor (MFA)

Opciones configurables:

- Obligatoria.
- Opcional.
- Deshabilitada.

Métodos disponibles:

- Aplicación autenticadora.
- Correo electrónico.
- SMS (si está habilitado).
- Llaves de seguridad compatibles.

---

# 6. Configuración de Organizaciones

Parámetros globales:

- Número máximo de organizaciones.
- Estado por defecto.
- Políticas de creación.
- Dominios permitidos.
- Personalización visual.
- Configuración regional.

---

# 7. Configuración de Usuarios

Permite definir:

- Número máximo de usuarios por organización.
- Política de invitaciones.
- Auto registro.
- Tiempo de expiración de invitaciones.
- Sesiones simultáneas permitidas.
- Tiempo máximo de inactividad.

---

# 8. Configuración de Workspaces

Opciones globales:

- Número máximo por organización.
- Creación automática.
- Límites de almacenamiento.
- Configuración predeterminada.
- Visibilidad inicial.

---

# 9. Configuración de Colecciones

Permite establecer:

- Número máximo de colecciones.
- Convenciones de nombres.
- Configuración inicial.
- Políticas de archivado.
- Reglas de organización.

---

# 10. Configuración de Documentos

Parámetros principales:

- Tamaño máximo de archivo.
- Formatos permitidos.
- Cantidad máxima por colección.
- Política de versionado.
- Política de eliminación.
- Retención documental.

---

## Formatos compatibles

Ejemplos:

- PDF
- DOCX
- XLSX
- PPTX
- TXT
- Markdown
- CSV

La lista podrá ampliarse mediante nuevas integraciones.

---

# 11. Configuración de Inteligencia Artificial

Este módulo controla el comportamiento general de los Agentes IA.

Parámetros configurables:

- Modelo de lenguaje predeterminado.
- Temperatura.
- Máximo de tokens.
- Tiempo máximo de respuesta.
- Número de respuestas paralelas.
- Estrategias de recuperación.

Cada Agente podrá sobrescribir estos valores cuando la configuración lo permita.

---

# 12. Configuración de Embeddings

Opciones disponibles:

- Modelo de embeddings.
- Dimensión vectorial.
- Estrategia de actualización.
- Reindexación automática.
- Política de regeneración.

Los cambios en este módulo pueden requerir la reindexación completa de la Base de Conocimiento.

---

# 13. Configuración de la Arquitectura RAG

Parámetros globales:

- Tamaño de Chunk.
- Solapamiento entre Chunks.
- Número máximo de Chunks recuperados.
- Umbral mínimo de similitud.
- Estrategia de ranking.
- Recuperación híbrida (cuando esté habilitada).
- Reordenamiento de resultados.

Estas configuraciones impactan directamente en la calidad de las respuestas generadas.

---

# 14. Configuración de la Base Vectorial

Opciones generales:

- Proveedor.
- Índices.
- Estrategia de almacenamiento.
- Política de sincronización.
- Compresión.
- Replicación.
- Mantenimiento.

---

# 15. Configuración de Auditoría

Permite definir:

- Tiempo de retención.
- Eventos auditables.
- Nivel de detalle.
- Exportación.
- Integraciones con plataformas SIEM.
- Rotación de registros.

---

# 16. Configuración de Notificaciones

Tipos de notificaciones:

- Correo electrónico.
- Notificaciones internas.
- Webhooks.
- Integraciones externas.

Eventos configurables:

- Invitaciones.
- Procesamiento de documentos.
- Errores.
- Incidentes.
- Cambios administrativos.

---

# 17. Configuración de Integraciones

La plataforma permite configurar integraciones con servicios externos.

Ejemplos:

- Proveedores de identidad.
- Servicios de correo.
- Sistemas de almacenamiento.
- Plataformas de monitoreo.
- Modelos de IA.
- Bases vectoriales.
- Sistemas de registro de eventos.

Cada integración deberá disponer de sus credenciales correspondientes y ser validada antes de entrar en producción.

---

# 18. Configuración de Límites Operativos

Parámetros configurables:

- Solicitudes por minuto.
- Consultas simultáneas.
- Tamaño máximo de contexto.
- Tiempo máximo de ejecución.
- Número máximo de documentos por consulta.
- Límite de conversaciones activas.

Estos valores ayudan a proteger la estabilidad de la plataforma.

---

# 19. Variables del Sistema

El sistema dispone de variables globales para controlar su comportamiento.

Ejemplos:

- Entorno de ejecución.
- Región.
- Zona horaria.
- Idioma predeterminado.
- Configuración regional.
- Políticas de mantenimiento.

Las variables deberán mantenerse documentadas y gestionadas mediante mecanismos seguros.

---

# 20. Gestión de Cambios

Toda modificación en la Configuración Global deberá seguir un proceso controlado.

Se recomienda:

1. Analizar el impacto.
2. Aprobar el cambio.
3. Registrar la modificación.
4. Aplicar la configuración.
5. Verificar el funcionamiento.
6. Monitorear el sistema.
7. Documentar el resultado.

---

# 21. Buenas Prácticas

- Aplicar cambios fuera de horarios críticos cuando sea posible.
- Probar configuraciones en entornos no productivos.
- Mantener respaldos de la configuración.
- Revisar periódicamente los parámetros globales.
- Evitar modificaciones innecesarias.
- Documentar todas las excepciones.
- Aplicar el principio de mínimo privilegio.

---

# 22. Auditoría

Cada cambio realizado sobre la Configuración Global registra como mínimo:

- Usuario responsable.
- Fecha y hora.
- Parámetro modificado.
- Valor anterior.
- Valor nuevo.
- Dirección IP.
- Resultado de la operación.

Estos registros no podrán ser modificados por usuarios comunes.

---

# 23. Relación con otros documentos

Este documento complementa:

- Manual del Administrador.
- Política de Seguridad.
- Arquitectura Técnica.
- Arquitectura de Microservicios.
- Arquitectura RAG.
- Modelo de Permisos.
- Infraestructura.
- Backups.
- Recuperación ante Desastres.

La Configuración Global constituye el punto central de administración de Nexa Knowledge AI y define los parámetros que garantizan un funcionamiento uniforme, seguro y escalable para todas las organizaciones que utilizan la plataforma.