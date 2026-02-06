# LEO — AI-Powered Automation & Anomaly Detection Platform

LEO is an experimental but production-oriented platform exploring how **AI-driven reasoning**, **automation**, and **anomaly detection** can be combined into a secure, auditable, and extensible system.

This public repository serves as the **technical overview, architecture reference, and design documentation** for LEO.  
The full implementation currently lives in a **private repository (`leo-local/`)** while the project matures.

---

## Why LEO?

Modern systems expose massive operational complexity:
- logs, metrics, time-series signals
- shell-based workflows
- manual debugging and intervention

LEO explores a unified approach where:
- **natural language** can drive controlled automation
- **machine learning** can detect anomalous system behavior
- **execution is observable, auditable, and reversible**

The goal is **not** to replace engineers — but to reduce cognitive load while preserving control, safety, and traceability.

---

## High-Level Architecture

LEO is designed as a **modular, event-driven system**, with clear separation between reasoning, execution, and observability.

```
┌────────────┐
│   Client   │  (CLI / API / Future UI)
└─────┬──────┘
      │
      ▼
┌────────────────────────┐
│  Interpretation Layer  │
│  (NLP / ML / Rules)    │
└─────┬──────────────────┘
      │
      ▼
┌────────────────────────┐
│  Orchestration Engine  │
│  - execution lifecycle │
│  - run IDs & hashing   │
│  - validation          │
└─────┬──────────────────┘
      │
      ▼
┌────────────────────────┐
│  Execution Backends    │
│  - anomaly detection   │
│  - automation tasks   │
│  - future extensions  │
└─────┬──────────────────┘
      │
      ▼
┌────────────────────────┐
│ Observability & State  │
│ logs · artifacts ·     │
│ metrics · persistence  │
└────────────────────────┘
```

---

## Core Concepts

### 1. Anomaly Detection as a First-Class Service

LEO includes a dedicated anomaly detection component focused on **time-series data**, designed to support:

- real-time and batch analysis
- configurable sensitivity and thresholds
- per-run model isolation
- reproducible metrics and artifacts

The anomaly engine is designed to be **backend-agnostic**, allowing different algorithms and data sources to be plugged in without changing the orchestration layer.

---

### 2. Execution-Oriented Design

Every operation in LEO is treated as a **tracked execution**:

- unique run IDs
- deterministic run hashes
- structured logs and artifacts
- explicit success / failure states

This enables:
- auditability
- debugging
- reproducibility
- future rollback or replay mechanisms

---

### 3. Security-First Philosophy

LEO is built with the assumption that AI-driven systems **must not execute blindly**.

Design principles include:
- strict input validation
- explicit execution modes (manual vs autonomous)
- environment isolation
- secrets handled via dedicated abstractions

---

## Tech Stack (Implementation)

> Note: The following reflects the **private implementation** and may evolve.

- **Language:** Python (3.12+)
- **API Layer:** FastAPI
- **ML / Data:** NumPy, scikit-learn
- **State & Caching:** Redis
- **Testing:** pytest
- **CI/CD:** GitHub Actions
- **Execution Environment:** Containerized (Docker / Podman)

---

## Repository Structure (Public)

This repository intentionally does **not** contain the full source code.

```
leo/
├── README.md          # This document
├── docs/              # Architecture, design notes, diagrams
├── specs/             # Interface & data model specifications
└── roadmap.md         # Planned public milestones
```

The private repository (`leo-local/`) contains:
- full implementation
- test suites
- CI pipelines
- internal tooling

---

## Project Status

- 🟢 Core architecture implemented (private)
- 🟢 Anomaly detection service operational (private)
- 🟢 Execution tracking & logging implemented
- 🟡 Public documentation being expanded
- 🔒 Codebase private while stabilizing APIs and security model

---

## Roadmap (Public-Facing)

Planned future steps include:

- Publishing **API schemas and example payloads**
- Releasing **synthetic demos** without sensitive logic
- Adding **architecture diagrams and benchmarks**
- Selective open-sourcing of **non-sensitive components**

---

## Disclaimer

This repository is **not a runnable distribution**.

It exists to:
- document system design
- communicate architectural intent
- support technical discussion and evaluation

If you are interested in collaboration, research discussion, or a deeper technical walkthrough, feel free to open an issue.

---

## Author

LEO is developed and maintained by **Neri Carcasci**,  
with a focus on **trustworthy AI**, **automation**, and **production-grade ML systems**.

---

*LEO is an evolving research and engineering project. Interfaces and designs are subject to change.*
