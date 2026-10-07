"""
MindMirror AI - Safety & Supportive Crisis Screening Service
Detects potential acute emotional distress and attaches supportive, non-diagnostic guidance
with verified crisis resources.
"""

import re
from typing import Dict, Any, Tuple

CRISIS_PATTERNS = [
    r"\b(suicide|suicidal|kill myself|end my life|want to die|take my own life)\b",
    r"\b(self harm|cut myself|hurting myself|bleed to death)\b",
    r"\b(no reason to live|better off dead|can't live anymore)\b"
]

CRISIS_MESSAGE = (
    "MindMirror AI is a supportive wellness prototype, not a medical or diagnostic tool. "
    "If you or someone you know is going through severe distress or having thoughts of self-harm, "
    "please know you are not alone. Please reach out to immediate human support: \n"
    "• In the US/Canada: Call or text 988 (Suicide & Crisis Lifeline) available 24/7.\n"
    "• Text HOME to 741741 to connect with a Crisis Counselor.\n"
    "• In the UK: Call 111 (NHS) or 116 123 (Samaritans).\n"
    "• International: Visit https://findahelpline.com to find confidential support in your country."
)

class SafetyService:
    """Screens text for acute distress signals and provides supportive safety pathways."""

    def evaluate_safety(self, text: str) -> Tuple[bool, str]:
        """
        Returns:
            - is_crisis: bool (True if acute crisis pattern detected)
            - guidance_text: str (Supportive helpline message if crisis, else empty)
        """
        if not text:
            return False, ""

        text_lower = text.lower()
        for pattern in CRISIS_PATTERNS:
            if re.search(pattern, text_lower):
                return True, CRISIS_MESSAGE

        return False, ""

safety_service = SafetyService()
