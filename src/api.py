"""FastAPI demo for mama-ai with pluggable backends."""
from fastapi import FastAPI
from pydantic import BaseModel

from src.model import predict_text


class PredictRequest(BaseModel):
    text: str
    backend: str | None = None  # "hf", "gemini", or "heuristic"


app = FastAPI(title="mama-ai API", version="1.2.0")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "mama-ai"}


@app.post("/predict")
async def predict(body: PredictRequest):
    result = predict_text(body.text, backend=body.backend)
    return {
        "input": body.text,
        "backend": result["backend"],
        "label": result["label"],
        "score": result["score"],
    }
