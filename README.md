# Alive Todo

A calm asynchronous AI companion powered by local language models.

Alive Todo is not a task manager, productivity tracker, or autonomous agent framework. It is an experiment in building a persistent cognitive companion that can remember context, adapt its interaction style, and continue thinking in the background while a conversation evolves.

The project explores a different interaction model for AI systems: less focused on maximizing output, and more focused on maintaining continuity, reflection, and gentle guidance over time.

---

## Core Concepts

### Persistent Cognitive State

Instead of storing a simple chat history, Alive Todo maintains a lightweight cognitive state:

* Current focus
* Energy state
* Recent topics
* Active tasks
* Completed thoughts

This state is persisted locally and influences future interactions.

### Interaction Modes

The assistant adapts its behavior based on conversational signals.

Current modes include:

* `gentle_start`
* `focus_flow`
* `low_energy`
* `reflection`
* `default`

Modes affect response style and guidance without changing the assistant's core personality.

### Asynchronous Cognition

Some conversations trigger background thinking.

Rather than responding immediately, Alive Todo can create an asynchronous task and continue the conversation while a worker processes the thought in the background.

Example:

```text
You: deep queue worker architecture

Alive: aku pikirin dulu ya... [task #1]

...

Alive (async) [task #1]:
Queue worker architecture biasanya terdiri dari...
```

This creates a sense of temporal continuity rather than instant completion.

### Context Snapshots

Background tasks receive immutable contextual snapshots containing:

* Current focus
* Recent topics
* Energy state

This allows asynchronous reasoning to remain grounded in the conversational context that existed when the task was created.

### Semantic Task Routing

Not all thoughts are equal.

Alive Todo classifies asynchronous tasks into semantic categories such as:

* Technical design
* Emotional reflection
* Creative exploration
* General reflection

Task type influences prompting and reasoning strategy.

---

## Architecture

```text
User
 │
 ▼
Main Loop
 │
 ├── Mode Detection
 ├── Memory Updates
 ├── Task Routing
 │
 ▼
Task Queue
 │
 ▼
Worker Thread
 │
 ├── Context Snapshot
 ├── Semantic Prompting
 │
 ▼
LLM Runtime (Ollama)
 │
 ▼
Completed Tasks
 │
 ▼
Main Loop
 │
 ▼
Memory Lifecycle Update
```

The main loop remains the single authority for application state.

Workers do not directly modify memory.

---

## Current Features

* Local LLM integration through Ollama
* Persistent memory system
* Cognitive state model
* Interaction mode engine
* Background task queue
* Async thought processing
* Context snapshots
* Semantic task routing
* Task lifecycle tracking

---

## Technology Stack

* Python 3
* Ollama
* Qwen 2.5
* JSON-based local persistence
* Threaded task processing

---

## Project Structure

```text
app/
├── config/
├── llm/
├── memory/
├── modes/
├── queue/
├── tasks/
└── main.py
```

---

## Running

Start Ollama:

```bash
ollama serve
```

Ensure the model is available:

```bash
ollama pull qwen2.5:7b
```

Run the application:

```bash
python -m app.main
```

---

## Design Principles

### Local First

The system is designed to run entirely on local infrastructure.

### Calm by Default

The assistant should reduce pressure rather than increase it.

### Explicit State

Important cognitive information should exist as structured state rather than hidden prompt history.

### Event-Driven Thinking

Long-running thoughts should be represented as asynchronous events instead of blocking interactions.

### Incremental Complexity

Features are introduced gradually and validated through real interaction before additional abstraction is added.

---

## Roadmap

### Memory

* [x] Persistent memory
* [x] Cognitive state redesign
* [ ] Memory summarization
* [ ] Long-term memory retrieval

### Orchestration

* [x] Async queue
* [x] Task lifecycle tracking
* [x] Context snapshots
* [x] Semantic task routing
* [ ] Task prioritization
* [ ] Multiple worker support

### Interaction

* [x] Interaction modes
* [ ] Reflection sessions
* [ ] Daily check-ins
* [ ] Conversation summarization

### Runtime

* [x] Ollama integration
* [ ] Model abstraction layer
* [ ] Streaming responses
* [ ] Runtime metrics

---

## Status

Early experimental prototype.

The project currently focuses on architecture exploration, conversational continuity, and asynchronous cognition rather than production deployment.
