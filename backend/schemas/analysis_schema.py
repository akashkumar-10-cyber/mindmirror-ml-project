"""
MindMirror AI - Pydantic Schemas for Request and Response Validation.
"""

from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=2, max_length=2500, description="Natural language reflection to analyze")
    session_id: Optional[str] = Field("default_user", description="Session identifier for historical pattern tracking")

class TokenImportance(BaseModel):
    word: str
    weight: float
    impact: str = "neutral"  # positive, negative, neutral

class AnalyzeResponse(BaseModel):
    id: Optional[int] = None
    session_id: str
    text: str
    emotion: str
    confidence: float
    raw_probabilities: Dict[str, float]
    intensity: str  # Low, Medium, High
    intensity_score: float
    context: str
    situation: str
    detected_factors: List[str]
    explanation: str
    token_importance: List[TokenImportance]
    recommendation: List[str]
    general_suggestion: Optional[str] = None
    pattern_note: Optional[str] = None
    is_crisis_alert: bool = False
    crisis_guidance: Optional[str] = None
    timestamp: Optional[str] = None

class HistoryItem(BaseModel):
    id: int
    session_id: str
    text: str
    emotion: str
    confidence: float
    intensity: str
    intensity_score: float
    context: str
    situation: str
    detected_factors: List[str]
    explanation: str
    token_importance: List[TokenImportance]
    recommendation: List[str]
    general_suggestion: Optional[str]
    pattern_note: Optional[str]
    timestamp: Optional[str]

class DashboardMetrics(BaseModel):
    total_analyses: int
    most_common_emotion: str
    avg_intensity_score: float
    most_common_context: str
    recent_trend: str
    emotion_distribution: Dict[str, int]
    context_distribution: Dict[str, int]
    intensity_distribution: Dict[str, int]
    timeline_data: List[Dict[str, Any]]
    active_patterns: List[str]
