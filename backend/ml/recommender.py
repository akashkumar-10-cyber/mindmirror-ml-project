"""
MindMirror AI - Emotion-Aware Action Recommendation Engine
Translates user reflection into simple, relatable, and deeply personalized 5-step action plans.
Written in clear, warm, and easily understandable language connected directly to the user's specific scenario.
"""

import re
from typing import Dict, List, Any, Optional

class ActionRecommender:
    """
    Synthesizes user reflections, emotion, intensity, and situational dynamics
    into clean, understandable, and deeply relevant 5-step action plans.
    """

    def generate(
        self,
        emotion: str,
        intensity: str,
        context: str,
        situation: str,
        text: str,
        pattern_note: Optional[str] = None
    ) -> Dict[str, Any]:
        emotion_upper = emotion.upper()
        intensity_upper = intensity.upper()
        
        explanation = self._build_explanation(emotion_upper, intensity_upper, context, situation, text)
        steps = self._build_action_steps(emotion_upper, intensity_upper, context, situation, text)
        wellness = self._build_wellness_suggestion(emotion_upper, context, situation, text)

        return {
            "explanation": explanation,
            "recommendations": steps,
            "general_suggestion": wellness
        }

    def _build_explanation(self, emotion: str, intensity: str, context: str, situation: str, text: str) -> str:
        return (
            f"Based on what you shared, you are experiencing {emotion.lower()} ({intensity.lower()} intensity) "
            f"around your {context.lower()} ({situation.lower()}). "
            f"Here is a simple, step-by-step action plan to help you move forward right now."
        )

    def _build_action_steps(self, emotion: str, intensity: str, context: str, situation: str, text: str) -> List[str]:
        t = text.lower()
        sit = situation.lower()

        # =========================================================================
        # 1. ROMANTIC PROPOSALS & CONFESSIONS
        # =========================================================================
        if any(w in t for w in ["propos", "confess", "tell her i like", "tell him i like", "tell her how i feel", "tell him how i feel", "with flowers", "ask her out", "ask him out", "crush"]):
            return [
                "Keep your words simple and real: You don't need a scripted speech. Just share 1 or 2 things you genuinely appreciate about her.",
                "Choose a relaxed, quiet setting: Pick a comfortable place where neither of you feels rushed or put under pressure in front of crowds.",
                "Take 3 slow breaths before speaking: Calm your racing heart and turn that nervous energy into genuine, warm excitement.",
                "Speak with an honest smile: Look her in the eyes, be yourself, and speak from the heart without demanding an immediate answer.",
                "Give her space to take it in: Whatever her initial reaction is, smile and show maturity—being brave enough to share your feelings is already a huge win."
            ]

        # =========================================================================
        # 2. DATING & FIRST DATES
        # =========================================================================
        if "date" in t or "first date" in sit:
            return [
                "Get the basics sorted early: Confirm the time, place, and how you're getting there so you aren't rushing at the last minute.",
                "Pick an outfit you feel great in: Wear something comfortable and clean that makes you feel confident and like yourself.",
                "Think of 2 or 3 fun conversation topics: Keep simple topics in mind like favorite music, funny travel moments, or weekend hobbies.",
                "Focus on getting to know them, not 'impressing' them: Remember, a date is just two people hanging out to see if they vibe, not a job interview.",
                "Listen closely and be present: Put your phone away, ask follow-up questions, and enjoy the conversation as it unfolds naturally."
            ]

        # =========================================================================
        # 3. BREAKUP, HEARTBREAK & REJECTION (ROMANTIC)
        # =========================================================================
        if any(w in t for w in ["breakup", "broke up", "dumped", "ex-boyfriend", "ex-girlfriend", "heartbroken", "she rejected", "he rejected", "parted ways", "missing her", "missing him", "miss my ex"]):
            return [
                "Accept the sadness without shame: Grieving a connection is a natural human reaction. Let the tears flow if you need to.",
                "Keep distance to protect your healing: Don't check their social media or read old chat messages today. That only re-opens the wound.",
                "Write your raw thoughts in a private note: Pour everything you want to say onto a piece of paper, then close it or tear it up. Do NOT send it.",
                "Spend time with someone who makes you feel safe: Hang out with a friend, sibling, or pet who reminds you that you are loved and valued.",
                "Take life one day at a time: You don't have to feel 100% better tomorrow. Just focus on getting through today with kindness toward yourself."
            ]

        # =========================================================================
        # 4. GRIEF & LOSS (DEATH OF LOVED ONE OR PET)
        # =========================================================================
        if any(w in t for w in ["died", "passed away", "grief", "grieving", "lost my dog", "lost my cat", "lost my pet", "lost my grandma", "lost my grandpa", "lost my mom", "lost my dad", "funeral", "mourning"]):
            return [
                "Allow yourself to mourn freely: Tears and heavy sorrow are a testament to how deeply you loved them. Do not rush yourself.",
                "Surround yourself with soft physical comforts: Wrap up in a warm blanket, drink water, and keep your surroundings gentle and quiet.",
                "Look at a favorite photo or write down a special memory: Honor their memory by recalling a moment that made you both smile.",
                "Let others support you right now: If someone offers to bring you food, listen, or sit with you, accept their kindness. You don't have to carry this alone.",
                "Breathe through the waves: Grief comes in heavy waves. When a wave hits, put your hand on your heart and focus on slow, gentle breathing."
            ]

        # =========================================================================
        # 5. SCHEDULE CONFLICT: TRIP / OUTING vs UPCOMING EXAM OR DEADLINE
        # =========================================================================
        if ("trip" in t or "vacation" in t or "outing" in t or "party" in t or "travel" in t or "friends" in t) and ("exam" in t or "test" in t or "deadline" in t or "study" in t):
            return [
                "Do an honest 5-minute study check: How much of the syllabus do you already know? Knowing your real prep level removes the vague panic and gives you a clear decision.",
                "Finish high-scoring topics on Friday & Saturday: Study in focused 45-minute sprints before Sunday so 80% of your exam preparation is locked in ahead of time.",
                "Decide your trip plan with zero guilt: If your study is done, go on the trip and enjoy it. If you are totally unprepared, consider shortening the trip or returning early so you don't stress on Sunday night.",
                "Pack a 1-page portable revision sheet: Download short formulas, flashcards, or key points on your phone for quick 15-minute reviews during travel downtime.",
                "Protect Sunday night sleep (at least 6 hours): Make sure you get home early enough on Sunday to get solid sleep - showing up refreshed on Monday morning is essential for exam recall."
            ]

        # =========================================================================
        # 6. ACADEMIC FAILURE / BAD MARKS / EXAM DISAPPOINTMENT
        # =========================================================================
        if any(w in t for w in ["failed my exam", "failed test", "bad marks", "low score", "bad grade", "low gpa", "flunked", "scored low", "failed the class"]):
            return [
                "Let out the initial disappointment: It sucks to work hard and not get the score you wanted. Give yourself permission to feel sad for a moment without beating yourself up.",
                "Look at the big picture: One bad mark or failed test does not define your intelligence or future. You can recover from this.",
                "Identify what went wrong without self-blame: Look at the paper and pinpoint if the issue was lack of time, misreading questions, or not understanding a specific chapter.",
                "Ask for feedback or guidance: Reach out to your teacher or a classmate who did well to ask how they approached those difficult questions.",
                "Create a simple comeback plan for the next test: Plan 30 minutes of study each day for the next test so you're not cramming at the last minute."
            ]

        # =========================================================================
        # 6. UPCOMING EXAMS & TESTS (PREPARATION CRUNCH)
        # =========================================================================
        if any(w in t for w in ["exam", "test", "quiz", "finals", "midterm", "haven't studied", "didn't study", "syllabus"]):
            if intensity == "HIGH" or "haven't studied" in t or "haven't prepared" in t or "tomorrow" in t:
                return [
                    "Stop panic-scrolling and pause (2 mins): Sit back, close your eyes, and take 4 deep breaths. Panicking steals time; focus gives you marks.",
                    "Pick the Top 3 highest-scoring topics: Look at past papers or class notes and identify the 3 most important topics that carry maximum marks.",
                    "Start a 25-minute study sprint: Set a timer for 25 minutes. Study Topic #1 without checking your phone or switching tabs.",
                    "Test yourself with 2 practice problems: Don't just re-read notes. Try solving 2 questions on paper without looking at the answer.",
                    "Protect at least 5 hours of sleep: Cramming all night leads to blanking out during the exam. Sleep helps your brain recall what you reviewed."
                ]
            else:
                return [
                    "Separate your chapters into 'Must-Know' vs 'Quick Review': Focus 80% of your remaining study time on the highest-yield chapters.",
                    "Dedicate a 45-minute block to your weakest subject: Tackle the topic causing you the most stress while your mind is still fresh.",
                    "Make a 1-page formula & definition summary: Write down key points on a single sheet of paper for rapid last-minute revision.",
                    "Do a quick 10-minute quiz: Test yourself on the main definitions to lock them into long-term memory.",
                    "Take regular 5-minute stretch breaks: Drink water, stretch your neck and shoulders, and keep your workspace tidy."
                ]

        # =========================================================================
        # 7. JOB REJECTION / FIRED / CAREER DISAPPOINTMENT
        # =========================================================================
        if any(w in t for w in ["rejected from job", "got rejected", "fired", "laid off", "unemployed", "job rejection", "didn't get the job", "lost my job", "no interview callback"]):
            return [
                "Take today to process the disappointment: Being rejected or losing a job hurts. Give yourself 24 hours to relax before jumping back into applications.",
                "Remember hiring is often a timing game: Companies reject great candidates all the time for reasons that have nothing to do with your talent.",
                "Improve just 1 small thing on your resume: Add a clear bullet point or update your portfolio to make your strengths stand out better.",
                "Apply to 2 new opportunities tomorrow: Don't overwhelm yourself with 50 applications. Just send 2 well-tailored applications.",
                "Celebrate that you put yourself out there: Every application and interview makes you sharper for the opportunity that is actually right for you."
            ]

        # =========================================================================
        # 8. JOB INTERVIEWS & PREPARATION
        # =========================================================================
        if any(w in t for w in ["interview", "job interview", "hiring", "interviewer", "applied for a job"]):
            return [
                "Prepare your 60-second 'About Me': Practice introducing your background and key strengths out loud in a conversational, friendly tone.",
                "Pick 2 stories showing how you solved problems: Think of 2 real examples where you handled a difficult challenge and achieved a good result.",
                "Write down 2 thoughtful questions to ask them: Ask about team collaboration or what success looks like in the role in the first 90 days.",
                "Check your setup in advance: Test your camera/mic or iron your clothes early so you aren't stressing about tech or logistics.",
                "Pre-interview reset: Drink a glass of water, do a quick posture stretch, and remember they called you in because your profile impressed them."
            ]

        # =========================================================================
        # 9. PUBLIC SPEAKING, SPEECHES & PRESENTATIONS
        # =========================================================================
        if any(w in t for w in ["presentation", "speech", "speaking in front", "stage fright", "presenting", "pitch"]):
            return [
                "Nail your opening 30 seconds: Write down and practice your exact first two sentences out loud until they roll off your tongue effortlessly.",
                "Do 1 complete practice run out loud: Rehearse through your slides once from start to finish without stopping for tiny stumbles.",
                "Keep 3 bullet reminders per slide: Don't read long paragraphs—just glance at your key bullet points to guide your thoughts.",
                "Drop your shoulders and breathe (2 mins): Before you speak, relax your jaw, drop your shoulders away from your ears, and take 3 deep belly breaths.",
                "Remember the audience wants you to succeed: They are listening to learn something helpful, not waiting to catch you making a mistake."
            ]

        # =========================================================================
        # 10. WORKPLACE DEADLINES & OVERWHELMING BACKLOG
        # =========================================================================
        if any(w in t for w in ["boss", "deadline", "urgent", "so many assignments", "too much work", "backlog", "pile of work", "workload"]):
            return [
                "Do a 3-minute brain dump: Write down every pending task on a clean sheet of paper to get them out of your head.",
                "Pick the single most urgent task: Circle the one item that will cause the biggest problem if not finished today.",
                "Break that top task into 3 tiny steps: For example: 'Open file', 'Write outline', 'Complete section 1'. Small steps kill procrastination.",
                "Set a 30-minute timer and focus on Step 1: Put your phone in another room or on silent and work on only that single task until the timer dings.",
                "Check off the task and take a 5-minute break: Celebrate the progress, take a brief walk, then move to the next item."
            ]

        # =========================================================================
        # 11. PROGRAMMING BUGS, CODING & TECHNICAL ROADBLOCKS
        # =========================================================================
        if any(w in t for w in ["code", "bug", "error", "debugging", "program", "failing", "broken", "compiler", "runtime", "syntax"]):
            return [
                "Step away from the screen for 5 minutes: Physically stand up, get a glass of water, and look out the window to clear your mind.",
                "Explain the problem out loud in plain English: Describe the exact expected behavior vs the actual error (Rubber Duck Debugging).",
                "Check the latest change and print logs: Isolate the single line or function where variables aren't receiving the expected data.",
                "Test the smallest possible piece: Comment out unrelated code or write a minimal test case to verify the root cause.",
                "Timebox it: If you're still stuck after 30 minutes, write down what you tried and ask a teammate or search the exact error message online."
            ]

        # =========================================================================
        # 12. CONFLICTS, ARGUMENTS & FIGHTS (FRIENDS, PARTNER, FAMILY)
        # =========================================================================
        if any(w in t for w in ["fight", "argued", "argument", "fighting", "yelled", "angry with", "misunderstanding", "mad at me", "disagreement"]):
            return [
                "Let things cool down before replying: Never send angry text messages when your heart is pounding. Wait until your pulse is steady.",
                "Identify what actually bothered you: Write down privately: 'What specific action upset me, and how did it make me feel?'",
                "Use 'I feel' statements instead of blaming: When you're ready to talk, say 'I felt hurt when...' instead of 'You always...'",
                "Talk in person or over a call: Text messages strip away tone of voice and lead to misunderstandings. Speak calmly.",
                "Listen to their side without interrupting: Understanding each other is more important than 'winning' an argument."
            ]

        # =========================================================================
        # 13. FINANCIAL STRESS & EXPENSES (RENT, BILLS, MONEY)
        # =========================================================================
        if any(w in t for w in ["money", "rent", "bills", "broke", "expensive", "debt", "loan", "cannot afford", "salary", "bank account"]):
            return [
                "Write down the exact numbers on paper: Knowing the exact amounts and real due dates is always less scary than vague panic in your head.",
                "Sort expenses into 'Needs' vs 'Can Wait': Prioritize essentials (food, housing, utility bills) and pause non-essential subscriptions or spending for this week.",
                "Check if you can get a payment extension: Many utility, rent, or bill providers will give you an extra 7-14 days if you call them politely before the due date.",
                "Set a simple 7-day budget: Give yourself a realistic daily spending limit for groceries and basics until your next paycheck.",
                "Focus on what you can control right now: Take one small step today (like canceling an unused subscription or tracking today's expenses)."
            ]

        # =========================================================================
        # 14. SLEEPLESSNESS, INSOMNIA & PHYSICAL EXHAUSTION
        # =========================================================================
        if any(w in t for w in ["sleep", "insomnia", "can't sleep", "awake", "tired", "exhausted", "fatigue", "no energy", "burnout", "drained"]):
            return [
                "Put all glowing screens away right now: Blue light tells your brain it is daytime. Turn off phone notifications and dim room lights.",
                "Drink a glass of water and get comfortable: Adjust your pillow, loosen your clothes, and lie down in a cool room.",
                "Try the 4-7-8 breathing method: Inhale through your nose for 4 seconds, hold for 7 seconds, and exhale slowly through your mouth for 8 seconds.",
                "If you can't sleep after 20 minutes, get out of bed: Sit in a dim corner and read a book or listen to calming music until your eyelids feel heavy.",
                "Give yourself permission to just rest: Even resting quietly with your eyes closed recharges your body and brain."
            ]

        # =========================================================================
        # 15. LONELINESS & FEELING ISOLATED
        # =========================================================================
        if any(w in t for w in ["lonely", "alone", "isolated", "no friends", "nobody to talk to", "left out", "feeling down", "nobody cares"]):
            return [
                "Remind yourself that loneliness is a temporary state, not who you are: Feeling alone right now does not mean nobody cares or that you won't make friends.",
                "Send a simple, casual text to one person: Reach out with a friendly 'Hey! How have you been doing lately?' to a friend, cousin, or old classmate.",
                "Step outside for 15 minutes of sunlight: Fresh air, natural light, and watching the world move helps reduce the feeling of being trapped inside your head.",
                "Put on a comfort show, music, or good food: Treat your evening like a cozy self-care date with your favorite movie, hot drink, or meal.",
                "Plan one small social activity this week: Look up a local club, gym, gaming group, or hobby community where you can meet people with shared interests."
            ]

        # =========================================================================
        # 16. FEELING STUCK / LOST IN LIFE / NO DIRECTION
        # =========================================================================
        if any(w in t for w in ["stuck", "lost in life", "no purpose", "don't know what to do with my life", "hopeless", "pointless", "unmotivated", "numb", "direction"]):
            return [
                "Remove the pressure to figure out your entire life today: You don't need a 5-year plan right now. You only need a plan for the next 2 hours.",
                "Write down 3 tiny things that used to make you smile: Think back to simple hobbies, games, books, or walks you enjoyed before feeling stuck.",
                "Pick one 10-minute micro-action for today: Clean one corner of your desk, wash the dishes, or take a short walk outside. Small wins build momentum.",
                "Limit scrolling on social media: Watching other people's curated highlight reels will only make you feel more behind. Put your phone away.",
                "Talk to someone whose perspective you trust: Share how you're feeling with a mentor, older sibling, or close friend. Hearing another perspective brings clarity."
            ]

        # =========================================================================
        # 17. FEELING UNAPPRECIATED / MISUNDERSTOOD
        # =========================================================================
        if any(w in t for w in ["unappreciated", "nobody notices", "taken for granted", "ignored", "misunderstood", "no one understands"]):
            return [
                "Anchor your self-worth in your own hands: You know how much effort and care you put in, even if others fail to see it right now.",
                "Write down 3 things you are proud of yourself for: Acknowledge your own kindness, hard work, and small everyday achievements.",
                "Pull back your energy where it isn't respected: Stop over-extending yourself for people who don't reciprocate. Save your energy for those who value you.",
                "Do something entirely for yourself tonight: Cook your favorite comfort food, listen to your playlist, or enjoy a peaceful hobby without guilt.",
                "Express your needs clearly when you feel ready: If this involves someone close, calmly tell them: 'I felt unappreciated when X happened, and I'd like us to talk.'"
            ]

        # =========================================================================
        # 18. PROCRASTINATION, LAZINESS & MOTIVATION LOSS
        # =========================================================================
        if any(w in t for w in ["procrastinat", "lazy", "no motivation", "can't focus", "distracted", "wasting time", "slacking"]):
            return [
                "Use the 2-Minute Rule: Pick the task you're avoiding and commit to doing just 2 minutes of work on it. Starting is the hardest part.",
                "Clear your immediate desk area: Remove clutter, close extra browser tabs, and keep only the single task in front of you.",
                "Put your phone in another room: Eliminate the temptation to scroll by physically separating yourself from devices for 30 minutes.",
                "Work in short 20-minute bursts: Tell yourself: 'I will work for 20 minutes, then take a real 5-minute break.'",
                "Reward yourself for finishing: After completing your focus block, enjoy a snack, check your phone, or stretch."
            ]

        # =========================================================================
        # 19. SELF-DOUBT, IMPOSTER SYNDROME & INSECURITY
        # =========================================================================
        if any(w in t for w in ["imposter", "not good enough", "insecure", "hate myself", "failure", "doubt myself", "everyone is better"]):
            return [
                "Name 3 things you've achieved or learned in the past year: Remind yourself of real obstacles you've already conquered before.",
                "Separate feelings from facts: Feeling like a fraud doesn't mean you are one. You earned your spot through your own effort.",
                "Stop comparing your behind-the-scenes to other people's highlights: People only post their wins online, never their struggles.",
                "Talk to yourself like you would talk to a close friend: You would never tell a friend they're a failure—give yourself that same kindness.",
                "Focus on progress, not perfection: Take one small positive step today rather than trying to be flawless."
            ]

        # =========================================================================
        # 20. GENERAL EMOTION FALLBACKS (HIGHLY DISTINCT PER EMOTION)
        # =========================================================================
        if emotion == "ANXIETY":
            return [
                "Ground your body (5-4-3-2-1): Look around and name 5 things you see, 4 you feel, 3 you hear, 2 you smell, and 1 you taste.",
                "Separate what you can control from what you can't: Focus only on what you can do right now, and let go of the rest for today.",
                "Take one small, concrete action: Pick the simplest 2-minute task in front of you and complete it to get your momentum back.",
                "Step outside or open a window: Fresh air and natural light immediately help slow down a racing nervous system.",
                "Drink a full glass of water: Hydrating and loosening your shoulders sends a biological signal of safety to your brain."
            ]
        elif emotion in ["SADNESS", "DISAPPOINTMENT"]:
            return [
                "Take the weight off your shoulders for the next hour: You don't have to solve everything right now. Just focus on taking care of yourself.",
                "Wash your face with warm water or take a shower: Changing your sensory environment is the fastest way to signal a fresh start to your brain.",
                "Have a warm drink and a small snack: Physical comfort goes a long way in calming an emotionally heavy state.",
                "Write down what's bothering you in 2 sentences: Getting it out on paper takes away its power to swirl inside your head.",
                "Plan one comforting activity before sleep: Put on comfortable clothes, play calming music, or read a book to help your mind settle."
            ]
        elif emotion in ["ANGER", "FRUSTRATION"]:
            return [
                "Step away from the situation immediately: Give yourself a 5-minute timeout before saying or texting anything you might regret.",
                "Release physical tension: Squeeze your hands into tight fists for 5 seconds, then let go completely and shake out your arms.",
                "Write down your unfiltered thoughts privately on paper: Vent everything out on a piece of paper, then tear it up to release the anger.",
                "Go for a brisk walk: Physical movement helps burn off adrenaline and brings your logic back online.",
                "Ask yourself: 'Will this matter in a month?': Put the issue into perspective and choose the most constructive next step."
            ]
        elif emotion == "JOY":
            return [
                "Pause and truly savor this moment: Take 30 seconds to smile and appreciate how good this feels right now.",
                "Share the good news with someone you care about: Call or text a friend or family member—sharing happiness multiplies it.",
                "Write down this feeling in a note: Capture why today was great so you can re-read it whenever you need a boost in the future.",
                "Channel this positive energy: Use this great mood to do something kind for someone else or tackle a fun personal project.",
                "Celebrate your win: Treat yourself to something you enjoy today—you earned this moment."
            ]

        # UNIVERSAL 5 STEPS (WARM, GROUNDED & SIMPLE)
        return [
            "Take 3 deep, steady breaths: Give yourself a moment of quiet pause before doing anything else.",
            "Write down what's on your mind: Getting thoughts out of your head and onto paper immediately creates clarity.",
            "Pick just ONE small step to do right now: Focus on the single smallest action that will make things 5% easier.",
            "Put distractions away for 20 minutes: Turn off notifications and give yourself a calm, focused window to make progress.",
            "Check in with yourself after 30 minutes: Notice how much better it feels once you start taking action."
        ]

    def _build_wellness_suggestion(self, emotion: str, context: str, situation: str, text: str) -> str:
        t = text.lower()
        
        # Specific scenarios with warm, simple, human language
        if ("trip" in t or "vacation" in t or "outing" in t or "party" in t or "travel" in t) and ("exam" in t or "test" in t or "deadline" in t or "study" in t):
            return "Balancing fun and responsibility is all about smart timing. When you finish your core study early, you can enjoy your trip with total peace of mind."

        if any(w in t for w in ["propos", "confess", "tell her", "tell him", "date"]):
            return "Being open about your feelings takes real courage. Whatever happens, be proud that you chose to be genuine and brave."
        
        if any(w in t for w in ["failed my exam", "failed test", "bad marks", "low score", "bad grade"]):
            return "A setback in one test is just data on where to adjust, not a measure of your worth or potential."
            
        if any(w in t for w in ["exam", "study", "homework", "assignment"]):
            return "Your grades do not define your worth as a person. Do your best in focused intervals, get some sleep, and trust the process."
            
        if any(w in t for w in ["rejected from job", "fired", "unemployed", "lost my job"]):
            return "Rejection is often redirection toward a role where your real strengths are truly valued. Keep your head high."
            
        if any(w in t for w in ["interview", "job", "career"]):
            return "An interview is just a mutual conversation to find a good fit. Be confident in the unique skills and energy you bring."
            
        if any(w in t for w in ["breakup", "dumped", "heartbroken", "missing her", "missing him"]):
            return "Your heart is healing even on the days it feels heavy. Be gentle with yourself—you will feel joy again."
            
        if any(w in t for w in ["died", "passed away", "grief", "lost my pet", "lost my dog", "lost my cat"]):
            return "Grief is love that has nowhere to go. Give yourself unlimited patience and compassion as you heal."
            
        if any(w in t for w in ["lonely", "alone", "no friends", "isolated"]):
            return "You are worthy of genuine connection and belonging. Treat yourself with warmth today."
            
        if any(w in t for w in ["stuck", "lost in life", "no purpose", "hopeless"]):
            return "It is okay to not have everything figured out. Life moves in seasons, and this quiet season is preparing you for the next chapter."
            
        if any(w in t for w in ["unappreciated", "nobody notices", "taken for granted"]):
            return "Your value does not decrease based on someone else's inability to see your worth."
            
        if any(w in t for w in ["code", "bug", "project", "work"]):
            return "Every difficult roadblock you solve builds real resilience. Take regular breaks so your mind stays fresh and sharp."
            
        if any(w in t for w in ["sleep", "insomnia", "tired", "exhausted"]):
            return "Your body needs rest to function. Give yourself permission to power down tonight without feeling guilty."
            
        if emotion in ["ANXIETY", "FEAR"]:
            return "You have handled hard days before and you can handle this one too. Take it one breath and one step at a time."
            
        if emotion in ["SADNESS", "DISAPPOINTMENT"]:
            return "Bad days happen, but they always pass. Be kind to yourself today and take things one gentle step at a time."
            
        if emotion in ["ANGER", "FRUSTRATION"]:
            return "Taking a pause before reacting protects your peace of mind and keeps you in control of your response."
            
        if emotion == "JOY":
            return "Happiness feels wonderful. Soak in this moment and let your positive momentum brighten the rest of your day."
        
        return "Small, consistent steps lead to big peace of mind. Stay hydrated, breathe deeply, and take things one moment at a time."

action_recommender = ActionRecommender()
