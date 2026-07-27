# Convenciones Frontend

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Uso Interno

---

# 1. Introducción

## Objetivo

Este documento establece el estándar oficial para el desarrollo del Frontend de Nexa Knowledge AI.

Su propósito es garantizar una experiencia de usuario consistente, una base de código mantenible y una arquitectura escalable que facilite el desarrollo colaborativo.

Estas convenciones son obligatorias para todos los proyectos frontend desarrollados por NexaDigital S.A.S.

---

# 2. Principios

Todo desarrollo frontend deberá cumplir los siguientes principios:

- Simplicidad.
- Consistencia.
- Reutilización.
- Accesibilidad.
- Escalabilidad.
- Seguridad.
- Rendimiento.
- Responsividad.
- Mantenibilidad.
- Experiencia de usuario centrada en el usuario.

---

# 3. Arquitectura General

El frontend deberá organizarse mediante una arquitectura modular.

```
UI

↓

Pages

↓

Components

↓

Hooks / Composables

↓

Services

↓

API Client
```

Cada nivel tendrá una responsabilidad claramente definida.

---

# 4. Organización del Proyecto

Estructura recomendada:

```
src/

├── app/
├── assets/
├── components/
├── layouts/
├── pages/
├── routes/
├── services/
├── hooks/
├── store/
├── contexts/
├── types/
├── utils/
├── constants/
├── styles/
├── icons/
├── i18n/
└── tests/
```

La estructura podrá adaptarse al framework utilizado manteniendo la separación de responsabilidades.

---

# 5. Convenciones de Nombres

## Componentes

PascalCase

```
DocumentCard
```

```
ConversationPanel
```

---

## Hooks

Prefijo:

```
use
```

Ejemplo:

```
useAuthentication
```

```
useDocuments
```

---

## Variables

camelCase

```
currentWorkspace
```

---

## Constantes

UPPER_SNAKE_CASE

```
MAX_UPLOAD_SIZE
```

---

## Archivos

kebab-case

```
document-card.tsx
```

---

# 6. Componentes

Los componentes deberán ser:

- Pequeños.
- Reutilizables.
- Independientes.
- Fáciles de probar.

Cada componente deberá cumplir una única responsabilidad.

---

# 7. Páginas

Las páginas representan casos de uso completos.

Ejemplos:

- Inicio.
- Login.
- Dashboard.
- Gestión Documental.
- Administración.
- Configuración.
- Chat IA.

Las páginas no deberán contener lógica de negocio compleja.

---

# 8. Gestión del Estado

El estado se dividirá en:

## Estado Global

Ejemplos:

- Usuario autenticado.
- Organización activa.
- Configuración.
- Tema visual.
- Idioma.

---

## Estado Local

Ejemplos:

- Formularios.
- Modales.
- Filtros.
- Tablas.
- Componentes individuales.

Se evitará almacenar estado global innecesario.

---

# 9. Consumo de APIs

Toda comunicación con el backend deberá realizarse mediante servicios especializados.

Ejemplo:

```
DocumentService
```

```
UserService
```

Los componentes nunca consumirán APIs directamente.

---

# 10. Manejo de Errores

Todos los errores deberán gestionarse de forma uniforme.

Ejemplos:

- Error de autenticación.
- Error de permisos.
- Error de red.
- Error de validación.
- Error interno.

Los mensajes deberán ser claros y comprensibles para el usuario.

---

# 11. Diseño Responsivo

La interfaz deberá adaptarse correctamente a distintos tamaños de pantalla.

Se consideran como mínimo:

- Escritorio.
- Portátil.
- Tablet.
- Dispositivos móviles.

La funcionalidad no deberá depender exclusivamente del tamaño de pantalla.

---

# 12. Accesibilidad

La aplicación deberá cumplir buenas prácticas de accesibilidad.

Se recomienda:

