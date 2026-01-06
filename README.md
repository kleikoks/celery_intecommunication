# Celery Microservice Communication Showcase

This repository demonstrates a simple Celery-based communication pattern between two independent services:
an **AI service** and a **Backend (BE) service**.

The services may run on different machines or containers.
The only shared requirement is a **common message broker** (Redis).

---

## Services

- **ai_service**  
  Simulates an AI worker that consumes tasks from the AI queue and responds back to the backend.

- **be_service**  
  Simulates a backend worker that produces tasks for the AI service and consumes responses.

- **runner**  
  A lightweight producer script that periodically publishes tasks  
  (acts as a simplified alternative to Celery Beat).

---

## Architecture Overview

- Each service runs its **own Celery application**
- Task names are **globally unique and namespaced** (`ai.*`, `be.*`)
- Tasks are routed using `task_routes`
- Workers consume **explicitly bound queues**
- Communication is **asynchronous and bidirectional**

---

## Message Flow

1. The **runner** publishes a `be.produce_message` task.
2. The **BE service** receives the task and sends an `ai.consume_message` task.
3. The **AI service** processes the message and sends message an `be.consume_message`.
4. The **BE service** precesses the task.

---

## Key Celery Concepts Demonstrated

- Multiple Celery apps sharing a broker
- Explicit task routing via `task_routes`
- Queue isolation per service
- Cross-service task invocation using `send_task`
- Worker queue binding via `-Q`

---

## Broker

- **Redis** is used as the message broker
- Services communicate exclusively through queues
