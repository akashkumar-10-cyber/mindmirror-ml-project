"""
MindMirror AI - Transparent Emotion Intensity Estimator
Computes a reproducible intensity score (0.0 to 1.0) and categorical level (Low, Medium, High)
by combining neural model confidence, lexical intensifiers, and affective urgency signals.
"""

import re
from typing import Dict, Any, List, Tuple

# Linguistic amplifiers that elevate emotional intensity
HIGH_AMPLIFIERS = [
    "extremely", "severely", "completely", "totally", "overwhelmed", "terrible",
    "unbearable", "impossible", "panic", "horrible", "can't handle", "cannot cope",
    "ruined", "desperate", "furious", "heartbroken", "dreading", "dying", "failing",
    "exhausted", "urgent", "terrified", "shaking", "screaming", "paralyzed"
]

MEDIUM_AMPLIFIERS = [
    "very", "really", "quite", "pretty", "definitely", "so much", "hard",
    "struggling", "worried", "nervous", "stressed", "annoyed", "upset",
    "tired", "pressure", "difficult", "heavy", "stuck", "confused"
]

MODERATORS = [
    "slightly", "a bit", "a little", "somewhat", "maybe", "kind of", "sort of",
    "manageable", "minor", "small"
]

class IntensityEstimator:
    """
    Transparent & Reproducible Emotion Intensity Estimator.
    Combines Model Probability Margin + Linguistic Amplifiers + Punctuation / Urgency Cues.
    """

    def estimate(self, text: str, emotion: str, confidence: float) -> Dict[str, Any]:
        """
        Estimates emotional intensity for the given text and ML prediction.
        Returns:
            - level: 'Low' | 'Medium' | 'High'
            - score: float (0.0 to 1.0)
            - factors: List[str] explaining the contributing signals
        """
        if not text or not text.strip():
            return {
                "level": "Low",
                "score": 0.2,
                "factors": ["Minimal baseline text"]
            }

        text_lower = text.lower()
        factors: List[str] = []
        score = 0.35  # Base neutral/moderate starting baseline

        # Factor 1: Model Confidence Weight (Contributes up to +0.30)
        conf_contribution = min(0.30, max(0.0, (confidence - 0.40) * 0.5))
        score += conf_contribution
        if confidence >= 0.80:
            factors.append(f"High ML classification confidence ({int(confidence*100)}%)")
        elif confidence >= 0.60:
            factors.append(f"Moderate ML classification confidence ({int(confidence*100)}%)")

        # Factor 2: Lexical Intensifiers (Contributes up to +0.35)
        found_high = [w for w in HIGH_AMPLIFIERS if w in text_lower]
        found_med = [w for w in MEDIUM_AMPLIFIERS if w in text_lower]
        found_mod = [w for w in MODERATORS if w in text_lower]

        if found_high:
            score += min(0.35, len(found_high) * 0.15)
            factors.append(f"Strong intensifiers detected: '{', '.join(found_high[:3])}'")
        elif found_med:
            score += min(0.20, len(found_med) * 0.08)
            factors.append(f"Moderate emotional keywords: '{', '.join(found_med[:3])}'")

        if found_mod:
            score -= min(0.20, len(found_mod) * 0.08)
            factors.append(f"Softening moderators present: '{', '.join(found_mod[:2])}'")

        # Factor 3: Text Punctuation and Urgency Markers (Contributes up to +0.15)
        exclamation_count = text.count("!")
        if exclamation_count >= 2:
            score += 0.10
            factors.append("Multiple exclamation marks indicating heightened arousal")
        elif exclamation_count == 1:
            score += 0.04

        # Capitalized urgency words (e.g., "HELP", "FAIL", "CANNOT")
        words = text.split()
        shouting_words = [w for w in words if len(w) > 2 and w.isupper() and w.isalpha()]
        if shouting_words:
            score += 0.10
            factors.append(f"Emphatic capitalization: '{', '.join(shouting_words[:2])}'")

        # Factor 4: Temporal Urgency ("tomorrow", "tonight", "in an hour", "deadline")
        urgency_markers = ["tomorrow", "tonight", "right now", "today", "in an hour", "urgent", "soon"]
        found_urgency = [m for m in urgency_markers if m in text_lower]
        if found_urgency:
            score += 0.10
            factors.append(f"Immediate time pressure: '{found_urgency[0]}'")

        # Bound score to [0.05, 0.98]
        final_score = round(max(0.05, min(0.98, score)), 3)

        # Categorization Thresholds
        if final_score >= 0.70:
            level = "High"
        elif final_score >= 0.42:
            level = "Medium"
        else:
            level = "Low"

        if not factors:
            factors.append("Standard conversational expression")

        return {
            "level": level,
            "score": final_score,
            "factors": factors
        }

intensity_estimator = IntensityEstimator()
