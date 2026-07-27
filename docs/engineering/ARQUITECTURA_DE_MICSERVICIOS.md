# Arquitectura de Microservicios

**Producto:** Nexa Knowledge AI

**Empresa:** NexaDigital S.A.S.

**Versión del documento:** 1.0

**Estado:** Vigente

**Clasificación:** Uso Interno

---

# 1. Introducción

## Objetivo

Este documento define la arquitectura de microservicios utilizada por Nexa Knowledge AI.

Describe la organización de los servicios, sus responsabilidades, la comunicación entre ellos y los principios que permiten construir una plataforma distribuida, escalable y resiliente.

---

# 2. Objetivos de la Arquitectura

La arquitectura de microservicios busca:

- Desacoplar los dominios funcionales.
- Permitir despliegues independientes.
- Escalar servicios de forma individual.
- Reducir el impacto de fallos.
- Facilitar el mantenimiento.
- Mejorar la disponibilidad.
- Acelerar la evolución del producto.

---

# 3. Principios de Diseño

Todos los microservicios deberán respetar los siguientes principios:

- Una única responsabilidad por servicio.
- Base de datos privada por servicio cuando aplique.
- Comunicación mediante contratos bien definidos.
- Independencia tecnológica.
- Despliegue autónomo.
- Observabilidad integrada.
- Tolerancia a fallos.
- Seguridad desde el diseño.

---

# 4. Vista General

```
                    Clientes

                        │
                        ▼
                 API Gateway
                        │
 ┌──────────────────────────────────────────┐
 │                                          │
 ▼                                          ▼
Auth Service                         User Service
 │                                          │
 └──────────────┐                   ┌────────┘
                ▼                   ▼
          Organization Service
                │
                ▼
         Workspace Service
                │
                ▼
         Collection Service
                │
                ▼
          Document Service
                │
                ▼
        Processing Service
                │
                ▼
         Embedding Service
                │
                ▼
         Vector Search Service
                │
                ▼
            AI Service
                │
                ▼
      Conversation Service

                │
                ▼
        Audit Service
```

---

# 5. Microservicios Principales

## Auth Service

Responsable de:

- Autenticación.
- Emisión de tokens.
- Renovación de sesiones.
- Integración con proveedores de identidad.
- MFA.

No almacena información documental.

---

## User Service

Gestiona:

- Usuarios.
- Perfiles.
- Roles.
- Preferencias.
- Estado de cuentas.

Expone APIs relacionadas con la identidad del usuario.

---

## Organization Service

Administra:

- Organizaciones.
- Configuración empresarial.
- Licencias.
- Suscripciones.

Garantiza el aislamiento entre clientes.

---

## Workspace Service

Gestiona:

- Workspaces.
- Configuración.
- Miembros.
- Accesos.

Cada Workspace representa un espacio independiente de trabajo.

---

## Collection Service

Responsable de:

- Colecciones.
- Organización documental.
- Configuración de acceso.
- Clasificación.

---

## Document Service

Gestiona:

- Carga.
- Versiones.
- Metadatos.
- Eliminación.
- Descarga.
- Historial.

No realiza procesamiento de IA.

---

## Processing Service

Procesa documentos.

Responsabilidades:

- Extracción.
- OCR (cuando aplique).
- Limpieza.
- Normalización.
- Conversión.

---

## Embedding Service

Responsable de:

- Chunking.
- Embeddings.
- Reindexación.
- Actualización de vectores.

No interactúa directamente con usuarios finales.

---

## Vector Search Service

Gestiona:

- Base Vectorial.
- Recuperación semántica.
- Ranking.
- Búsqueda híbrida (si está habilitada).

---

## AI Service

Implementa:

- Orquestación RAG.
- Construcción de prompts.
- Comunicación con LLM.
- Generación de respuestas.

Es el núcleo funcional de la Inteligencia Artificial.

---

## Conversation Service

Gestiona:

- Conversaciones.
- Historial.
- Contexto.
- Mensajes.

---

## Audit Service

Registra:

- Eventos.
- Acciones administrativas.
- Cambios críticos.
- Consultas relevantes.

---

# 6. Comunicación entre Servicios

La plataforma utiliza dos mecanismos principales.

## Comunicación síncrona

Mediante APIs REST internas.

Se utiliza cuando la respuesta es inmediata.

Ejemplos:

- Consultar usuarios.
- Obtener documentos.
- Validar permisos.

---

## Comunicación asíncrona

Mediante eventos y colas.

Se utiliza para:

