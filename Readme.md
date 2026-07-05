# Maatri AI

## Safe Multi-Agent Maternal Healthcare Assistant

Maatri AI is a bilingual (English + Hindi) multi-agent maternal healthcare assistant built using Google ADK, Gemini, FastAPI, FAISS, and React.

The system combines Retrieval-Augmented Generation (RAG), conversation memory, Model Context Protocol (MCP), and intelligent agent routing to provide grounded, medically-safe answers for pregnancy and maternal healthcare questions.

---

## Features

- English Maternal Healthcare Agent
- Hindi Maternal Healthcare Agent
- Google ADK Multi-Agent Planner
- Retrieval-Augmented Generation (RAG)
- FAISS Semantic Search
- Cross Encoder Re-ranking
- Conversation Memory
- MCP Server
- FastAPI Backend
- React Frontend
- Gemini Integration
- Query Rewriting
- Source Attribution
- Safety-first Medical Responses

---

## Tech Stack

Backend

- Python
- FastAPI
- Google ADK
- Gemini
- MCP
- FAISS
- Sentence Transformers
- Cross Encoder

Frontend

- React
- Vite
- TailwindCSS

Models

- multilingual-e5
- Cross Encoder
- Gemini 2.5 Flash

---

## Project Structure

---

## Running Locally

### Backend

```bash
cd backend

pip install -r requirements.txt

python main.py
```

### Frontend
```bash
cd frontend

npm install

npm run dev
```
### Docker
```bash
docker compose up --build
```
### Future Impprovements 
- Larger medical knowledge base
- Medical citation ranking
- Voice interaction
- Doctor handoff
- Deployment on GCP
