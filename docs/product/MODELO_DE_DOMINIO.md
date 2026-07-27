# Modelo de Dominio

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión:** 1.0

---

# 1. Introducción

## Objetivo

El Modelo de Dominio define las entidades de negocio que conforman Nexa Knowledge AI, sus atributos principales, responsabilidades y relaciones.

Este documento representa el lenguaje oficial del negocio y sirve como referencia para:

- Desarrollo de software
- Arquitectura
- Diseño de APIs
- Modelado de bases de datos
- Integraciones
- Documentación
- Inteligencia Artificial
- Soporte

Toda funcionalidad implementada en la plataforma debe estar alineada con este modelo.

---

# 2. Principios del Modelo

El modelo de dominio sigue los principios de Domain-Driven Design (DDD).

Cada entidad representa un concepto del negocio.

Las entidades:

- poseen identidad propia
- tienen un ciclo de vida
- contienen reglas de negocio
- mantienen relaciones con otras entidades

---

# 3. Entidades del Dominio

```
Organización
│
├── Usuarios
│
├── Workspaces
│      │
│      ├── Colecciones
│      │        │
│      │        └── Documentos
│      │                  │
│      │                  ├── Fragmentos
│      │                  └── Embeddings
│      │
│      ├── Asistentes IA
│      │
│      └── Conversaciones
│                │
│                ├── Consultas
│                └── Respuestas
│
└── Suscripción
```

---

# 4. Organización

## Descripción

Representa una empresa cliente dentro de Nexa Knowledge AI.

Toda la información pertenece a una única organización.

## Responsabilidades

- administrar usuarios
- administrar licencias
- definir políticas
- controlar almacenamiento
- administrar Workspaces

## Atributos

- id
- nombre
- dominio
- estado
- plan
- configuración
- fecha de creación

---

# 5. Usuario

Representa una persona autenticada en la plataforma.

## Responsabilidades

- acceder al sistema
- consultar documentos
- gestionar recursos autorizados
- interactuar con asistentes IA

## Atributos

- id
- nombre
- correo
- contraseña
- estado
- idioma
- zona horaria

---

# 6. Rol

Define el conjunto de permisos asignados a un usuario.

Roles predeterminados

- Super Administrador
- Administrador
- Supervisor
- Editor
- Colaborador
- Lector

Cada organización puede definir roles personalizados.

---

# 7. Permiso

Representa una autorización sobre un recurso.

Ejemplos

- Leer documentos
- Crear documentos
- Eliminar documentos
- Administrar usuarios
- Crear asistentes IA
- Exportar conversaciones

Los permisos pueden heredarse.

---

# 8. Workspace

Es un espacio lógico de trabajo.

Cada Workspace organiza conocimiento relacionado.

Ejemplos

- RRHH
- Ingeniería
- Comercial
- Marketing
- Legal

## Contiene

- documentos
- colecciones
- asistentes
- conversaciones
- usuarios

---

# 9. Colección

Agrupa documentos relacionados.

Ejemplos

- Manuales
- Contratos
- Procedimientos
- Políticas

Las colecciones simplifican la administración del conocimiento.

---

# 10. Documento

Representa cualquier archivo procesable por la plataforma.

Puede encontrarse en diferentes estados.

Estados

- Pendiente
- Procesando
- Disponible
- Error
- Archivado

## Tipos soportados

- PDF
- DOCX
- XLSX
- PPTX
- TXT
- MD
- HTML
- CSV

## Metadatos

- autor
- versión
- idioma
- etiquetas
- tamaño
- fecha

---

# 11. Fragmento

Representa una porción del contenido de un documento.

Los documentos son divididos en múltiples fragmentos para optimizar la recuperación de información.

Cada fragmento mantiene una referencia a su documento original.

---

# 12. Embedding

Representa la codificación vectorial de un fragmento.

Los embeddings permiten realizar búsquedas semánticas.

Cada fragmento posee un embedding asociado.

---

# 13. Base de Conocimiento

