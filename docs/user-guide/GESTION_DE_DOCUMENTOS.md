# Gestión de Documentos

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

---

# 1. Introducción

## Objetivo

Este documento describe el ciclo de vida completo de los documentos dentro de Nexa Knowledge AI, desde su carga hasta su eliminación.

Está dirigido a usuarios con permisos para administrar documentos dentro de la plataforma y constituye la referencia oficial para la gestión documental.

---

# 2. ¿Qué es un documento?

Un documento es cualquier archivo incorporado a la Base de Conocimiento de Nexa Knowledge AI para que pueda ser procesado, indexado y consultado mediante Inteligencia Artificial.

Los documentos representan la principal fuente de conocimiento utilizada por los Agentes IA para responder preguntas.

---

# 3. Requisitos

Antes de cargar un documento, verifique que:

- Pertenece al Workspace correcto.
- Dispone de permisos para crear documentos.
- El archivo corresponde a información autorizada por la organización.
- El contenido se encuentra actualizado.
- No contiene información cuya carga esté restringida por las políticas internas.

---

# 4. Ciclo de vida de un documento

Todo documento sigue el siguiente flujo dentro de la plataforma:

```
Carga

↓

Validación

↓

Procesamiento

↓

Extracción de contenido

↓

Indexación

↓

Disponible para consultas

↓

Actualización (opcional)

↓

Nueva indexación

↓

Archivo o eliminación
```

---

# 5. Crear un documento

## Paso 1

Acceda al Workspace correspondiente.

---

## Paso 2

Seleccione la colección donde desea almacenar el documento.

---

## Paso 3

Seleccione **Nuevo documento**.

---

## Paso 4

Cargue el archivo desde su equipo.

---

## Paso 5

Complete los metadatos cuando corresponda.

Ejemplos:

- Nombre
- Descripción
- Etiquetas
- Categoría
- Autor
- Idioma

---

## Paso 6

Confirme la carga.

La plataforma iniciará automáticamente el procesamiento.

---

# 6. Procesamiento del documento

Después de la carga, Nexa Knowledge AI ejecuta automáticamente las siguientes tareas:

1. Validación del archivo.
2. Extracción del contenido.
3. Limpieza del texto.
4. División en fragmentos (Chunking).
5. Generación de embeddings.
6. Indexación en la Base Vectorial.
7. Actualización de la Base de Conocimiento.

El documento solo estará disponible cuando todas las etapas finalicen correctamente.

---

# 7. Estados del documento

Cada documento puede encontrarse en uno de los siguientes estados.

| Estado | Descripción |
|---------|-------------|
| Cargando | El archivo está siendo transferido. |
| Procesando | El contenido está siendo analizado. |
| Indexando | Se generan embeddings y se almacena el conocimiento. |
| Disponible | Puede responder consultas. |
| Error | Ocurrió un problema durante el procesamiento. |
| Archivado | Ya no participa en las consultas, pero permanece almacenado. |
| Eliminado | El documento ha sido eliminado según las políticas vigentes. |

---

# 8. Actualizar un documento

Cuando un documento cambia:

1. Abra el documento.
2. Seleccione **Actualizar**.
3. Cargue la nueva versión.
4. Confirme la operación.

El sistema iniciará nuevamente el proceso de indexación.

Mientras se procesa la nueva versión, la plataforma podrá continuar utilizando la versión anterior hasta completar la actualización, según la configuración de la organización.

---

# 9. Versionado

Cada actualización genera una nueva versión del documento.

El historial puede incluir:

- Número de versión.
- Fecha.
- Usuario responsable.
- Descripción del cambio.
- Estado.

El versionado facilita la trazabilidad y la recuperación de información.

---

# 10. Organización mediante colecciones

Se recomienda organizar los documentos utilizando colecciones temáticas.

Ejemplos:

## Recursos Humanos

- Políticas
- Contratos
- Beneficios

---

## Ingeniería

- Arquitectura
- Manuales
- APIs
- Procedimientos

---

## Comercial

- Planes
- Contratos
- Presentaciones

