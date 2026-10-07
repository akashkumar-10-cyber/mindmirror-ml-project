"""
MindMirror AI - Historical Pattern Detection Service
Analyzes stored SQLite records to dynamically extract emotion trends,
recurring context-emotion clusters, and intensity trajectories over time.
"""

from collections import Counter
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from ..database.models import AnalysisHistory

class PatternService:
    """Calculates statistical and sequential patterns from real stored user history."""

    def analyze_patterns(self, db: Session, session_id: str = "default_user") -> Dict[str, Any]:
        """
        Analyzes session history and returns actionable pattern insights.
        Returns:
            - patterns: List[str] (Human-readable calculated insights)
            - trend: str ('increasing' | 'decreasing' | 'stable' | 'insufficient_data')
            - top_emotion_context_pair: Optional[Tuple[str, str, int]]
        """
        # Fetch records sorted chronologically
        records = (
            db.query(AnalysisHistory)
            .filter(AnalysisHistory.session_id == session_id)
            .order_by(AnalysisHistory.created_at.asc())
            .all()
        )

        total_count = len(records)
        if total_count < 3:
            return {
                "patterns": ["Not enough data to identify a reliable pattern yet (requires 3+ analyses)."],
                "trend": "insufficient_data",
                "summary": "Record a few more entries to unlock personalized pattern insights.",
                "total_records": total_count
            }

        patterns: List[str] = []

        # 1. Cluster Analysis: (Emotion + Context) Frequency
        pair_counts = Counter()
        emotion_counts = Counter()
        context_counts = Counter()
        intensities = []

        for r in records:
            pair = (r.emotion, r.context)
            pair_counts[pair] += 1
            emotion_counts[r.emotion] += 1
            context_counts[r.context] += 1
            intensities.append(r.intensity_score)

        most_common_pair, pair_freq = pair_counts.most_common(1)[0]
        if pair_freq >= 2 and most_common_pair[1] != "Context uncertain":
            patterns.append(
                f"{most_common_pair[1]}-related {most_common_pair[0].lower()} has appeared {pair_freq} times across your recent entries."
            )

        # 2. Intensity Trajectory Trend (Slope over recent 3-5 entries)
        recent_intensities = intensities[-4:]
        if len(recent_intensities) >= 3:
            first_half = sum(recent_intensities[:len(recent_intensities)//2]) / (len(recent_intensities)//2)
            second_half = sum(recent_intensities[len(recent_intensities)//2:]) / (len(recent_intensities) - len(recent_intensities)//2)
            diff = second_half - first_half

            if diff <= -0.12:
                trend = "decreasing"
                patterns.append("Recent emotion intensity appears to be decreasing compared to earlier sessions.")
            elif diff >= 0.12:
                trend = "increasing"
                patterns.append("Recent emotion intensity shows an increasing trend; consider proactive pacing.")
            else:
                trend = "stable"
                patterns.append("Your emotion intensity has remained relatively stable over your recent reflections.")
        else:
            trend = "stable"

        # 3. Contextual Clustering Pattern
        most_common_context, ctx_freq = context_counts.most_common(1)[0]
        ctx_pct = int((ctx_freq / total_count) * 100)
        if ctx_pct >= 50 and most_common_context not in ["General", "Context uncertain"]:
            patterns.append(
                f"{ctx_pct}% of your reflections stem from the {most_common_context} domain, indicating it as a primary current focus."
            )

        # Fallback if no specific high-volume patterns emerged
        if not patterns:
            patterns.append("Your emotional expressions show diverse distribution across multiple contexts.")

        return {
            "patterns": patterns,
            "trend": trend,
            "summary": patterns[0],
            "total_records": total_count
        }

pattern_service = PatternService()