- Navegación mediante teclado.
- Etiquetas accesibles.
- Contraste adecuado.
- Indicadores visuales de foco.
- Compatibilidad con lectores de pantalla.
- Uso correcto de atributos ARIA cuando sea necesario.

---

# 13. Internacionalización

La plataforma deberá permitir múltiples idiomas.

Todo texto visible deberá obtenerse desde el sistema de internacionalización.

No deberán existir cadenas de texto codificadas directamente en los componentes.

---

# 14. Rendimiento

Se recomienda:

- Lazy Loading.
- Code Splitting.
- Memoización cuando sea necesaria.
- Carga diferida de imágenes.
- Paginación.
- Virtualización para listas extensas.

El tiempo de carga deberá mantenerse al mínimo.

---

# 15. Seguridad

El frontend deberá:

- Validar entradas del usuario.
- Proteger tokens de acceso.
- Evitar exposición de información sensible.
- No almacenar secretos.
- Respetar la política de autenticación.

La autorización siempre será validada también por el backend.

---

# 16. Gestión de Sesiones

El cliente deberá gestionar correctamente:

- Inicio de sesión.
- Renovación de tokens.
- Expiración de sesión.
- Cierre de sesión.
- Cambio de organización.
- Cambio de Workspace.

Las sesiones expiradas deberán redirigir al usuario al proceso de autenticación.

---

# 17. Formularios

Todos los formularios deberán:

- Validar datos antes del envío.
- Mostrar errores específicos.
- Indicar campos obligatorios.
- Evitar envíos duplicados.
- Mostrar estados de carga.

---

# 18. Diseño Visual

Toda la interfaz deberá respetar el Design System oficial.

Se utilizarán componentes reutilizables para:

- Botones.
- Tablas.
- Formularios.
- Tarjetas.
- Diálogos.
- Menús.
- Navegación.
- Alertas.

No deberán implementarse componentes duplicados para resolver el mismo problema.

---

# 19. Pruebas

Todo desarrollo deberá incorporar pruebas.

## Unitarias

Validan componentes individuales.

---

## Integración

Comprueban la interacción entre componentes y servicios.

---

## End-to-End

Verifican el funcionamiento completo de los principales flujos del usuario.

---

# 20. Observabilidad

El frontend deberá registrar eventos relevantes, como:

- Errores inesperados.
- Excepciones de JavaScript.
- Fallos de carga.
- Errores de autenticación.
- Errores de red.

Estos registros facilitarán el diagnóstico de incidencias.

---

# 21. Optimización

Se recomienda:

- Reducir el tamaño del paquete generado.
- Eliminar dependencias innecesarias.
- Reutilizar componentes.
- Evitar renderizados repetitivos.
- Optimizar el consumo de recursos.

Las optimizaciones deberán medirse mediante herramientas de análisis de rendimiento.

---

# 22. Revisión de Código

Todo cambio deberá ser revisado antes de integrarse.

La revisión verificará:

- Cumplimiento de convenciones.
- Calidad del código.
- Accesibilidad.
- Rendimiento.
- Seguridad.
- Correcto funcionamiento de la interfaz.

---

# 23. Buenas Prácticas

- Mantener componentes pequeños.
- Favorecer la reutilización.
- Evitar lógica duplicada.
- Utilizar tipado fuerte cuando el lenguaje lo permita.
- Documentar componentes reutilizables.
- Mantener consistencia visual.
- Respetar el Design System.
- Escribir código legible y mantenible.

---

# 24. Documentos Relacionados

Este documento complementa:

- Arquitectura Técnica.
- Arquitectura de Microservicios.
- Convenciones Backend.
- Introducción API.
- Manual del Usuario.
- Gestión de Documentos.
- Política de Seguridad.
- Configuración Global.

Las Convenciones Frontend establecen el estándar oficial para el desarrollo de la interfaz de usuario de Nexa Knowledge AI, garantizando una experiencia consistente, accesible y escalable para todos los usuarios de la plataforma.