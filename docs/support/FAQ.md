# Preguntas Frecuentes (FAQ)

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Público

---

# 1. Introducción

## Objetivo

Este documento recopila las preguntas más frecuentes sobre Nexa Knowledge AI y sus respectivas respuestas.

Su propósito es facilitar la resolución de dudas comunes de usuarios, administradores y equipos de soporte, reduciendo tiempos de atención y proporcionando respuestas consistentes.

Este documento forma parte de la Base Oficial de Conocimiento del producto.

---

# 2. Información General

## ¿Qué es Nexa Knowledge AI?

Nexa Knowledge AI es una plataforma SaaS que permite consultar documentos empresariales utilizando lenguaje natural.

Los usuarios pueden hacer preguntas directamente al sistema y recibir respuestas fundamentadas en la documentación disponible.

---

## ¿Qué tipo de documentos puede procesar?

La plataforma admite diferentes tipos de documentos, entre ellos:

- PDF
- Microsoft Word
- Microsoft Excel
- PowerPoint
- Archivos de texto
- Markdown
- CSV
- Otros formatos compatibles configurados por el administrador.

---

## ¿El sistema responde utilizando Inteligencia Artificial?

Sí.

Nexa Knowledge AI utiliza una arquitectura RAG (Retrieval-Augmented Generation), que combina la recuperación de información de los documentos con modelos de lenguaje para generar respuestas fundamentadas.

---

## ¿El sistema inventa respuestas?

No debería.

Las respuestas se generan únicamente utilizando la información disponible en los documentos autorizados.

Si la información no existe o es insuficiente, el sistema indicará que no dispone de evidencia suficiente para responder.

---

# 3. Gestión de Usuarios

## ¿Cómo creo una cuenta?

Las cuentas pueden crearse:

- Por un administrador.
- Mediante invitación.
- Mediante integración con un proveedor de identidad (si está habilitado).

---

## ¿Cómo recupero mi contraseña?

Seleccione la opción **"Olvidé mi contraseña"** en la pantalla de inicio de sesión y siga las instrucciones enviadas al correo electrónico registrado.

---

## ¿Puedo cambiar mi correo electrónico?

Sí.

Siempre que la política de la organización lo permita y el usuario tenga los permisos correspondientes.

---

## ¿Cómo cierro mi sesión?

Desde el menú del perfil seleccione la opción **Cerrar sesión**.

---

# 4. Gestión de Documentos

## ¿Cómo subo un documento?

1. Acceda al Workspace correspondiente.
2. Ingrese a la sección **Documentos**.
3. Seleccione **Subir documento**.
4. Elija el archivo.
5. Espere a que finalice el procesamiento.

---

## ¿Cuánto tarda el procesamiento?

Depende de:

- Tamaño del documento.
- Cantidad de páginas.
- Complejidad del contenido.
- Carga del sistema.

En la mayoría de los casos el procesamiento se completa en pocos minutos.

---

## ¿Qué ocurre después de subir un documento?

La plataforma:

- Extrae el contenido.
- Lo normaliza.
- Lo divide en fragmentos (Chunks).
- Genera Embeddings.
- Indexa la información en la Base Vectorial.
- Habilita el documento para consultas.

---

## ¿Puedo actualizar un documento?

Sí.

Al cargar una nueva versión, la plataforma volverá a procesar e indexar el contenido.

---

## ¿Qué ocurre si elimino un documento?

El documento dejará de estar disponible para futuras consultas.

Las conversaciones anteriores no se modifican automáticamente.

---

# 5. Consultas al Agente IA

## ¿Cómo hago una pregunta?

Escriba su consulta en lenguaje natural en el chat del Agente IA.

No es necesario utilizar comandos especiales.

---

## ¿Puedo hacer preguntas complejas?

Sí.

Por ejemplo:

- Comparaciones.
- Resúmenes.
- Explicaciones.
- Procedimientos.
- Políticas.
- Información técnica.

Siempre que exista información suficiente en la documentación disponible.

---

## ¿El sistema recuerda el contexto?

Sí.

Durante una conversación el agente utiliza el historial para interpretar preguntas relacionadas.

---

## ¿Puede responder utilizando varios documentos?

Sí.

Si la información relevante se encuentra distribuida en distintos documentos, el sistema podrá combinar el contexto recuperado para generar una única respuesta.

---

## ¿Qué ocurre si la respuesta no existe?

El sistema indicará que no encontró información suficiente para responder de forma confiable.

