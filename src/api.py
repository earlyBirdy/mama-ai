"""FastAPI demo for mama-ai."""
from fastapi import FastAPI

app = FastAPI(title="mama-ai API", version="1.1.0")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "mama-ai"}


@app.get("/predict")
async def predict(text: str):
    # TODO: swap with real model inference
    return {"input": text, "prediction": "demo-label", "confidence": 0.42}