---

# 11. Metadatos

Los metadatos facilitan la organización y búsqueda del contenido.

Ejemplos:

- Autor.
- Departamento.
- Fecha de creación.
- Fecha de actualización.
- Tipo de documento.
- Estado.
- Etiquetas.
- Idioma.
- Nivel de confidencialidad.

Mantener estos datos actualizados mejora la precisión de las búsquedas.

---

# 12. Búsqueda de documentos

Los documentos pueden localizarse utilizando:

- Nombre.
- Etiquetas.
- Categoría.
- Autor.
- Fecha.
- Colección.
- Workspace.
- Contenido.
- Similitud semántica.

La búsqueda semántica permite encontrar información incluso cuando no coinciden exactamente las palabras utilizadas.

---

# 13. Eliminación de documentos

Para eliminar un documento:

1. Abra el documento.
2. Seleccione **Eliminar**.
3. Confirme la operación.

Dependiendo de la configuración de la organización, la eliminación podrá ser:

- Lógica.
- Física.
- Programada.
- Sujeta a un período de retención.

---

# 14. Restauración

Cuando las políticas lo permitan, un documento eliminado de forma lógica podrá restaurarse.

La restauración recuperará:

- El documento.
- Sus metadatos.
- Su historial de versiones.

La disponibilidad inmediata para consultas dependerá de si es necesario ejecutar una nueva indexación.

---

# 15. Impacto sobre los Agentes IA

Los Agentes IA únicamente responderán utilizando documentos que:

- Estén disponibles.
- Hayan sido indexados correctamente.
- Sean accesibles para el usuario.
- Pertenezcan al ámbito autorizado de la consulta.

Los documentos en proceso o con errores no se utilizarán para generar respuestas.

---

# 16. Buenas prácticas

Para mantener una Base de Conocimiento de alta calidad se recomienda:

- Utilizar nombres descriptivos.
- Evitar documentos duplicados.
- Mantener la información actualizada.
- Eliminar versiones obsoletas cuando corresponda.
- Organizar adecuadamente las colecciones.
- Completar los metadatos.
- Revisar periódicamente los documentos más consultados.
- Validar el contenido antes de publicarlo.

---

# 17. Problemas frecuentes

## El documento no aparece en las consultas

Posibles causas:

- Todavía se encuentra procesándose.
- El procesamiento finalizó con errores.
- El usuario no dispone de permisos.
- El documento pertenece a otro Workspace.
- El Agente IA no tiene acceso a la colección correspondiente.

---

## La respuesta utiliza una versión antigua

Es posible que la nueva versión aún esté indexándose.

Espere a que finalice el procesamiento antes de realizar nuevas consultas.

---

## El archivo fue rechazado

Verifique:

- Formato compatible.
- Integridad del archivo.
- Tamaño permitido.
- Restricciones definidas por la organización.

---

# 18. Preguntas frecuentes

## ¿Puedo modificar un documento directamente?

No.

Las modificaciones se realizan cargando una nueva versión.

---

## ¿Qué ocurre si elimino un documento?

Dejará de utilizarse para responder consultas una vez aplicada la política de eliminación correspondiente.

---

## ¿Los Agentes IA responden inmediatamente después de cargar un documento?

No.

Primero debe finalizar correctamente el proceso de procesamiento e indexación.

---

## ¿Puedo organizar un mismo documento en varias colecciones?

Dependerá de la configuración de la organización y de las capacidades habilitadas para la plataforma.

---

## ¿Quién puede eliminar documentos?

Únicamente los usuarios con los permisos correspondientes.

---

# 19. Relación con otros documentos

Este documento complementa:

- Manual del Usuario.
- Gestión de Workspaces.
- Gestión de Colecciones.
- Modelo de Permisos.
- Reglas de Negocio.
- Arquitectura Funcional.
- Base de Conocimiento del Producto.
- Arquitectura RAG.

La correcta gestión documental es fundamental para garantizar que los Agentes IA proporcionen respuestas precisas, actualizadas y respaldadas por información confiable.