---

# 6. Permisos

## ¿Por qué no puedo consultar ciertos documentos?

Probablemente no dispone de permisos para acceder a ellos.

El Agente IA respeta exactamente los permisos definidos por la organización.

---

## ¿Puede otro usuario acceder a mis documentos privados?

No.

El acceso siempre está condicionado por los permisos asignados.

---

## ¿Quién administra los permisos?

Los administradores de la organización.

---

# 7. Administración

## ¿Qué puede hacer un administrador?

Entre otras funciones:

- Gestionar usuarios.
- Crear Workspaces.
- Configurar colecciones.
- Asignar permisos.
- Revisar auditorías.
- Administrar la configuración global.

---

## ¿Puedo limitar el acceso a determinados documentos?

Sí.

La plataforma permite definir permisos por organización, Workspace, colección y documento.

---

# 8. Seguridad

## ¿Los documentos están protegidos?

Sí.

La plataforma implementa múltiples mecanismos de seguridad, incluyendo autenticación, autorización, cifrado y auditoría.

---

## ¿Se almacenan mis conversaciones?

Sí.

Las conversaciones pueden almacenarse para mantener el historial, facilitar auditorías y mejorar la experiencia del usuario, de acuerdo con la configuración establecida por la organización.

---

## ¿La información se comparte con otros clientes?

No.

Cada organización opera en un entorno aislado, garantizando la separación lógica de la información.

---

# 9. Integraciones

## ¿Puede conectarse con otros sistemas?

Sí.

Nexa Knowledge AI puede integrarse mediante APIs con aplicaciones corporativas y servicios externos autorizados.

---

## ¿Es posible utilizar distintos modelos de IA?

Sí.

La arquitectura permite integrar diferentes proveedores de modelos de lenguaje, según la configuración realizada por el administrador.

---

# 10. Rendimiento

## ¿Qué afecta la velocidad de respuesta?

Entre los principales factores se encuentran:

- Complejidad de la consulta.
- Cantidad de documentos.
- Tamaño del contexto recuperado.
- Carga de la infraestructura.
- Tiempo de respuesta del proveedor de IA.

---

## ¿Existe un límite de consultas?

Dependerá del plan contratado y de las políticas configuradas por la organización.

---

# 11. Soporte

## ¿Qué debo hacer si encuentro un error?

Se recomienda:

1. Registrar el problema.
2. Capturar el mensaje de error si existe.
3. Indicar los pasos realizados.
4. Contactar al equipo de soporte.

---

## ¿Cómo reporto un problema?

Los incidentes deberán reportarse utilizando los canales oficiales definidos por la organización.

Siempre que sea posible, incluya:

- Fecha y hora.
- Usuario afectado.
- Workspace.
- Documento relacionado.
- Descripción del problema.
- Evidencia (capturas o registros).

---

# 12. Preguntas Técnicas

## ¿Qué es RAG?

RAG (Retrieval-Augmented Generation) es una arquitectura que recupera información relevante desde los documentos antes de solicitar una respuesta al modelo de lenguaje.

Esto permite respuestas más precisas y fundamentadas.

---

## ¿Qué son los Embeddings?

Son representaciones vectoriales del contenido de los documentos utilizadas para realizar búsquedas semánticas.

---

## ¿Qué es una Base Vectorial?

Es un sistema especializado que almacena embeddings y permite recuperar rápidamente la información más relevante para responder una consulta.

---

## ¿Qué es un Chunk?

Es un fragmento de texto obtenido durante el procesamiento de un documento para facilitar su indexación y recuperación.

---

# 13. Buenas Prácticas

Para obtener mejores respuestas:

- Realice preguntas claras.
- Evite combinar demasiados temas en una sola consulta.
- Utilice nombres específicos de documentos cuando sea posible.
- Mantenga la documentación actualizada.
- Revise los permisos asignados.
- Espere a que finalice el procesamiento antes de consultar documentos recién cargados.

---

# 14. Documentos Relacionados

Este documento complementa:

- Manual del Usuario.
- Gestión de Documentos.
- Arquitectura RAG.
- Funcionamiento del Agente IA.
- Manual del Administrador.
- Política de Seguridad.
- Solución de Problemas.
- Términos de Uso.

La presente FAQ constituye la referencia oficial de preguntas frecuentes de Nexa Knowledge AI y forma parte de la base de conocimiento utilizada para asistir a usuarios y administradores de la plataforma.