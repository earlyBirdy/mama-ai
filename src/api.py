"""FastAPI demo for mama-ai with real HF model."""
from fastapi import FastAPI
from pydantic import BaseModel

from .model import predict_text


class PredictRequest(BaseModel):
    text: str


app = FastAPI(title="mama-ai API", version="1.1.0")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "mama-ai"}


@app.post("/predict")
async def predict(body: PredictRequest):
    """Predict sentiment for the given text using a tiny HF model."""
    result = predict_text(body.text)
    return {
        "input": body.text,
        "label": result["label"],
        "score": result["score"],
    }
