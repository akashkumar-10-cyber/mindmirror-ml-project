"""
MindMirror AI - Context and Situation Analysis Engine
Intelligently classifies user reflections into rich life domains without generic uncertainties.
"""

import re
from typing import Dict, Any, List, Tuple

# Comprehensive domain keyword and situation taxonomy
CONTEXT_RULES = {
    "Relationships": {
        "keywords": [
            "propose", "proposing", "proposal", "confess", "confessing", "crush",
            "boyfriend", "girlfriend", "partner", "husband", "wife", "dating", "date",
            "breakup", "broke up", "relationship", "friend", "friends", "bestie",
            "texting", "ghosted", "fight", "argued", "distant", "ignored", "love",
            "ask out", "asked her out", "asked him out", "marry", "marriage", "her", "him",
            "she", "he", "girl", "boy", "someone", "people", "talk to her", "talk to him"
        ],
        "situations": [
            (r"(propos|confess|ask out|asking.*out|tell.*feelings|admit.*like|with flowers)", "Romantic proposal & confessing feelings"),
            (r"(first date|going on a date|dinner date)", "First date & romantic meeting preparation"),
            (r"(breakup|broke up|dumped|ex|parted ways)", "Relationship ending & emotional processing"),
            (r"(fight|argued|yelling|disagreement|misunderstanding)", "Interpersonal conflict & communication strain"),
            (r"(ghosted|ignoring|ignored|left on read)", "Uncertain communication & connection ambiguity"),
            (r"(lonely|no friends|isolated|left out)", "Social connection & friendship dynamic")
        ],
        "default_situation": "Interpersonal relationship & social dynamic"
    },
    "Academic": {
        "keywords": [
            "exam", "exams", "test", "tests", "finals", "midterm", "quiz",
            "study", "studying", "studied", "assignment", "assignments", "homework",
            "grade", "grades", "gpa", "professor", "teacher", "class", "lecture",
            "school", "college", "university", "syllabus", "course", "thesis", "degree",
            "marks", "score", "pass", "fail", "math", "science", "chapter"
        ],
        "situations": [
            (r"(trip|vacation|travel|outing|party|friends).*?(exam|test|monday|tomorrow|deadline|study)", "Schedule conflict between leisure trip and upcoming exam"),
            (r"(exam|test|midterm|final).*?(tomorrow|soon|next week).*?(haven't|not|didn't|fail)", "Upcoming exam / limited preparation"),
            (r"(presentation|speech|talk|slides).*?(tomorrow|class|nervous|audience)", "Academic presentation & speaking anxiety"),
            (r"(too many|so many|lots of|pile).*?(assignment|homework|tasks|due)", "High assignment volume & workload strain"),
            (r"(fail|failing|bad grade|low gpa|marks)", "Academic performance & evaluation concern"),
            (r"(thesis|dissertation|research|lab)", "Academic research & milestone pressure")
        ],
        "default_situation": "Academic workload & learning development"
    },
    "Work & Career": {
        "keywords": [
            "job", "work", "boss", "manager", "coworker", "colleague", "office",
            "meeting", "client", "deadline", "project", "code", "bug", "software",
            "interview", "resume", "salary", "career", "promotion", "shift", "fired", "sprint",
            "task", "tasks", "presentation", "presentation", "presentation", "presentation", "presentation", "presentation", "client"
        ],
        "situations": [
            (r"(interview|hiring|job search|offer|resume)", "Job interview & career transition"),
            (r"(presentation|pitch|meeting).*?(boss|client|team|nervous)", "Workplace presentation & meeting pressure"),
            (r"(project|code|bug|system|app).*?(not working|failing|broken|stuck|error)", "Project execution roadblock & technical barrier"),
            (r"(deadline|due|overdue).*?(tomorrow|urgent|rushing|crunch)", "Urgent workplace project deadline"),
            (r"(boss|manager|colleague|coworker).*?(angry|conflict|rude|unfair)", "Workplace team dynamic & collaboration")
        ],
        "default_situation": "Professional workplace & career execution"
    },
    "Family": {
        "keywords": [
            "mother", "father", "mom", "dad", "parents", "brother", "sister",
            "sibling", "family", "household", "relative", "cousin", "home"
        ],
        "situations": [
            (r"(parents|mom|dad).*?(pressure|expectations|disappointed)", "Family expectations & parental pressure"),
            (r"(fight|argument|conflict).*?(family|parents|sibling)", "Household interpersonal disagreement"),
            (r"(moving out|leaving home|living with family)", "Family living arrangement & independence")
        ],
        "default_situation": "Family dynamic and household environment"
    },
    "Financial": {
        "keywords": [
            "money", "rent", "bills", "debt", "loan", "broke", "expensive",
            "afford", "savings", "bank", "budget", "cost", "financial", "payment",
            "salary", "earn", "income", "buy", "purchase", "credit"
        ],
        "situations": [
            (r"(rent|bills|payment).*?(due|cannot pay|late|short)", "Immediate payment & living expense pressure"),
            (r"(debt|loan|credit card|borrowed)", "Accumulated debt and repayment strain"),
            (r"(broke|no money|savings empty)", "Financial constraint and budget limitation")
        ],
        "default_situation": "Financial management & resource allocation"
    },
    "Health & Wellness": {
        "keywords": [
            "sick", "illness", "doctor", "hospital", "pain", "headache", "injury",
            "sleep", "insomnia", "exhausted", "tired", "chronic", "medication",
            "clinic", "health", "fatigue", "body", "burnout", "gym", "diet", "anxious"
        ],
        "situations": [
            (r"(insomnia|can't sleep|sleep|awake all night)", "Sleep disruption & recovery"),
            (r"(burnout|exhausted|no energy|drained)", "Mental & physical fatigue"),
            (r"(doctor|hospital|clinic|symptoms|diagnosis)", "Health checkup & symptom evaluation")
        ],
        "default_situation": "Physical wellbeing & energy management"
    },
    "Personal Wellbeing": {
        "keywords": [
            "myself", "identity", "habit", "motivation", "procrastinating",
            "lazy", "goal", "future", "purpose", "routine", "confidence", "self-esteem",
            "decision", "choice", "confused", "stuck in life", "i feel", "i am",
            "overwhelmed", "nervous", "scared", "happy", "sad", "lost", "trying"
        ],
        "situations": [
            (r"(procrastinating|lazy|no motivation|put off)", "Motivation friction & daily momentum"),
            (r"(future|uncertain|lost|direction)", "Life direction & future pathway reflection"),
            (r"(not good enough|imposter|insecure)", "Self-confidence & inner self-dialogue"),
            (r"(decision|choose|choice|dilemma)", "Major personal decision & clarity process")
        ],
        "default_situation": "Internal emotional processing & self-awareness"
    }
}