Es el conjunto organizado de toda la información procesada.

Incluye

- documentos
- fragmentos
- embeddings
- metadatos
- relaciones

Es el origen de toda respuesta generada por IA.

---

# 14. Asistente IA

Representa un agente especializado.

Cada asistente puede estar configurado para responder únicamente sobre un subconjunto del conocimiento.

## Configuración

- nombre
- descripción
- instrucciones
- modelo
- temperatura
- herramientas
- colecciones autorizadas

---

# 15. Conversación

Representa una sesión entre un usuario y un asistente.

Una conversación contiene múltiples consultas.

Cada conversación mantiene su contexto.

---

# 16. Consulta

Representa una pregunta realizada por el usuario.

Incluye

- texto
- fecha
- usuario
- contexto
- filtros
- asistente

---

# 17. Respuesta

Representa la información generada por la IA.

Puede incluir

- texto
- referencias
- fuentes
- confianza
- tiempo de respuesta

---

# 18. Fuente

Representa un documento utilizado para construir una respuesta.

Puede contener

- documento
- página
- sección
- fragmento

Una respuesta puede utilizar múltiples fuentes.

---

# 19. Modelo IA

Representa un proveedor de Inteligencia Artificial.

Ejemplos

- GPT
- Claude
- Gemini
- Llama

Cada asistente puede utilizar un modelo diferente.

---

# 20. Proveedor de Embeddings

Representa el modelo encargado de generar representaciones vectoriales.

Ejemplos

- OpenAI Embeddings
- Gemini Embeddings
- BGE
- E5

---

# 21. Base Vectorial

Almacena los embeddings.

Implementaciones homologadas

- Pinecone
- Qdrant

Su responsabilidad es recuperar los fragmentos más relevantes para una consulta.

---

# 22. Suscripción

Representa el contrato comercial de una organización.

Incluye

- plan
- almacenamiento
- usuarios máximos
- consultas IA
- asistentes permitidos
- fecha de renovación

---

# 23. Auditoría

Representa los eventos relevantes del sistema.

Ejemplos

- inicio de sesión
- carga de documentos
- eliminación
- cambios de permisos
- consultas IA

---

# 24. Relaciones del Dominio

Una Organización posee múltiples Usuarios.

Una Organización posee múltiples Workspaces.

Un Workspace contiene múltiples Colecciones.

Una Colección contiene múltiples Documentos.

Un Documento contiene múltiples Fragmentos.

Cada Fragmento posee un Embedding.

Una Base Vectorial almacena múltiples Embeddings.

Un Asistente consulta la Base de Conocimiento.

Una Conversación pertenece a un Usuario.

Una Conversación contiene múltiples Consultas.

Cada Consulta produce una Respuesta.

Una Respuesta puede utilizar múltiples Fuentes.

---

# 25. Reglas de Negocio

Las siguientes reglas son obligatorias.

- Ningún usuario puede acceder a documentos de otra organización.
- Todo documento pertenece a una única colección.
- Todo documento pertenece a un único Workspace.
- Todo Workspace pertenece a una única organización.
- Todo embedding pertenece a un único fragmento.
- Ningún asistente puede acceder a colecciones no autorizadas.
- Toda respuesta debe originarse en información disponible dentro de la Base de Conocimiento o en herramientas explícitamente autorizadas.
- Toda consulta debe quedar asociada a una conversación.
- Toda conversación pertenece a un único usuario.
- Toda organización debe tener al menos un administrador.

---

# 26. Lenguaje Ubicuo

Los siguientes términos constituyen el vocabulario oficial de Nexa Knowledge AI.

- Organización
- Workspace
- Colección
- Documento
- Fragmento
- Embedding
- Base de Conocimiento
- Asistente IA
- Conversación
- Consulta
- Respuesta
- Fuente
- Modelo IA
- Base Vectorial
- Suscripción
- Auditoría

Todos los documentos, APIs, interfaces y manuales deberán utilizar esta terminología de forma consistente.