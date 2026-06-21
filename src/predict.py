import sys
import joblib
from src.config import MODEL_PATH
from src.utils import clean_text


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model not found. Please train the model first using: python -m src.train_model"
        )
    return joblib.load(MODEL_PATH)


def predict_sentiment(text: str) -> dict:
    model = load_model()
    cleaned = clean_text(text)

    label = model.predict([cleaned])[0]

    confidence = None
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba([cleaned])[0]
        confidence = float(max(probabilities))

    return {
        "text": text,
        "cleaned_text": cleaned,
        "sentiment": label,
        "confidence": confidence,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python -m src.predict "your text here"')
        sys.exit(1)

    user_text = " ".join(sys.argv[1:])
    result = predict_sentiment(user_text)
    print(result)
