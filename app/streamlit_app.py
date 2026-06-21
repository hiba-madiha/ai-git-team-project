import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from src.predict import predict_sentiment


st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 AI Sentiment Analyzer")
st.write("Type a review/comment and the AI model will predict whether it is positive or negative.")

with st.sidebar:
    st.header("About")
    st.write("This project is made for Git, branching, merging, Pull Requests, and team workflow practice.")
    st.write("Model: TF-IDF + Logistic Regression")

user_text = st.text_area("Enter text:", height=140, placeholder="Example: This product is amazing!")

if st.button("Predict Sentiment"):
    if not user_text.strip():
        st.warning("Please enter some text first.")
    else:
        try:
            result = predict_sentiment(user_text)
            sentiment = result["sentiment"]
            confidence = result["confidence"]

            if sentiment == "positive":
                st.success(f"Prediction: {sentiment.upper()}")
            else:
                st.error(f"Prediction: {sentiment.upper()}")

            if confidence is not None:
                st.info(f"Confidence: {confidence:.2f}")

            st.json(result)
        except FileNotFoundError as e:
            st.error(str(e))
            st.code("python -m src.train_model")
