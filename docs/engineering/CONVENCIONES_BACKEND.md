# Convenciones Backend

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Uso Interno

---

# 1. Introducción

## Objetivo

Este documento define el estándar oficial para el desarrollo del Backend de Nexa Knowledge AI.

Su propósito es garantizar que todos los servicios sean desarrollados siguiendo criterios comunes de arquitectura, calidad, mantenibilidad y seguridad.

Estas convenciones son obligatorias para todos los proyectos backend de NexaDigital S.A.S.

---

# 2. Principios

Todo desarrollo backend deberá cumplir los siguientes principios:

- Código limpio.
- Alta cohesión.
- Bajo acoplamiento.
- Principio SOLID.
- Arquitectura por capas.
- API First.
- Seguridad por defecto.
- Observabilidad.
- Escalabilidad.
- Documentación continua.

---

# 3. Arquitectura Base

Todos los servicios deberán seguir una arquitectura por capas.

```
Controller

↓

Application

↓

Domain

↓

Infrastructure

↓

Persistence
```

Cada capa tendrá responsabilidades claramente definidas.

---

# 4. Organización del Proyecto

Estructura recomendada:

```
src/

├── application/
├── domain/
├── infrastructure/
├── interfaces/
├── controllers/
├── services/
├── repositories/
├── middleware/
├── dto/
├── validators/
├── config/
├── shared/
├── exceptions/
└── tests/
```

La estructura podrá adaptarse siempre que mantenga una separación clara de responsabilidades.

---

# 5. Convenciones de Nombres

## Clases

PascalCase

Ejemplo:

```
DocumentService
```

---

## Interfaces

Prefijo **I**

```
IDocumentRepository
```

---

## Variables

camelCase

```
documentId
```

---

## Constantes

UPPER_SNAKE_CASE

```
MAX_UPLOAD_SIZE
```

---

## Archivos

snake_case o kebab-case, según el estándar del lenguaje utilizado.

Ejemplo:

```
document_service.ts
```

---

# 6. Controllers

Los Controllers deben:

- Recibir solicitudes HTTP.
- Validar parámetros básicos.
- Delegar la lógica al Application Service.
- Construir la respuesta HTTP.

No deben contener lógica de negocio.

---

# 7. Application Services

Responsables de coordinar casos de uso.

Pueden:

- Orquestar servicios.
- Ejecutar validaciones funcionales.
- Controlar transacciones.
- Publicar eventos.

No deben acceder directamente a la base de datos.

---

# 8. Dominio

La capa de dominio contiene:

- Entidades.
- Objetos de valor.
- Agregados.
- Servicios de dominio.
- Reglas de negocio.

Debe permanecer independiente de frameworks y tecnologías externas.

---

# 9. Repositories

Toda interacción con la persistencia debe realizarse mediante repositorios.

Ejemplo:

```
DocumentRepository
```

Nunca se accederá directamente al motor de base de datos desde otras capas.

---

# 10. DTO (Data Transfer Objects)

Los DTO definen el contrato de entrada y salida de cada operación.

Ejemplos:

```
CreateDocumentRequest
```

```
UpdateUserRequest
```

Los DTO nunca deberán contener lógica de negocio.

---

# 11. Validaciones

Las validaciones deberán realizarse en múltiples niveles:

- Formato.
- Tipos.
- Reglas de negocio.
- Integridad.
- Permisos.

Los datos inválidos deberán rechazarse antes de ejecutar la lógica principal.

---

# 12. Manejo de Errores

Todos los errores deberán utilizar excepciones controladas.

Ejemplos:

- ValidationException
- NotFoundException
- UnauthorizedException
- ForbiddenException
- ConflictException
- BusinessRuleException

No se devolverán mensajes internos del sistema al cliente.

---

# 13. Respuestas API

Todas las respuestas seguirán una estructura uniforme.

Ejemplo exitoso:

```json
{
  "success": true,
  "data": {}
}
```

Ejemplo de error:

