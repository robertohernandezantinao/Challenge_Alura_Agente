# Casos de Uso

**Producto:** Nexa Knowledge AI  
**Empresa:** NexaDigital S.A.S.  
**Versión:** 1.0

---

# 1. Introducción

## 1.1 Objetivo

Este documento describe los casos de uso funcionales de Nexa Knowledge AI.

Cada caso de uso representa una interacción entre uno o más actores y la plataforma para alcanzar un objetivo de negocio específico.

Los casos de uso definidos en este documento constituyen la referencia oficial para el diseño funcional, la implementación, las pruebas y la documentación del producto.

---

# 2. Actores

## Usuario

Persona autenticada que interactúa con la plataforma para consultar información, administrar documentos o gestionar recursos autorizados.

---

## Administrador

Usuario con privilegios para administrar la organización, usuarios, configuraciones y políticas.

---

## Agente IA

Componente inteligente encargado de procesar consultas, recuperar contexto y generar respuestas fundamentadas.

---

## Sistema

Representa los procesos automáticos ejecutados por la plataforma.

Ejemplos:

- Procesamiento documental.
- Indexación.
- Generación de embeddings.
- Sincronización.
- Auditoría.
- Notificaciones.

---

# 3. Convenciones

Cada caso de uso incluye:

- Identificador
- Nombre
- Objetivo
- Actores
- Precondiciones
- Flujo principal
- Flujos alternativos
- Resultado esperado

---

# 4. Gestión de Organizaciones

---

## UC-ORG-001 Crear Organización

### Objetivo

Registrar una nueva organización dentro de la plataforma.

### Actores

- Administrador

### Precondiciones

- El usuario posee permisos para crear organizaciones.

### Flujo principal

1. Selecciona "Nueva Organización".
2. Ingresa la información requerida.
3. Configura el plan inicial.
4. Confirma la creación.
5. El sistema crea la organización.
6. Se registra el evento en auditoría.

### Resultado esperado

La organización queda disponible para su uso.

---

## UC-ORG-002 Actualizar Organización

### Objetivo

Modificar la información general de una organización.

---

## UC-ORG-003 Suspender Organización

### Objetivo

Suspender temporalmente una organización.

---

## UC-ORG-004 Eliminar Organización

### Objetivo

Eliminar una organización siguiendo las políticas de retención de datos.

---

# 5. Gestión de Usuarios

---

## UC-USR-001 Invitar Usuario

### Objetivo

Incorporar un nuevo usuario a la organización.

### Flujo principal

1. El administrador selecciona "Invitar Usuario".
2. Ingresa el correo electrónico.
3. Selecciona el rol.
4. El sistema envía la invitación.
5. El usuario acepta la invitación.
6. Se activa la cuenta.

---

## UC-USR-002 Modificar Usuario

---

## UC-USR-003 Desactivar Usuario

---

## UC-USR-004 Restablecer Contraseña

---

# 6. Gestión de Workspaces

---

## UC-WSP-001 Crear Workspace

### Objetivo

Crear un nuevo espacio de trabajo.

---

## UC-WSP-002 Configurar Workspace

---

## UC-WSP-003 Eliminar Workspace

---

## UC-WSP-004 Transferir Workspace

---

# 7. Gestión Documental

---

## UC-DOC-001 Subir Documento

### Objetivo

Agregar un nuevo documento a la base de conocimiento.

### Flujo principal

1. Seleccionar Workspace.
2. Seleccionar Colección.
3. Seleccionar archivo.
4. Validar formato.
5. Cargar archivo.
6. Registrar metadatos.
7. Iniciar procesamiento.

### Resultado esperado

El documento queda registrado y pendiente de indexación.

---

## UC-DOC-002 Actualizar Documento

---

## UC-DOC-003 Eliminar Documento

---

## UC-DOC-004 Versionar Documento

---

## UC-DOC-005 Restaurar Versión

---

# 8. Procesamiento Inteligente

---

## UC-ING-001 Procesar Documento

### Objetivo

Transformar un documento en conocimiento indexable.

### Flujo principal

1. Extraer contenido.
2. Limpiar texto.
3. Detectar idioma.
4. Dividir en fragmentos.
5. Generar embeddings.
6. Almacenar información.
7. Actualizar estado.

---

## UC-ING-002 Reindexar Documento

---

## UC-ING-003 Validar Procesamiento

---

# 9. Base de Conocimiento

---

## UC-KB-001 Crear Colección

---

## UC-KB-002 Mover Documentos

