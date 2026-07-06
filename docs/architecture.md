# Maatri AI Architecture

Maatri AI is a bilingual, multi-agent maternal healthcare assistant built using Google Agent Development Kit (ADK), Retrieval-Augmented Generation (RAG), FastAPI, React, and Gemini.

The system follows a modular architecture where specialized agents collaborate to provide safe, grounded, and explainable healthcare responses.

---

# Overall System Architecture

```mermaid
flowchart LR

U[User]

U --> FE[React Frontend]

FE --> API[FastAPI Backend]

API --> Planner[Planner Agent]

Planner --> Language[Language Detection]

Planner --> Risk[Risk Assessment]

Planner --> Intent[Intent Classification]

Language --> EN[English Agent]

Language --> HI[Hindi Agent]

Intent --> Nutrition[Nutrition Agent]

Intent --> Emergency[Emergency Agent]

EN --> Memory[Conversation Memory]

HI --> Memory

Memory --> Rewrite[Query Rewriter]

Rewrite --> Retrieve[Hybrid Retrieval]

Retrieve --> FAISS[FAISS Vector Search]

FAISS --> CE[Cross Encoder Reranker]

CE --> Gemini[Gemini Generator]

Gemini --> Fallback[Local BART Summarizer]

Fallback --> Evidence[Evidence Synthesizer]

Evidence --> Response[Grounded Response]

Response --> Explain[Explainability Panel]

Explain --> FE
```

---

# Planner Workflow

The Planner Agent orchestrates the entire system.

```mermaid
flowchart TD

Query[User Query]

Query --> Language

Language --> Risk

Risk --> Intent

Intent --> Planner

Planner --> English

Planner --> Hindi

Planner --> Nutrition

Planner --> Emergency
```

---

# English RAG Pipeline

```mermaid
flowchart TD

Question

Question --> History

History --> Rewrite

Rewrite --> Embed

Embed --> FAISS

FAISS --> Rerank

Rerank --> Context

Context --> Gemini

Gemini --> Final
```

---

# Hindi RAG Pipeline

```mermaid
flowchart TD

Question

Question --> History

History --> Rewrite

Rewrite --> Embed

Embed --> HindiFAISS

HindiFAISS --> HindiCrossEncoder

HindiCrossEncoder --> Gemini

Gemini --> Final
```

---

# Generation Pipeline

The system prioritizes cloud-based generation while providing graceful degradation when cloud APIs are unavailable.

```mermaid
flowchart TD

Evidence

Evidence --> Gemini

Gemini --> Success

Gemini --> Failure

Failure --> LocalBART

LocalBART --> Success2

LocalBART --> Failure2

Failure2 --> EvidenceSummary
```

---

# Explainability Pipeline

Every answer returned by Maatri includes execution metadata.

```mermaid
flowchart TD

UserQuery

UserQuery --> Planner

Planner --> Retrieval

Retrieval --> Generation

Generation --> Metadata

Metadata --> ExplainabilityPanel
```

The Explainability Panel displays:

- Active Agent
- Language
- Risk Assessment
- Query Rewrite
- Retrieved Documents
- Source Distribution
- Retrieval Latency
- Generator Used
- Conversation Memory
- Execution Timeline

---

# Agent Responsibilities

## Planner Agent

Responsible for coordinating the complete workflow.

Responsibilities:

- Language Detection
- Risk Assessment
- Intent Classification
- Agent Routing

---

## Health Agent

Handles general pregnancy-related health queries.

Examples:

- Morning sickness
- Fever
- Swollen feet
- Exercise
- Medication

---

## Nutrition Agent

Specializes in maternal nutrition.

Examples:

- Fruits
- Vegetables
- Protein
- Iron
- Calcium
- Coffee
- Milk

---

## Emergency Agent

Detects high-risk maternal conditions requiring urgent attention.

Examples:

- Heavy bleeding
- Severe abdominal pain
- High fever
- Reduced fetal movement

---

# Retrieval Strategy

The retrieval pipeline combines dense semantic search with neural reranking.

1. Query rewriting using conversation history.
2. Sentence embedding generation.
3. FAISS semantic retrieval.
4. Cross Encoder reranking.
5. Top-k evidence selection.
6. Grounded response generation.

---

# Safety Mechanisms

Maatri incorporates multiple safety layers.

- Grounded Retrieval-Augmented Generation
- Medical evidence only
- Risk assessment agent
- Safety-focused prompting
- Conversation memory
- Source attribution
- Medical disclaimer
- Local fallback summarization
- Explainability metadata

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | React + Vite + TailwindCSS |
| Backend | FastAPI |
| Multi-Agent | Google ADK |
| LLM | Gemini 2.5 Flash |
| Retrieval | FAISS |
| Embeddings | Sentence Transformers |
| Reranking | Cross Encoder |
| Memory | Session-based Conversation Store |
| Explainability | Custom Metadata Pipeline |
| Fallback | DistilBART Summarizer |
| Protocol | Model Context Protocol (MCP) |