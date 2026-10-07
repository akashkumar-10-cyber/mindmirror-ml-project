"""
MindMirror AI - FastAPI API Endpoints
Implements REST endpoints for real-time ML analysis, history management,
dashboard aggregations, pattern discovery, and health diagnostics.
"""

import json
from collections import Counter
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import desc

from ..database.connection import get_db
from ..database.models import AnalysisHistory
from ..schemas.analysis_schema import (
    AnalyzeRequest,
    AnalyzeResponse,
    TokenImportance,
    HistoryItem,
    DashboardMetrics
)
from ..ml.emotion_model import emotion_classifier
from ..ml.intensity_estimator import intensity_estimator
from ..ml.context_detector import context_detector
from ..ml.recommender import action_recommender
from ..services.pattern_service import pattern_service
from ..services.safety_service import safety_service

router = APIRouter(prefix="/api", tags=["MindMirror API"])

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    """Health check endpoint displaying ML engine status and database connection."""
    try:
        count = db.query(AnalysisHistory).count()
        db_status = "healthy"
    except Exception as e:
        count = 0
        db_status = f"error: {str(e)}"

    return {
        "status": "healthy",
        "service": "MindMirror AI - Emotion-Aware Action Recommendation System",
        "model_loaded": emotion_classifier.model_name,
        "is_transformer_active": emotion_classifier.is_transformer_loaded,
        "supported_emotions": ["ANXIETY", "JOY", "SADNESS", "ANGER", "FRUSTRATION", "SURPRISE", "NEUTRAL"],
        "database": db_status,
        "total_records": count
    }

@router.post("/analyze", response_model=AnalyzeResponse, status_code=status.HTTP_201_CREATED)
def analyze_reflection(request: AnalyzeRequest, db: Session = Depends(get_db)):
    """
    Main ML Pipeline Endpoint:
    1. Input Validation
    2. ML Transformer Inference
    3. Token Attribution Explainability (XAI)
    4. Emotion Intensity Estimation
    5. Context & Situation Extraction
    6. Historical Pattern Integration
    7. Multi-Layer Action Recommendation Synthesis
    8. Safety / Crisis Screening
    9. SQLite Persistence
    """
    raw_text = request.text.strip()
    session_id = request.session_id or "default_user"

    if len(raw_text) < 2:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Reflection text is too short. Please provide at least 2 characters."
        )

    # 1. Real ML Emotion Classification
    ml_result = emotion_classifier.predict(raw_text)
    emotion = ml_result["emotion"]
    confidence = ml_result["confidence"]
    raw_probs = ml_result["raw_probabilities"]

    # 2. Token-level XAI Attribution
    token_weights = emotion_classifier.explain(raw_text, emotion)

    # 3. Transparent Intensity Estimation
    intensity_result = intensity_estimator.estimate(raw_text, emotion, confidence)
    intensity_level = intensity_result["level"]
    intensity_score = intensity_result["score"]
    intensity_factors = intensity_result["factors"]

    # 4. Context & Situation Detection
    context_result = context_detector.analyze(raw_text)
    context_name = context_result["context"]
    situation_name = context_result["situation"]
    context_kws = context_result["detected_keywords"]

    # 5. Check Historical Pattern from Existing Records
    pattern_data = pattern_service.analyze_patterns(db, session_id=session_id)
    recent_pattern_note = pattern_data["summary"] if pattern_data["total_records"] >= 2 else None

    # 6. Action Recommendation Synthesis
    recommendation_output = action_recommender.generate(
        emotion=emotion,
        intensity=intensity_level,
        context=context_name,
        situation=situation_name,
        text=raw_text,
        pattern_note=recent_pattern_note
    )

    # 7. Crisis & Safety Check
    is_crisis, crisis_msg = safety_service.evaluate_safety(raw_text)

    # Combined detected factors
    all_factors = intensity_factors + ([f"Context: {context_name} ({', '.join(context_kws)})"] if context_kws else [])

    # 8. Persist in Database
    db_record = AnalysisHistory(
        session_id=session_id,
        text=raw_text,
        emotion=emotion,
        confidence=confidence,
        raw_probabilities=json.dumps(raw_probs),
        intensity=intensity_level,
        intensity_score=intensity_score,
        context=context_name,
        situation=situation_name,
        detected_factors=json.dumps(all_factors),
        explanation=recommendation_output["explanation"],
        token_importance=json.dumps(token_weights),
        recommendation=json.dumps(recommendation_output["recommendations"]),
        general_suggestion=recommendation_output["general_suggestion"],
        pattern_note=recent_pattern_note
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return AnalyzeResponse(
        id=db_record.id,
        session_id=session_id,
        text=raw_text,
        emotion=emotion,
        confidence=confidence,
        raw_probabilities=raw_probs,
        intensity=intensity_level,
        intensity_score=intensity_score,
        context=context_name,
        situation=situation_name,
        detected_factors=all_factors,
        explanation=recommendation_output["explanation"],
        token_importance=[TokenImportance(**item) for item in token_weights],
        recommendation=recommendation_output["recommendations"],
        general_suggestion=recommendation_output["general_suggestion"],
        pattern_note=recent_pattern_note,
        is_crisis_alert=is_crisis,
        crisis_guidance=crisis_msg if is_crisis else None,
        timestamp=db_record.created_at.isoformat() if db_record.created_at else None
    )

@router.get("/history", response_model=List[HistoryItem])
def get_history(
    session_id: str = Query("default_user"),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db)
):
    """Retrieves chronological analysis history for the specified session."""
    records = (
        db.query(AnalysisHistory)
        .filter(AnalysisHistory.session_id == session_id)
        .order_by(desc(AnalysisHistory.created_at))
        .limit(limit)
        .all()
    )
    return [r.to_dict() for r in records]

