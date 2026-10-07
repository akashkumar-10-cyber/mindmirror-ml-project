# MindMirror AI – Emotion-Aware Action Recommendation and Wellness Support System

> **“MindMirror AI doesn't just tell you how you feel — it understands the situation and helps you decide what to do next.”**

MindMirror AI is a Machine Learning innovation project that goes fundamentally beyond static sentiment/emotion classification. Rather than outputting an isolated categorical label (e.g. *“You are anxious”*), MindMirror AI combines:
1. **Transformer-based Emotion Classification**
2. **Transparent Emotion Intensity Estimation**
3. **Domain Context & Situational Grounding**
4. **Explainable AI (Token Perturbation Attribution)**
5. **Historical Pattern Detection**
6. **⭐ Emotion-Aware Next-Step Action Recommendation**

---

## 1. Problem Statement & Innovation

### The Traditional Problem
Standard text sentiment and emotion classifiers operate in a single dimension:
$$\text{User Text} \longrightarrow \text{Emotion Label}$$

Users in acute stress or cognitive overload are left with the question: **“Now what do I actually do about this?”**

### The MindMirror AI Proposed Innovation
MindMirror AI executes a multi-layer analytical synthesis:
$$\text{User Text} \longrightarrow \begin{pmatrix} \text{Transformer Emotion} \\ \text{Intensity Level} \\ \text{Context \& Situation} \\ \text{Token Explainability (XAI)} \\ \text{Historical Session Patterns} \end{pmatrix} \longrightarrow \text{5-Step Actionable Next Steps}$$

---

## 2. Core Architecture & Workflow

```
[ USER REFLECTION TEXT ]
          │
          ▼
 [ NLP PREPROCESSING ] ── (Sanitization, Truncation, BPE Tokenization)
          │
          ▼
[ REAL TRANSFORMER MODEL ] ── (Hugging Face DistilRoBERTa / PyTorch)
          │
     ┌────┴────────────────────────┬───────────────────────────┐
     ▼                             ▼                           ▼
[ EMOTION CLASSIFICATION ]  [ INTENSITY ESTIMATION ]  [ CONTEXT & SITUATION ]
(Anxiety, Joy, Sadness, etc.) (Low, Med, High Score)  (Academic, Work, etc.)
     │                             │                           │
     └─────────────────────────────┼───────────────────────────┘
                                   │
                                   ▼
                   [ TOKEN PERTURBATION XAI ]
                                   │
                                   ▼
             [ ACTION RECOMMENDATION SYNTHESIS ENGINE ]
               (5 Prioritized Next-Step Action Items)
                                   │
                                   ▼
                      [ SQLITE DATABASE STORAGE ]
                                   │
                                   ▼
             [ HISTORICAL PATTERN DETECTION & TRENDS ]
                                   │
                                   ▼
                 [ CHART.JS INTERACTIVE DASHBOARD ]
```

---

## 3. Machine Learning Specifications

### 3.1 Pretrained Transformer Model
- **Primary Model**: `j-hartmann/emotion-english-distilroberta-base` (Hugging Face Transformers / PyTorch)
- **Secondary / Offline Fallback**: `bhadresh-psav/bert-base-uncased-emotion` / Calibrated Affective Vector Engine
- **Supported Emotion Labels**:
  - `ANXIETY` (mapped from Fear/Worry)
  - `SADNESS`
  - `ANGER`
  - `FRUSTRATION` (mapped from Disgust/Aversion)
  - `JOY`
  - `SURPRISE`
  - `NEUTRAL`

### 3.2 Explainable AI (XAI) – Token Perturbation Attribution
MindMirror AI implements an explainability technique that measures the change in the predicted emotion probability when individual tokens are masked:
$$\text{Attribution}(w_i) = P(\text{emotion} \mid \text{text}) - P(\text{emotion} \mid \text{text} \setminus \{w_i\})$$
This assigns authentic attribution weights to each word, displayed as an interactive heatmap.

### 3.3 Transparent Emotion Intensity Estimation
Intensity is computed via a transparent formula combining:
1. **Model Confidence Margin**: Probability magnitude above baseline uniform distribution.
2. **Lexical Amplifiers**: Presence of high-arousal intensifiers (*extremely, overwhelmed, unbearable, terrified, urgent*).
3. **Punctuation & Urgency Cues**: Multiple exclamation marks, capitalizations, and immediate temporal markers (*tomorrow, tonight, in an hour*).

