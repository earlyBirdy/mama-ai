"""FastAPI demo for mama-ai with pluggable backends and health endpoints."""
from fastapi import FastAPI
from pydantic import BaseModel

from src.model import predict_text, get_backend_status


class PredictRequest(BaseModel):
    text: str
    backend: str | None = None  # "hf", "gemini", or "heuristic"


app = FastAPI(title="mama-ai API", version="1.2.1")


@app.get("/health")
async def health():
    status = get_backend_status()
    ok = any(v.get("available") for v in status.values())
    return {"status": "ok" if ok else "degraded", "backends": status}


@app.get("/backend_status")
async def backend_status():
    return get_backend_status()


@app.post("/predict")
async def predict(body: PredictRequest):
    result = predict_text(body.text, backend=body.backend)
    return {
        "input": body.text,
        "backend": result["backend"],
        "label": result["label"],
        "score": result["score"],
    }