- Procesamiento documental.
- Reindexación.
- Envío de correos.
- Auditoría.
- Notificaciones.

---

# 7. Eventos del Sistema

Ejemplos de eventos publicados:

```
UserCreated
```

```
UserUpdated
```

```
DocumentUploaded
```

```
DocumentProcessed
```

```
EmbeddingsGenerated
```

```
DocumentIndexed
```

```
ConversationCreated
```

```
AgentResponseGenerated
```

Cada evento deberá contener:

- Identificador.
- Fecha.
- Servicio origen.
- Versión.
- Datos del evento.

---

# 8. API Gateway

Todas las solicitudes externas ingresan por el API Gateway.

Funciones:

- Autenticación.
- Validación inicial.
- Rate Limiting.
- Balanceo.
- Enrutamiento.
- Observabilidad.

Los clientes nunca acceden directamente a los microservicios.

---

# 9. Base de Datos por Servicio

Siempre que sea posible, cada microservicio administrará su propio almacenamiento.

Beneficios:

- Bajo acoplamiento.
- Independencia.
- Escalabilidad.
- Evolución autónoma.

El acceso directo a la base de otro servicio está prohibido.

---

# 10. Patrones Arquitectónicos

## API Gateway

Punto único de entrada para clientes.

---

## Saga

Coordina operaciones distribuidas que afectan varios servicios.

Se recomienda para procesos como:

- Creación de organizaciones.
- Aprovisionamiento inicial.
- Eliminación de recursos relacionados.

---

## Outbox Pattern

Garantiza la publicación consistente de eventos después de una transacción.

Evita pérdida de mensajes.

---

## Circuit Breaker

Protege la plataforma frente a fallos repetitivos en servicios externos.

Cuando un servicio deja de responder, el Circuit Breaker evita nuevas llamadas hasta que el servicio se recupere.

---

## Retry Pattern

Permite reintentar automáticamente operaciones temporales que fallan por causas transitorias.

Debe utilizar retroceso exponencial.

---

## Health Checks

Cada servicio deberá publicar:

```
/health
```

y

```
/ready
```

para facilitar la supervisión y el despliegue.

---

## Service Discovery

Los servicios deberán localizarse dinámicamente mediante mecanismos de descubrimiento o configuración centralizada.

No deberán utilizar direcciones IP fijas.

---

# 11. Seguridad

Toda comunicación entre servicios deberá:

- Utilizar canales seguros.
- Autenticarse.
- Autorizarse cuando corresponda.
- Registrarse.
- Validarse.

Nunca se confiará únicamente en la red interna.

---

# 12. Observabilidad

Cada microservicio deberá generar:

- Logs estructurados.
- Métricas.
- Trazas distribuidas.
- Eventos de auditoría.

Esto permitirá identificar rápidamente problemas de rendimiento y disponibilidad.

---

# 13. Escalabilidad

Cada servicio podrá escalar horizontalmente de manera independiente.

Ejemplos:

- El AI Service puede aumentar réplicas cuando crece el número de consultas.
- El Processing Service puede escalar durante cargas masivas de documentos.
- El Vector Search Service puede ampliarse para soportar más búsquedas simultáneas.

---

# 14. Tolerancia a Fallos

Los servicios deberán diseñarse para continuar operando ante fallos parciales.

Se recomienda:

- Timeouts.
- Retries controlados.
- Circuit Breakers.
- Colas persistentes.
- Reintentos diferidos.
- Operaciones idempotentes.

---

# 15. Despliegue

Cada microservicio deberá:

- Construirse de forma independiente.
- Versionarse individualmente.
- Desplegarse sin afectar a otros servicios.
- Mantener compatibilidad con los contratos existentes.

---

# 16. Evolución

La incorporación de nuevos microservicios deberá seguir estos principios:

- No romper contratos existentes.
- Publicar eventos versionados.
- Mantener compatibilidad hacia atrás.
- Documentar nuevos endpoints.
- Actualizar la arquitectura técnica.

---

# 17. Relación con otros documentos

Este documento complementa:

- Arquitectura Técnica.
- Arquitectura RAG.
- Introducción API.
- Convenciones Backend.
- Convenciones Frontend.
- Infraestructura.
- Política de Seguridad.
- Configuración Global.
- Manual del Administrador.

La Arquitectura de Microservicios establece la organización oficial de los componentes distribuidos de Nexa Knowledge AI y define los principios técnicos que garantizan una plataforma escalable, resiliente y preparada para evolucionar conforme crezcan las necesidades del producto y de sus clientes.