**Levels**:
- **Low**: Score $< 0.42$
- **Medium**: Score $0.42 - 0.69$
- **High**: Score $\ge 0.70$

### 3.4 Context & Situation Analysis Taxonomy
The system categorizes reflections into 8 life domains and extracts granular situational dynamics:
- **Academic**: Exam preparation crunch, presentation speaking anxiety, assignment volume overload.
- **Work**: Workplace presentation, project roadblocks/code bugs, urgent deadlines.
- **Relationships**: Interpersonal conflict, breakup processing, communication strain.
- **Family**: Household expectations, parental pressure.
- **Financial**: Immediate bill pressure, debt triage, budget limitations.
- **Health-related concern**: Sleep disruption/insomnia, physical fatigue, burnout.
- **Personal**: Procrastination friction, existential direction, self-doubt.
- **General**: Broad reflections (*Context uncertain* when confidence $< 0.35$).

---

## 4. Technology Stack

| Layer | Technologies |
|---|---|
| **Backend API** | Python 3.14 / 3.11+, FastAPI, Uvicorn, Pydantic |
| **Machine Learning** | PyTorch, Hugging Face Transformers (`DistilRoBERTa`), Tokenizers |
| **Database** | SQLite, SQLAlchemy ORM |
| **Frontend UI** | HTML5, Tailwind CSS, Vanilla JS / ES Modules, Lucide Icons |
| **Data Visualization** | Chart.js (Doughnut, Bar, Smooth Line Curve, Polar Area) |
| **Testing** | Pytest, FastAPI TestClient |

---

## 5. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/health` | Health diagnostics and loaded ML model status |
| `POST` | `/api/analyze` | Full ML analysis, intensity, context, recommendations, and persistence |
| `GET` | `/api/history` | Retrieves chronological reflection history for a session |
| `GET` | `/api/dashboard` | Returns aggregated metrics and coordinate data for Chart.js |
| `GET` | `/api/patterns` | Dynamic pattern discovery across historical session entries |
| `DELETE` | `/api/history` | Wipes all session history |
| `DELETE` | `/api/history/{id}` | Deletes a single history record |

---

## 6. Installation & Running in VS Code

### Step 1: Open the Project in VS Code
Open the project directory:
```
C:\Users\Dell\.gemini\antigravity\scratch\ML project
```

### Step 2: Install Dependencies (if not already installed)
```bash
pip install -r backend/requirements.txt
```

### Step 3: Run the Application
Run the one-click launcher from the VS Code terminal:
```bash
python start_app.py
```
*(Or double-click `run_project.bat` on Windows)*

The terminal will display the banner and active link:
```
================================================================================
  [ML Architecture] HuggingFace DistilRoBERTa + PyTorch + FastAPI + SQLite
  [Status]           Server launching on: http://127.0.0.1:8000
  [Frontend]         Web UI available at: http://127.0.0.1:8000
  [API Docs]         Swagger UI docs at:  http://127.0.0.1:8000/docs
================================================================================
```
The browser will automatically open to `http://127.0.0.1:8000`.

---

## 7. Automated Testing Suite

To run the full suite of 12 unit and integration tests:
```bash
python -m pytest backend/tests/test_pipeline.py -v
```

Tests cover:
- Real Transformer prediction and confidence evaluation
- Token-level explainability attribution calculation
- Intensity estimation thresholds (Low/Medium/High)
- Context & situation extraction across domains
- Action recommendation 5-step synthesis
- Crisis safety screening
- Health, Analyze, History, and Dashboard endpoints

---

## 8. Safety & Privacy Protocols

> [!IMPORTANT]
> **Supportive Wellness Prototype**: MindMirror AI is an emotion-aware machine learning prototype designed for supportive reflection and educational demonstration. It does **NOT** diagnose psychiatric or medical conditions and does **NOT** provide clinical treatment advice.

- **Crisis Detection**: Severe distress keywords trigger supportive helpline cards with 24/7 resources (**988 Lifeline**, **Crisis Text Line 741741**, **International Befrienders**).
- **Privacy**: All analysis records are persisted locally in SQLite (`mindmirror.db`). Users can delete individual records or wipe full history at any time.
