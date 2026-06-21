# AI Git Team Project — Sentiment Analyzer

Ye project Git practice ke liye intentionally professional structure mein banaya gaya hai.

## Project kya karta hai?

Ye aik simple AI/NLP project hai jo user ke review/comment ko classify karta hai:

- Positive
- Negative

Is project mein ye cheezen included hain:

- Dataset CSV
- Model training script
- Prediction module
- FastAPI backend
- Streamlit web UI
- Unit tests
- GitHub Actions CI workflow
- `.gitignore`
- Team branch workflow practice

---

## Folder Structure

```text
ai-git-team-project/
│
├── app/
│   └── streamlit_app.py          # Web UI
│
├── data/
│   └── train.csv                 # Training dataset
│
├── models/                       # Model yahan save hoga after training
│
├── scripts/
│   ├── run_api.sh
│   ├── run_streamlit.sh
│   └── train.sh
│
├── src/
│   ├── __init__.py
│   ├── api.py                    # FastAPI app
│   ├── config.py                 # Common paths/settings
│   ├── predict.py                # Prediction code
│   ├── train_model.py            # Model training code
│   └── utils.py                  # Helper functions
│
├── tests/
│   └── test_predict.py           # Unit test
│
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 1. Project Run Karna

## Step 1: Folder open karo

```bash
cd ai-git-team-project
```

## Step 2: Virtual environment banao

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Requirements install karo

```bash
pip install -r requirements.txt
```

## Step 4: Model train karo

```bash
python -m src.train_model
```

Agar sab theek hai to terminal par output ayega:

```text
Model trained successfully
Model saved at: models/sentiment_model.joblib
```

## Step 5: Prediction test karo

```bash
python -m src.predict "This product is very good"
python -m src.predict "I hate this service"
```

## Step 6: API run karo

```bash
uvicorn src.api:app --reload
```

Browser mein open karo:

```text
http://127.0.0.1:8000/docs
```

Wahan `/predict` endpoint test karo.

## Step 7: Streamlit UI run karo

New terminal open karo, venv activate karo, phir:

```bash
streamlit run app/streamlit_app.py
```

Browser usually yahan open hota hai:

```text
http://localhost:8501
```

## Step 8: Tests run karo

```bash
pytest
```

---

# 2. Git Start Karna

## Step 1: Git initialize karo

```bash
git init
```

## Step 2: Status check karo

```bash
git status
```

## Step 3: Files stage karo

```bash
git add .
```

## Step 4: First commit karo

```bash
git commit -m "Initial AI sentiment project"
```

## Step 5: Main branch ka naam set karo

```bash
git branch -M main
```

---

# 3. GitHub Par Push Karna

GitHub par new repository banao. Example repo name:

```text
ai-git-team-project
```

Phir terminal mein:

```bash
git remote add origin https://github.com/YOUR_USERNAME/ai-git-team-project.git
git push -u origin main
```

Agar remote already added hai aur change karna hai:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/ai-git-team-project.git
```

---

# 4. Apni Branch Banana

Kabhi bhi directly `main` par kaam nahi karna. Feature branch banao.

```bash
git checkout main
git pull origin main
git checkout -b feature/improve-ui
```

Ab changes karo. Example: `app/streamlit_app.py` mein UI change karo.

```bash
git status
git add .
git commit -m "Improve Streamlit UI"
git push -u origin feature/improve-ui
```

GitHub par jao aur Pull Request banao:

```text
feature/improve-ui  --->  main
```

---

# 5. Team Member Ko Code Base Share Karna

GitHub repo ka link teammate ko do.

Teammate ye karega:

```bash
git clone https://github.com/YOUR_USERNAME/ai-git-team-project.git
cd ai-git-team-project
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python -m src.train_model
```

Teammate apni branch banaye:

```bash
git checkout -b feature/add-more-data
```

Phir changes kare, commit kare, push kare:

```bash
git add .
git commit -m "Add more training data"
git push -u origin feature/add-more-data
```

GitHub par Pull Request open kare.

---

# 6. Colleague Ki Branch Apne System Par Lana

Agar colleague ki branch ka naam hai:

```text
feature/add-more-data
```

To aap ye commands chalao:

```bash
git fetch origin
git checkout feature/add-more-data
```

Agar branch local mein nahi bani to:

```bash
git checkout -b feature/add-more-data origin/feature/add-more-data
```

Branch check karo:

```bash
git branch
```

---

# 7. Colleague Ki Branch Main Mein Merge Karna

Pehle latest main lo:

