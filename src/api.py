"""FastAPI demo for mama-ai with pluggable backends and health endpoints."""
from fastapi import FastAPI
from pydantic import BaseModel

from src.model import predict_text, get_backend_status, run_mama_ai_flow


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



class MamaAIRequest(BaseModel):
    meal_description: str
    feeling: str
    activity_level: str  # e.g. "0–10", "10–30", "30–60", "60+"

@app.post("/mama_ai_demo")
async def mama_ai_demo(body: MamaAIRequest):
    """MAMA.AI demo endpoint.

    Accepts a simple text-based description of the meal, feeling, and movement,
    and returns a prototype JSON response representing what MAMA.AI would say.
    """
    result = run_mama_ai_flow(
        meal_description=body.meal_description,
        feeling=body.feeling,
        activity_level=body.activity_level,
    )
    return result