@router.get("/dashboard", response_model=DashboardMetrics)
def get_dashboard_metrics(
    session_id: str = Query("default_user"),
    db: Session = Depends(get_db)
):
    """Calculates summary aggregations and timeline points for Chart.js charts."""
    records = (
        db.query(AnalysisHistory)
        .filter(AnalysisHistory.session_id == session_id)
        .order_by(AnalysisHistory.created_at.asc())
        .all()
    )

    total = len(records)
    if total == 0:
        return DashboardMetrics(
            total_analyses=0,
            most_common_emotion="None yet",
            avg_intensity_score=0.0,
            most_common_context="None yet",
            recent_trend="No data",
            emotion_distribution={},
            context_distribution={},
            intensity_distribution={},
            timeline_data=[],
            active_patterns=["Start your first analysis to see live metrics and historical insights!"]
        )

    emotion_counts = Counter(r.emotion for r in records)
    context_counts = Counter(r.context for r in records)
    intensity_counts = Counter(r.intensity for r in records)

    avg_intensity = sum(r.intensity_score for r in records) / total
    most_common_emotion = emotion_counts.most_common(1)[0][0]
    most_common_context = context_counts.most_common(1)[0][0]

    # Pattern and trend insights
    pattern_data = pattern_service.analyze_patterns(db, session_id=session_id)

    # Timeline data points for Chart.js
    timeline = []
    for r in records[-20:]:  # Last 20 points for smooth graphing
        timeline.append({
            "id": r.id,
            "timestamp": r.created_at.strftime("%b %d, %H:%M") if r.created_at else "Entry",
            "emotion": r.emotion,
            "intensity_score": round(r.intensity_score, 2),
            "intensity": r.intensity,
            "confidence": round(r.confidence, 2),
            "context": r.context
        })

    return DashboardMetrics(
        total_analyses=total,
        most_common_emotion=most_common_emotion,
        avg_intensity_score=round(avg_intensity, 2),
        most_common_context=most_common_context,
        recent_trend=pattern_data["trend"].capitalize(),
        emotion_distribution=dict(emotion_counts),
        context_distribution=dict(context_counts),
        intensity_distribution=dict(intensity_counts),
        timeline_data=timeline,
        active_patterns=pattern_data["patterns"]
    )

@router.get("/patterns")
def get_patterns(
    session_id: str = Query("default_user"),
    db: Session = Depends(get_db)
):
    """Returns detected emotional patterns and trend analysis."""
    return pattern_service.analyze_patterns(db, session_id=session_id)

@router.delete("/history")
def delete_all_history(
    session_id: str = Query("default_user"),
    db: Session = Depends(get_db)
):
    """Deletes all analysis history for a given session."""
    deleted_count = (
        db.query(AnalysisHistory)
        .filter(AnalysisHistory.session_id == session_id)
        .delete()
    )
    db.commit()
    return {"message": f"Successfully deleted {deleted_count} history records.", "deleted": deleted_count}

@router.delete("/history/{item_id}")
def delete_history_item(
    item_id: int,
    session_id: str = Query("default_user"),
    db: Session = Depends(get_db)
):
    """Deletes a specific history record by ID."""
    record = (
        db.query(AnalysisHistory)
        .filter(AnalysisHistory.id == item_id, AnalysisHistory.session_id == session_id)
        .first()
    )
    if not record:
        raise HTTPException(status_code=404, detail="Analysis record not found.")

    db.delete(record)
    db.commit()
    return {"message": f"Record #{item_id} deleted successfully.", "id": item_id}