```bash
git checkout main
git pull origin main
```

Ab colleague ki branch merge karo:

```bash
git merge feature/add-more-data
```

Agar conflict nahi hai:

```bash
git push origin main
```

---

# 8. Pull Request Wala Professional Method

Recommended team workflow:

1. Har developer apni branch banaye.
2. Code change kare.
3. Commit kare.
4. Branch push kare.
5. Pull Request banaye.
6. Team review kare.
7. CI tests pass hon.
8. PR merge ho main mein.

---

# 9. Conflict Resolve Karna

Conflict tab hota hai jab 2 log same file ke same part ko change kar dete hain.

Example:

```bash
git merge feature/add-more-data
```

Agar conflict aya:

```text
CONFLICT (content): Merge conflict in data/train.csv
```

File open karo. Aapko aisa kuch dikhega:

```text
<<<<<<< HEAD
old line from main
=======
new line from colleague branch
>>>>>>> feature/add-more-data
```

Aap decide karo final line kya honi chahiye. Markers remove karo.

Phir:

```bash
git add data/train.csv
git commit -m "Resolve merge conflict in training data"
git push origin main
```

---

# 10. Apni Branch Mein Latest Main Lana

Agar aap apni feature branch par kaam kar rahi ho aur main update ho chuki hai:

```bash
git checkout feature/improve-ui
git fetch origin
git merge origin/main
```

Ya advanced clean history ke liye:

```bash
git checkout feature/improve-ui
git fetch origin
git rebase origin/main
```

Beginners ke liye merge easier hai.

---

# 11. Useful Git Commands

## Current branch dekhna

```bash
git branch
```

## All branches dekhna

```bash
git branch -a
```

## Commit history

```bash
git log --oneline --graph --all
```

## Last commit undo but changes keep

```bash
git reset --soft HEAD~1
```

## File ke changes discard

```bash
git checkout -- filename.py
```

## Stash temporary changes

```bash
git stash
git stash pop
```

## Remote check

```bash
git remote -v
```

---

# 12. Practice Tasks for Team

## Task A — UI Developer

Branch:

```bash
git checkout -b feature/ui-title
```

Kaam:

- Streamlit app ka title improve karo.
- Sidebar add karo.

## Task B — Data Developer

Branch:

```bash
git checkout -b feature/more-training-data
```

Kaam:

- `data/train.csv` mein 10 new positive aur negative examples add karo.

## Task C — Backend Developer

Branch:

```bash
git checkout -b feature/api-health
```

Kaam:

- FastAPI mein `/health` endpoint improve karo.

## Task D — ML Developer

Branch:

```bash
git checkout -b feature/model-metrics
```

Kaam:

- Training script mein accuracy print karo.

---

# 13. Recommended Branch Naming

```text
feature/add-login
feature/improve-ui
feature/model-metrics
bugfix/fix-api-error
hotfix/security-patch
experiment/new-model
docs/update-readme
```

---

# 14. Commit Message Style

Good commit messages:

```text
Add sentiment prediction API
Improve Streamlit UI layout
Fix model loading error
Add unit tests for prediction
Update README with run commands
```

Bad commit messages:

```text
changes
final
new work
abc
done
```

---

# 15. Best Professional Workflow

```bash
git checkout main
git pull origin main
git checkout -b feature/my-work

# changes karo

git status
git add .
git commit -m "Meaningful message"
git push -u origin feature/my-work
```

GitHub par Pull Request banao.

Merge ke baad local update:

```bash
git checkout main
git pull origin main
git branch -d feature/my-work
```

Remote branch delete:

```bash
git push origin --delete feature/my-work
```

---

# 16. One Complete Example

Aap UI change karna chahti hain:

```bash
git checkout main
git pull origin main
git checkout -b feature/ui-improvement
```

`app/streamlit_app.py` edit karo.

```bash
git add app/streamlit_app.py
git commit -m "Improve Streamlit sentiment UI"
git push -u origin feature/ui-improvement
```

GitHub par PR banao.

Agar teammate ka PR merge ho gaya aur aapki branch old ho gayi:

```bash
git checkout feature/ui-improvement
git fetch origin
git merge origin/main
```

Conflict aaye to resolve karo, phir:

```bash
git add .
git commit -m "Resolve conflicts with main"
git push
```

---

# 17. Important Concept

`main` branch stable production code hoti hai.

Feature branches development ke liye hoti hain.

Pull Request review ke liye hoti hai.

Merge final approved code ko main mein lane ke liye hota hai.
