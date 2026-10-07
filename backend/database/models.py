"""
MindMirror AI - Database Models
SQLAlchemy ORM Model for persisting emotion analysis, context, recommendations, and metrics.
"""

from datetime import datetime, timezone
import json
from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from .connection import Base

class AnalysisHistory(Base):
    """Stores full historical emotion analysis records."""
    __tablename__ = "analysis_history"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    session_id = Column(String(64), index=True, nullable=False, default="default_user")
    text = Column(Text, nullable=False)
    
    # ML Emotion Output
    emotion = Column(String(32), index=True, nullable=False)
    confidence = Column(Float, nullable=False)
    raw_probabilities = Column(Text, nullable=True)  # JSON string of all class probs
    
    # Intensity
    intensity = Column(String(16), index=True, nullable=False)  # Low, Medium, High
    intensity_score = Column(Float, nullable=False)
    
    # Context & Situation
    context = Column(String(32), index=True, nullable=False)  # Academic, Work, etc.
    situation = Column(String(256), nullable=False)
    detected_factors = Column(Text, nullable=True)  # JSON list
    
    # Explainable AI (XAI)
    explanation = Column(Text, nullable=False)
    token_importance = Column(Text, nullable=True)  # JSON list of {word, weight}
    
    # Personalized Recommendations
    recommendation = Column(Text, nullable=False)  # JSON list of step strings
    general_suggestion = Column(Text, nullable=True)
    pattern_note = Column(Text, nullable=True)
    
    # Metadata
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), index=True)

    def to_dict(self):
        """Serialize model instance to clean dictionary."""
        def safe_json_loads(val, default):
            if not val:
                return default
            try:
                return json.loads(val)
            except Exception:
                return default

        return {
            "id": self.id,
            "session_id": self.session_id,
            "text": self.text,
            "emotion": self.emotion,
            "confidence": round(self.confidence, 4),
            "raw_probabilities": safe_json_loads(self.raw_probabilities, {}),
            "intensity": self.intensity,
            "intensity_score": round(self.intensity_score, 4),
            "context": self.context,
            "situation": self.situation,
            "detected_factors": safe_json_loads(self.detected_factors, []),
            "explanation": self.explanation,
            "token_importance": safe_json_loads(self.token_importance, []),
            "recommendation": safe_json_loads(self.recommendation, []),
            "general_suggestion": self.general_suggestion,
            "pattern_note": self.pattern_note,
            "timestamp": self.created_at.isoformat() if self.created_at else None
        }
