# SemantiCache

A real-time semantic caching and cost-optimization gateway for LLM applications.

## Week 1 Status: Infrastructure Skeleton

This week sets up the three core services and proves they can talk to each other:
- **FastAPI** - the backend API
- **Redis** - will be used for caching (Week 3+)
- **PostgreSQL + pgvector** - will be used for storing embeddings (Week 3+)

No caching or ML logic yet - that starts in Week 2-3.

## How to Run This

Make sure Docker Desktop is installed and running, then from the project root:

```bash
docker compose up --build
```

Wait until you see logs from all three containers (backend, redis, postgres).
First run takes a few minutes (downloading images) - after that it's much faster.

## How to Verify It's Working

Open your browser and go to:

```
http://localhost:8000/
```

You should see:
```json
{"message": "SemantiCache backend is running"}
```

Then go to:

```
http://localhost:8000/health
```

You should see:
```json
{"redis": "connected", "postgres": "connected"}
```

**If both say "connected" - Week 1 is done. Your full stack is wired up correctly.**

## Stopping Everything

Press `Ctrl + C` in the terminal, then run:

```bash
docker compose down
```

## Project Structure

```
semanticache/
├── docker-compose.yml       # defines all 3 services
├── backend/
│   ├── Dockerfile            # how to build the FastAPI container
│   ├── requirements.txt      # Python dependencies
│   └── app/
│       └── main.py           # the actual API code
├── .gitignore
└── README.md
```

## Next Steps (Week 2)

- Install Ollama and run local LLMs (Phi-3 mini + Mistral 7B)
- Build the embeddings pipeline using sentence-transformers