---

## UC-KB-003 Sincronizar Conocimiento

---

# 10. Agentes IA

---

## UC-AI-001 Crear Agente IA

### Objetivo

Crear un nuevo agente especializado.

### Flujo principal

1. Definir nombre.
2. Definir instrucciones.
3. Seleccionar modelo IA.
4. Configurar temperatura.
5. Asociar colecciones.
6. Configurar herramientas.
7. Publicar agente.

---

## UC-AI-002 Editar Agente IA

---

## UC-AI-003 Duplicar Agente IA

---

## UC-AI-004 Eliminar Agente IA

---

# 11. Conversaciones

---

## UC-CHAT-001 Iniciar Conversación

### Objetivo

Crear una nueva conversación con un Agente IA.

### Flujo principal

1. Seleccionar agente.
2. Escribir consulta.
3. Enviar pregunta.
4. Recuperar contexto.
5. Generar respuesta.
6. Mostrar fuentes.

---

## UC-CHAT-002 Continuar Conversación

---

## UC-CHAT-003 Compartir Conversación

---

## UC-CHAT-004 Exportar Conversación

---

# 12. Consultas Inteligentes

---

## UC-ASK-001 Realizar Consulta

### Objetivo

Responder preguntas utilizando lenguaje natural.

### Flujo principal

1. Recibir pregunta.
2. Interpretar intención.
3. Ejecutar búsqueda semántica.
4. Recuperar contexto.
5. Construir prompt.
6. Consultar el modelo IA.
7. Validar respuesta.
8. Mostrar fuentes.

### Resultado esperado

El usuario obtiene una respuesta fundamentada en información autorizada.

---

## UC-ASK-002 Consultar Documento Específico

---

## UC-ASK-003 Consultar Colección

---

## UC-ASK-004 Aplicar Filtros

---

## UC-ASK-005 Regenerar Respuesta

---

# 13. Administración

---

## UC-ADM-001 Configurar Organización

---

## UC-ADM-002 Administrar Licencias

---

## UC-ADM-003 Configurar Modelos IA

---

## UC-ADM-004 Configurar Integraciones

---

# 14. Facturación

---

## UC-BILL-001 Cambiar Plan

---

## UC-BILL-002 Renovar Suscripción

---

## UC-BILL-003 Consultar Facturas

---

# 15. Auditoría

---

## UC-AUD-001 Consultar Auditoría

---

## UC-AUD-002 Exportar Auditoría

---

# 16. Integraciones

---

## UC-INT-001 Configurar API

---

## UC-INT-002 Registrar Webhook

---

## UC-INT-003 Integrar Google Workspace

---

## UC-INT-004 Integrar Microsoft 365

---

## UC-INT-005 Integrar Slack

---

## UC-INT-006 Integrar Jira

---

# 17. Seguridad

---

## UC-SEC-001 Iniciar Sesión

---

## UC-SEC-002 Configurar MFA

---

## UC-SEC-003 Configurar SSO

---

## UC-SEC-004 Cerrar Sesión

---

# 18. Matriz de Trazabilidad

| Caso de Uso | Módulo | Funcionalidad |
|--------------|--------|---------------|
| UC-ORG-001 | Organizaciones | ORG-001 |
| UC-USR-001 | Usuarios | USR-001 |
| UC-WSP-001 | Workspaces | WSP-001 |
| UC-DOC-001 | Documentos | DOC-001 |
| UC-ING-001 | Procesamiento | ING-001 |
| UC-KB-001 | Base de Conocimiento | KB-001 |
| UC-AI-001 | Agentes IA | AI-001 |
| UC-CHAT-001 | Conversaciones | CHAT-001 |
| UC-ASK-001 | Consultas | ASK-001 |
| UC-ADM-001 | Administración | ADM-001 |
| UC-BILL-001 | Facturación | BILL-001 |
| UC-AUD-001 | Auditoría | AUD-001 |
| UC-INT-001 | Integraciones | INT-001 |
| UC-SEC-001 | Seguridad | SEC-001 |

---

# 19. Consideraciones

- Todos los casos de uso deben respetar el modelo de permisos definido por la organización.
- Todas las operaciones relevantes deben generar eventos de auditoría.
- Toda consulta realizada por un Agente IA debe responder utilizando únicamente información autorizada o herramientas explícitamente habilitadas.
- Los casos de uso aquí descritos constituyen la base para el diseño de pruebas funcionales, criterios de aceptación y futuras historias de usuario.