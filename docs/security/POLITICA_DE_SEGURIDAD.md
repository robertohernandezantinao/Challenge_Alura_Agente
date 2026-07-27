# Política de Seguridad

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Uso Interno

---

# 1. Introducción

## Objetivo

Esta Política de Seguridad establece los principios, normas y controles que rigen la protección de la información, la infraestructura y los servicios de Nexa Knowledge AI.

Su propósito es garantizar la confidencialidad, integridad, disponibilidad y trazabilidad de la información gestionada por la plataforma, minimizando los riesgos asociados al uso de tecnologías de Inteligencia Artificial y servicios en la nube.

---

# 2. Alcance

Esta política aplica a:

- Todos los colaboradores de NexaDigital S.A.S.
- Administradores de la plataforma.
- Desarrolladores.
- Personal de soporte.
- Clientes que utilizan la plataforma.
- Integraciones externas.
- Proveedores tecnológicos autorizados.

También aplica a todos los entornos:

- Desarrollo.
- Pruebas.
- Staging.
- Producción.

---

# 3. Objetivos de Seguridad

La plataforma deberá garantizar:

- Confidencialidad de la información.
- Integridad de los datos.
- Disponibilidad de los servicios.
- Autenticidad de los usuarios.
- Trazabilidad de todas las operaciones.
- Protección frente a accesos no autorizados.
- Cumplimiento de la normativa aplicable.

---

# 4. Principios de Seguridad

Toda decisión técnica y funcional deberá respetar los siguientes principios.

## Seguridad por diseño

La seguridad deberá incorporarse desde las primeras etapas del desarrollo.

---

## Mínimo privilegio

Cada usuario únicamente dispondrá de los permisos estrictamente necesarios para realizar su trabajo.

---

## Defensa en profundidad

La protección deberá implementarse mediante múltiples capas de seguridad.

---

## Zero Trust

Ningún usuario, dispositivo o servicio será considerado confiable por defecto.

Toda solicitud deberá ser autenticada y autorizada.

---

## Auditoría permanente

Las acciones relevantes deberán quedar registradas para permitir investigaciones posteriores.

---

# 5. Clasificación de la Información

Toda la información administrada por la plataforma deberá clasificarse según su nivel de sensibilidad.

| Nivel | Descripción |
|---------|-------------|
| Pública | Información destinada a difusión pública. |
| Interna | Información de uso exclusivo de la organización. |
| Confidencial | Información cuyo acceso está restringido. |
| Restringida | Información crítica cuyo acceso requiere autorización específica. |

La clasificación determinará los controles de acceso aplicables.

---

# 6. Gestión de Identidades

Todo acceso requiere una identidad válida.

Las cuentas deberán ser:

- Individuales.
- Únicas.
- Trazables.
- Revocables.

No se permiten cuentas compartidas.

---

# 7. Autenticación

La plataforma admite distintos mecanismos de autenticación.

Entre ellos:

- Usuario y contraseña.
- OAuth 2.0.
- OpenID Connect.
- SAML 2.0.
- Microsoft Entra ID.
- Google Workspace.

Cuando la organización lo requiera, será obligatorio utilizar autenticación multifactor (MFA).

---

# 8. Autorización

La autorización se implementa mediante el Modelo Oficial de Permisos de Nexa Knowledge AI.

Toda operación verifica:

- Usuario autenticado.
- Organización activa.
- Rol asignado.
- Permisos efectivos.
- Recurso solicitado.

Las verificaciones se realizan antes de acceder a cualquier información.

---

# 9. Protección de Datos

La plataforma deberá proteger:

- Datos personales.
- Documentos corporativos.
- Conversaciones.
- Embeddings.
- Metadatos.
- Registros de auditoría.
- Configuración.

Los datos únicamente podrán utilizarse para las finalidades autorizadas.

---

# 10. Seguridad Documental

Los documentos cargados deberán:

- Permanecer asociados a su organización.
- Mantener aislamiento entre clientes.
- Conservar su historial de versiones.
- Respetar las políticas de retención.
- Ser accesibles únicamente para usuarios autorizados.

---

# 11. Seguridad de la Arquitectura RAG

La arquitectura RAG incorpora controles específicos para evitar la exposición de información.

Antes de recuperar cualquier fragmento documental se validan:

- Organización.
- Workspace.
- Colección.
- Documento.
- Permisos del usuario.
- Estado del documento.

Los Agentes IA nunca recuperarán información fuera del alcance autorizado.

---

# 12. Seguridad de los Agentes IA

Los Agentes IA deberán operar siguiendo las siguientes reglas:

- Responder únicamente con información autorizada.
- Utilizar exclusivamente documentos disponibles.
- Respetar el modelo de permisos.
- Evitar revelar información confidencial.
- Indicar cuando no exista evidencia suficiente para responder.
- Registrar las consultas cuando corresponda.

Los Agentes IA no deberán generar respuestas basadas en documentos inaccesibles para el usuario.

---

# 13. Cifrado

La información deberá protegerse mediante mecanismos de cifrado adecuados.

## Datos en tránsito

Toda comunicación utilizará HTTPS con TLS.

---

## Datos en reposo

La información almacenada deberá mantenerse cifrada utilizando mecanismos compatibles con la infraestructura utilizada.

---

## Gestión de claves

Las claves criptográficas deberán:

- Almacenarse de forma segura.
- Rotarse periódicamente.
- Tener acceso restringido.
- Nunca almacenarse en el código fuente.

---

# 14. Gestión de Secretos

Las credenciales de acceso deberán gestionarse mediante servicios especializados de almacenamiento seguro.

Se prohíbe almacenar:

- Contraseñas.
- Tokens.
- Claves API.
- Certificados privados.

En repositorios de código o archivos de configuración no protegidos.

---

# 15. Registro y Auditoría

El sistema registrará eventos relacionados con:

- Autenticación.
- Cambios administrativos.
- Gestión de usuarios.
- Carga de documentos.
- Eliminación de información.
- Consultas de Agentes IA.
- Cambios de permisos.
- Errores críticos.

Los registros deberán conservarse según la política de retención definida por la organización.

---

# 16. Monitoreo

La plataforma deberá supervisar continuamente:

- Disponibilidad.
- Uso de recursos.
- Errores.
- Accesos sospechosos.
- Intentos de autenticación fallidos.
- Actividad administrativa.
- Estado de los servicios.

Las alertas críticas deberán notificarse de forma inmediata al personal responsable.

---

# 17. Gestión de Vulnerabilidades

NexaDigital S.A.S. deberá establecer procesos para:

- Identificar vulnerabilidades.
- Evaluar riesgos.
- Priorizar correcciones.
- Aplicar actualizaciones.
- Verificar la mitigación.

Las dependencias de software deberán mantenerse actualizadas.

---

# 18. Gestión de Incidentes

Ante un incidente de seguridad deberán ejecutarse las siguientes etapas:

1. Identificación.
2. Contención.
3. Análisis.
4. Erradicación.
5. Recuperación.
6. Documentación.
7. Revisión posterior.

Cada incidente deberá registrarse para facilitar futuras mejoras.

---

# 19. Continuidad del Negocio

La plataforma deberá disponer de mecanismos para garantizar la continuidad del servicio.

Entre ellos:

- Copias de seguridad.
- Recuperación ante desastres.
- Replicación.
- Alta disponibilidad.
- Monitoreo continuo.

---

# 20. Responsabilidades

## Administradores

- Configurar controles de seguridad.
- Gestionar permisos.
- Supervisar auditorías.
- Responder ante incidentes.

---

## Desarrolladores

- Aplicar prácticas de desarrollo seguro.
- Corregir vulnerabilidades.
- Revisar dependencias.
- Proteger credenciales.

---

## Usuarios

- Mantener la confidencialidad de sus credenciales.
- Utilizar la plataforma conforme a las políticas establecidas.
- Reportar incidentes de seguridad.

---

# 21. Buenas Prácticas

Se recomienda:

- Activar MFA.
- Utilizar contraseñas robustas.
- Revisar periódicamente los permisos.
- Cerrar sesiones no utilizadas.
- Mantener actualizado el software.
- No compartir credenciales.
- Clasificar correctamente la información.
- Revisar periódicamente los registros de auditoría.

---

# 22. Cumplimiento

El incumplimiento de esta política podrá dar lugar a:

- Revocación de accesos.
- Suspensión de cuentas.
- Investigación interna.
- Medidas disciplinarias.
- Acciones legales cuando corresponda.

---

# 23. Documentos Relacionados

Esta política complementa:

- Modelo de Permisos.
- Manual del Administrador.
- Configuración Global.
- Arquitectura Técnica.
- Arquitectura RAG.
- Arquitectura de Microservicios.
- Backups.
- Recuperación ante Desastres.
- Cumplimiento Normativo.

La Política de Seguridad constituye el marco oficial de protección de Nexa Knowledge AI y establece las directrices que deberán seguir todos los usuarios, administradores y componentes tecnológicos para garantizar un entorno confiable, resiliente y alineado con las mejores prácticas de seguridad de la información.