```json
{
  "success": false,
  "error": {
    "code": "DOCUMENT_NOT_FOUND",
    "message": "El documento no existe."
  }
}
```

---

# 14. Seguridad

Todo servicio deberá:

- Validar autenticación.
- Verificar permisos.
- Sanitizar entradas.
- Validar archivos.
- Evitar inyección de código.
- Proteger información sensible.

Nunca se confiará en los datos enviados por el cliente.

---

# 15. Logging

Los logs deberán ser:

- Estructurados.
- Consistentes.
- Trazables.

Cada registro deberá incluir, cuando corresponda:

- Timestamp.
- Nivel.
- Servicio.
- Usuario.
- Request ID.
- Correlation ID.
- Operación.
- Duración.

Nunca deberán registrarse contraseñas, tokens ni información confidencial.

---

# 16. Configuración

La configuración deberá separarse del código.

Ejemplos:

- Variables de entorno.
- Archivos de configuración.
- Gestores de secretos.

No deberán existir valores sensibles codificados directamente en el repositorio.

---

# 17. Persistencia

Las consultas deberán:

- Ser eficientes.
- Utilizar índices adecuados.
- Evitar duplicidad.
- Minimizar bloqueos.

Se recomienda aplicar migraciones versionadas para todos los cambios de esquema.

---

# 18. Eventos

Los eventos publicados deberán:

- Tener nombres descriptivos.
- Ser inmutables.
- Estar versionados.
- Contener únicamente la información necesaria.

Ejemplos:

```
DocumentUploaded
```

```
UserCreated
```

```
WorkspaceArchived
```

---

# 19. Pruebas

Todo desarrollo deberá incluir pruebas.

## Unitarias

Validan reglas de negocio de forma aislada.

---

## Integración

Verifican la interacción entre componentes.

---

## End-to-End

Comprueban el funcionamiento completo del flujo.

---

Las nuevas funcionalidades no deberán incorporarse sin una cobertura mínima definida por el equipo.

---

# 20. Documentación

Todo endpoint deberá documentarse indicando:

- Objetivo.
- Parámetros.
- Ejemplos.
- Respuestas.
- Códigos HTTP.
- Errores posibles.
- Permisos requeridos.

La documentación deberá mantenerse sincronizada con el código.

---

# 21. Observabilidad

Todos los servicios deberán exponer:

```
/health
```

Estado básico del servicio.

---

```
/ready
```

Disponibilidad para recibir tráfico.

---

```
/metrics
```

Métricas para monitoreo.

---

# 22. Rendimiento

Se recomienda:

- Minimizar consultas repetidas.
- Utilizar paginación.
- Implementar caché cuando sea apropiado.
- Procesar tareas pesadas de forma asíncrona.
- Optimizar operaciones sobre grandes volúmenes de datos.

---

# 23. Revisión de Código

Todo cambio deberá pasar por revisión antes de integrarse.

La revisión verificará:

- Calidad del código.
- Cumplimiento de convenciones.
- Seguridad.
- Rendimiento.
- Cobertura de pruebas.
- Impacto arquitectónico.

---

# 24. Buenas Prácticas

- Mantener funciones pequeñas.
- Evitar duplicación de código.
- Escribir código legible.
- Nombrar correctamente variables y métodos.
- Eliminar código muerto.
- Documentar decisiones complejas.
- Mantener dependencias actualizadas.
- Respetar los límites entre capas.

---

# 25. Relación con otros documentos

Este documento complementa:

- Arquitectura Técnica.
- Arquitectura de Microservicios.
- Introducción API.
- Convenciones Frontend.
- Política de Seguridad.
- Manual del Administrador.
- Infraestructura.
- Configuración Global.

Las Convenciones Backend constituyen el estándar oficial de desarrollo para todos los servicios de Nexa Knowledge AI y garantizan que la plataforma evolucione de forma consistente, mantenible y alineada con las mejores prácticas de ingeniería de software.