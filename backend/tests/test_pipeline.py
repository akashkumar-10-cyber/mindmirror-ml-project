"""
MindMirror AI - Comprehensive Test Suite
Validates ML inference, intensity scoring, context extraction, action recommendation,
XAI token attribution, database persistence, and REST endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.main import app
from backend.database.connection import Base, get_db
from backend.database.models import AnalysisHistory
from backend.ml.emotion_model import emotion_classifier
from backend.ml.intensity_estimator import intensity_estimator
from backend.ml.context_detector import context_detector
from backend.ml.recommender import action_recommender
from backend.services.safety_service import safety_service

# Setup in-memory SQLite database with StaticPool for thread-safe test isolation
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"
test_engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)

# ==================== ML & PIPELINE UNIT TESTS ====================

def test_emotion_classifier_real_prediction():
    text = "I have an exam tomorrow and I haven't studied anything. I feel like I'm going to fail."
    res = emotion_classifier.predict(text)
    assert "emotion" in res
    assert "confidence" in res
    assert "raw_probabilities" in res
    assert res["emotion"] in ["ANXIETY", "FEAR", "SADNESS"]
    assert res["confidence"] > 0.3

def test_explainable_ai_token_attribution():
    text = "I have an exam tomorrow and I feel very nervous."
    tokens = emotion_classifier.explain(text, "ANXIETY")
    assert len(tokens) > 0
    words = [t["word"].lower() for t in tokens]
    assert "exam" in words or "nervous" in words
    for t in tokens:
        assert 0.0 <= t["weight"] <= 1.0

def test_intensity_estimation_high():
    text = "I am extremely overwhelmed and terrified of failing tomorrow!"
    res = intensity_estimator.estimate(text, "ANXIETY", 0.88)
    assert res["level"] == "High"
    assert res["score"] >= 0.70
    assert len(res["factors"]) > 0

def test_context_detection_academic():
    text = "I have three finals next week and my professor gave us too many assignments."
    res = context_detector.analyze(text)
    assert res["context"] == "Academic"
    assert "exam" in str(res["situation"]).lower() or "assignment" in str(res["situation"]).lower() or "workload" in str(res["situation"]).lower()

def test_context_detection_work():
    text = "My boss scheduled an urgent client presentation tomorrow and my code has a bug."
    res = context_detector.analyze(text)
    assert "Work" in res["context"]

def test_context_detection_proposal_never_uncertain():
    text = "I am going to propose a girl tomorrow with flowers"
    res = context_detector.analyze(text)
    assert res["context"] == "Relationships"
    assert "proposal" in res["situation"].lower()

def test_action_recommender_generation():
    steps = action_recommender.generate(
        emotion="ANXIETY",
        intensity="HIGH",
        context="Academic",
        situation="Upcoming exam / limited preparation",
        text="I have an exam tomorrow and haven't studied."
    )
    assert "recommendations" in steps
    assert len(steps["recommendations"]) == 5
    assert "explanation" in steps
    assert "general_suggestion" in steps

def test_safety_crisis_detection():
    safe_text = "I am stressed about my exam."
    is_crisis, _ = safety_service.evaluate_safety(safe_text)
    assert not is_crisis

    crisis_text = "I can't take this anymore and want to kill myself."
    is_crisis, msg = safety_service.evaluate_safety(crisis_text)
    assert is_crisis
    assert "988" in msg

# ==================== ENDPOINT INTEGRATION TESTS ====================

def test_health_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "model_loaded" in data

def test_analyze_endpoint_valid():
    payload = {
        "text": "I have an exam tomorrow and I haven't studied anything. I feel like I'm going to fail.",
        "session_id": "test_user_1"
    }
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["emotion"] in ["ANXIETY", "FEAR", "SADNESS"]
    assert data["context"] == "Academic"
    assert len(data["recommendation"]) == 5
    assert len(data["token_importance"]) > 0
    assert data["id"] is not None

def test_analyze_endpoint_too_short():
    payload = {"text": "a", "session_id": "test_user_1"}
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 422

def test_history_and_deletion_endpoints():
    # Insert 2 entries
    client.post("/api/analyze", json={"text": "Exam tomorrow and scared.", "session_id": "user_hist"})
    client.post("/api/analyze", json={"text": "Great day with friends!", "session_id": "user_hist"})

    # Fetch history
    res = client.get("/api/history?session_id=user_hist")
    assert res.status_code == 200
    history = res.json()
    assert len(history) == 2

    # Delete history
    del_res = client.delete("/api/history?session_id=user_hist")
    assert del_res.status_code == 200
    assert del_res.json()["deleted"] == 2

    # Verify history empty
    res2 = client.get("/api/history?session_id=user_hist")
    assert len(res2.json()) == 0

def test_dashboard_metrics():
    # Add multiple entries for pattern tracking
    for _ in range(3):
        client.post("/api/analyze", json={
            "text": "Studying for another difficult exam tomorrow.",
            "session_id": "user_dash"
        })

    dash_res = client.get("/api/dashboard?session_id=user_dash")
    assert dash_res.status_code == 200
    metrics = dash_res.json()
    assert metrics["total_analyses"] == 3
    assert metrics["most_common_context"] == "Academic"
    assert len(metrics["timeline_data"]) == 3
    assert len(metrics["active_patterns"]) > 0