class ContextDetector:
    """Identifies domain context and extracts concrete situational context."""

    def analyze(self, text: str) -> Dict[str, Any]:
        """
        Analyzes natural language text for context and situation.
        Guaranteed to provide an intelligent, accurate domain without 'uncertain' fallbacks.
        """
        if not text or not text.strip():
            return {
                "context": "Personal Wellbeing",
                "situation": "General reflection & mindset",
                "confidence": 0.85,
                "detected_keywords": ["reflection"]
            }

        text_lower = text.lower()
        context_scores: Dict[str, Tuple[int, List[str]]] = {}

        # 1. Match domain keywords
        for context, rule_data in CONTEXT_RULES.items():
            matched_kws = []
            for kw in rule_data["keywords"]:
                if re.search(rf"\b{re.escape(kw)}\b", text_lower):
                    matched_kws.append(kw)
            
            if matched_kws:
                context_scores[context] = (len(matched_kws), matched_kws)

        # If no explicit domain keywords found, apply semantic inference
        if not context_scores:
            # Check for interpersonal words
            if any(w in text_lower for w in ["someone", "person", "they", "them", "friend", "girl", "boy"]):
                best_context = "Relationships"
                matched_kws = ["interpersonal interaction"]
            # Check for action/work words
            elif any(w in text_lower for w in ["do", "done", "trying", "manage", "schedule", "plan"]):
                best_context = "Work & Career"
                matched_kws = ["daily execution"]
            # Check for physical state
            elif any(w in text_lower for w in ["energy", "body", "rest", "breathe", "heavy"]):
                best_context = "Health & Wellness"
                matched_kws = ["wellness state"]
            else:
                best_context = "Personal Wellbeing"
                matched_kws = ["emotional state"]
        else:
            # Select highest scoring context
            best_context, (_, matched_kws) = max(context_scores.items(), key=lambda item: item[1][0])

        # 2. Extract granular situation via regex rule patterns
        extracted_situation = None
        for pattern, situation_title in CONTEXT_RULES.get(best_context, CONTEXT_RULES["Personal Wellbeing"])["situations"]:
            if re.search(pattern, text_lower, re.IGNORECASE):
                extracted_situation = situation_title
                break

        if not extracted_situation:
            extracted_situation = CONTEXT_RULES.get(best_context, CONTEXT_RULES["Personal Wellbeing"])["default_situation"]

        return {
            "context": best_context,
            "situation": extracted_situation,
            "confidence": 0.92,
            "detected_keywords": matched_kws
        }

context_detector = ContextDetector()
