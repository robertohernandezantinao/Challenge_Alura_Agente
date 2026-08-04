# Gestión de Tokens

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Interno

---

# 1. Introducción

## Objetivo

El presente documento define la estrategia oficial para la gestión de **Tokens de Autenticación** utilizados por Nexa Knowledge AI.

Su finalidad es establecer las políticas para la emisión, validación, renovación, revocación y protección de los tokens empleados durante la autenticación de usuarios, aplicaciones y servicios internos.

---

# 2. Alcance

Este documento aplica a:

- API REST.
- Panel Web.
- Microservicios.
- Clientes oficiales.
- Integraciones de terceros.
- Equipos de Desarrollo.
- Administradores de la plataforma.

Todas las comunicaciones autenticadas deberán utilizar los mecanismos descritos en este documento.

---

# 3. Objetivos

La gestión de tokens busca:

- Garantizar autenticación segura.
- Evitar accesos no autorizados.
- Reducir riesgos de suplantación.
- Permitir sesiones controladas.
- Facilitar la revocación de credenciales.
- Mantener trazabilidad de las sesiones.

---

# 4. Tipos de Tokens

La plataforma puede utilizar distintos tipos de tokens según el escenario.

## Access Token

Utilizado para autenticar solicitudes hacia la API.

Características:

- Vida útil corta.
- Firmado digitalmente.
- Contiene los permisos del usuario.
- Es enviado en cada solicitud autenticada.

---

## Refresh Token

Permite obtener un nuevo Access Token sin requerir un nuevo inicio de sesión.

Características:

- Vida útil mayor.
- Se almacena de forma segura.
- Nunca debe enviarse en cada petición de la API.
- Puede revocarse individualmente.

---

## API Token

Credencial utilizada por aplicaciones externas.

Características:

- Asociado a una organización o integración.
- Permisos limitados.
- Revocable.
- Auditable.

---

## Service Token

Utilizado para autenticación entre microservicios.

Características:

- Uso exclusivamente interno.
- No disponible para usuarios finales.
- Vida útil controlada.
- Emitido por el sistema de autenticación.

---

# 5. Estructura del Token

Los tokens emitidos por la plataforma contienen información mínima necesaria para la autenticación.

Dependiendo del mecanismo utilizado pueden incluir:

- Identificador del usuario.
- Organización.
- Workspace.
- Roles.
- Permisos.
- Fecha de emisión.
- Fecha de expiración.
- Identificador único del token.
- Emisor.
- Audiencia.

No deben contener información sensible innecesaria.

---

# 6. Emisión de Tokens

Los tokens son emitidos únicamente después de una autenticación exitosa.

El proceso general comprende:

1. Validación de credenciales.
2. Verificación de políticas de seguridad.
3. Generación del Access Token.
4. Generación del Refresh Token (cuando corresponda).
5. Registro del evento de autenticación.
6. Entrega segura al cliente.

---

# 7. Validación

Cada solicitud autenticada debe validar:

- Firma digital.
- Fecha de expiración.
- Integridad.
- Emisor autorizado.
- Audiencia correcta.
- Estado del usuario.
- Revocación del token.

Solo tras superar estas validaciones se autoriza el acceso a los recursos.

---

# 8. Renovación

Cuando el Access Token expira, el cliente puede solicitar uno nuevo utilizando un Refresh Token válido.

La renovación debe verificar:

- Validez del Refresh Token.
- Estado de la sesión.
- Estado del usuario.
- Políticas de seguridad vigentes.

Si la validación falla, el usuario deberá autenticarse nuevamente.

---

# 9. Expiración

La plataforma establece tiempos de vida diferenciados según el tipo de token.

Ejemplo de política:

| Tipo | Duración recomendada |
|------|----------------------|
| Access Token | 15–60 minutos |
| Refresh Token | Días o semanas, según configuración |
| API Token | Configurable |
| Service Token | Vida útil reducida y controlada |

Los valores exactos pueden variar según las políticas de cada organización.

---

# 10. Revocación

Un token puede revocarse por diversas razones:

- Cierre de sesión.
- Cambio de contraseña.
- Revocación manual.
- Compromiso de credenciales.
- Desactivación del usuario.
- Incidente de seguridad.

Un token revocado deja de ser válido inmediatamente.

---

# 11. Almacenamiento Seguro

Los clientes deben almacenar los tokens utilizando mecanismos seguros.

Se recomienda:

- Cookies seguras con atributos `HttpOnly` y `Secure` para aplicaciones web.
- Almacenamiento seguro proporcionado por el sistema operativo en aplicaciones móviles.
- Gestión mediante servicios de secretos para aplicaciones servidor.

No se recomienda almacenar tokens en ubicaciones expuestas al código cliente cuando existan alternativas más seguras.

---

# 12. Transporte Seguro

Todos los tokens deben transmitirse únicamente mediante conexiones cifradas.

Requisitos:

- HTTPS obligatorio.
- Certificados TLS válidos.
- Prohibición de transmisión mediante protocolos inseguros.

---

# 13. Auditoría

La plataforma registra eventos relevantes relacionados con los tokens.

Ejemplos:

- Emisión.
- Renovación.
- Revocación.
- Expiración.
- Uso indebido.
- Intentos fallidos de validación.

Estos registros permiten detectar comportamientos anómalos.

---

# 14. Seguridad

Las políticas de seguridad establecen que:

- Nunca se deben registrar tokens completos en logs.
- Los tokens deben firmarse digitalmente.
- Deben utilizar tiempos de expiración adecuados.
- Deben protegerse frente a robo y reutilización.
- Deben invalidarse cuando exista sospecha de compromiso.

---

# 15. Integración con la Plataforma

La gestión de tokens interactúa con:

- Autenticación.
- Autorización.
- Gestión de Usuarios.
- Gestión de Roles.
- API REST.
- Microservicios.
- Auditoría.
- Monitorización.
- Seguridad.

Los tokens representan el mecanismo principal para autenticar solicitudes.

---

# 16. Buenas Prácticas

Se recomienda:

- Utilizar Access Tokens de corta duración.
- Rotar Refresh Tokens cuando sea posible.
- Revocar credenciales comprometidas inmediatamente.
- Limitar los permisos incluidos en cada token.
- Aplicar el principio de mínimo privilegio.
- Auditar periódicamente los eventos de autenticación.

---

# 17. Limitaciones

Los tokens no sustituyen otros controles de seguridad.

Es necesario complementarlos con:

- Autorización basada en roles.
- Gestión de permisos.
- Políticas de seguridad.
- Monitorización continua.
- Auditoría.

---

# 18. Glosario

| Término | Descripción |
|----------|-------------|
| Access Token | Token utilizado para autenticar solicitudes a la API. |
| Refresh Token | Token utilizado para obtener un nuevo Access Token. |
| API Token | Credencial utilizada por aplicaciones externas. |
| Service Token | Token empleado en comunicaciones entre servicios internos. |
| Revocación | Proceso mediante el cual un token deja de ser válido antes de su expiración. |
| Expiración | Momento a partir del cual un token ya no puede utilizarse. |

---

# 19. Documentos Relacionados

Este documento complementa:

- Introducción API.
- Autenticación.
- Usuarios API.
- Documentos API.
- Chat API.
- Gestión de Usuarios.
- Gestión de Roles.
- Política de Seguridad.
- Gestión de Secretos.
- Arquitectura de Microservicios.

La presente documentación constituye la guía oficial para la gestión de tokens de autenticación en Nexa Knowledge AI y establece las políticas, procedimientos y controles necesarios para garantizar una autenticación segura, escalable y alineada con los estándares de seguridad de una plataforma SaaS empresarial.