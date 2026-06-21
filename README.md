# AI Git Team Project — Run Instructions

## 1. Open the project folder

```bash
cd ai-git-team-project
```

## 2. Create and activate a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Train the model

```bash
python -m src.train_model
```

After successful training, the model will be saved in the `models/` folder.

## 5. Test prediction from terminal

```bash
python -m src.predict "This product is very good"
python -m src.predict "I hate this service"
```

## 6. Run the FastAPI backend

```bash
uvicorn src.api:app --reload
```

Open this URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Use the `/predict` endpoint to test the API.

## 7. Run the Streamlit web app

Open a new terminal, activate the virtual environment again, then run:

### Windows

```bash
venv\Scripts\activate
streamlit run app/streamlit_app.py
```

### Linux / Mac

```bash
source venv/bin/activate
streamlit run app/streamlit_app.py
```

Open this URL in your browser:

```text
http://localhost:8501
```

## 8. Run tests

```bash
pytest
```
