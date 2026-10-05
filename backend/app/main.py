"""
SemantiCache - Week 1 Skeleton
--------------------------------
This file proves that FastAPI, Redis, and PostgreSQL are all running
and able to talk to each other. Nothing fancy yet - no caching logic,
no embeddings. Just a working foundation we'll build on in Week 2+.
"""

import os
import redis
import psycopg2
from fastapi import FastAPI

app = FastAPI(title="SemantiCache API", version="0.1.0")

# ---- Read connection info from environment variables ----
# (these values are set in docker-compose.yml)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "semanticache")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")


@app.get("/")
def root():
    """Just a simple landing endpoint to confirm the API is alive."""
    return {"message": "SemantiCache backend is running"}


@app.get("/health")
def health_check():
    """
    Checks that the backend can actually reach Redis and PostgreSQL.
    This is the single most important endpoint for Week 1 -
    if this returns 'connected' for both, your whole stack is working.
    """
    status = {"redis": "not checked", "postgres": "not checked"}

    # --- Check Redis ---
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=3)
        r.ping()
        status["redis"] = "connected"
    except Exception as e:
        status["redis"] = f"error: {str(e)}"

    # --- Check PostgreSQL ---
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            connect_timeout=3,
        )
        conn.close()
        status["postgres"] = "connected"
    except Exception as e:
        status["postgres"] = f"error: {str(e)}"

    return status
