from fastapi import FastAPI
from pydantic import BaseModel

from src.predict import predict_sentiment


app = FastAPI(
    title="AI Sentiment Analyzer API",
    description="A simple AI API for Git/team workflow practice.",
    version="1.0.0",
)


class PredictionRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "AI Sentiment Analyzer API is running",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "sentiment-analyzer",
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    return predict_sentiment(request.text)
