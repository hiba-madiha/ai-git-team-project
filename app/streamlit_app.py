import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from src.predict import predict_sentiment


st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🤖",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #1f4e79;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #555;
        margin-bottom: 25px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        background-color: #f5f7fb;
        border: 1px solid #dce3f0;
        margin-top: 20px;
    }

    .positive {
        color: green;
        font-size: 28px;
        font-weight: bold;
    }

    .negative {
        color: red;
        font-size: 28px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


with st.sidebar:
    st.title("🤖 AI Project")
    st.write("This project is made for learning:")

    st.divider()

    st.subheader("Model Info")
    st.write("Algorithm: TF-IDF + Logistic Regression")
    st.write("Task: Sentiment Classification")


st.markdown('<div class="main-title">AI Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Enter any review, comment, or feedback and the AI model will predict whether it is positive or negative.</div>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns([2, 1])

with col1:
    user_text = st.text_area(
        "Enter your text:",
        height=180,
        placeholder="Example: This product is very useful and easy to use.",
    )

    predict_button = st.button("Analyze Sentiment", use_container_width=True)

with col2:
    st.info(
        """
        Examples you can try:

        Positive:
        - This app is amazing.
        - I love this service.

        Negative:
        - This product is bad.
        - I am disappointed.
        """
    )


if predict_button:
    if not user_text.strip():
        st.warning("Please enter some text first.")
    else:
        try:
            result = predict_sentiment(user_text)
            sentiment = result["sentiment"]
            confidence = result["confidence"]

            st.markdown('<div class="result-box">', unsafe_allow_html=True)

            if sentiment == "positive":
                st.markdown(
                    '<div class="positive">Prediction: POSITIVE 😊</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    '<div class="negative">Prediction: NEGATIVE 😟</div>',
                    unsafe_allow_html=True,
                )

            if confidence is not None:
                st.write(f"Confidence: **{confidence:.2f}**")

            with st.expander("Show complete prediction output"):
                st.json(result)

            st.markdown("</div>", unsafe_allow_html=True)

        except FileNotFoundError as e:
            st.error(str(e))
            st.code("python -m src.train_model")