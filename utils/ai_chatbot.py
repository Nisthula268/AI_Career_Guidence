import json
import random
import joblib

# =========================================
# Load trained model and vectorizer
# =========================================
model = joblib.load("utils/model.pkl")
vectorizer = joblib.load("utils/vectorizer.pkl")

# =========================================
# Load intents
# =========================================
with open("data/intents.json", "r") as f:
    intents = json.load(f)["intents"]

CONFIDENCE_THRESHOLD = 0.4

# =========================================
# Memory & analytics
# =========================================
last_response = None
career_confusion = 0   # <-- REQUIRED for clarity score

# =========================================
# AI reply function
# =========================================
def get_ai_reply(user_input: str) -> str:
    global last_response, career_confusion

    # Vectorize input
    vec = vectorizer.transform([user_input])

    # Predict probabilities
    probs = model.predict_proba(vec)[0]
    max_prob = max(probs)

    # Low confidence fallback
    if max_prob < CONFIDENCE_THRESHOLD:
        career_confusion += 1
        return "I'm not confident about that. Could you please rephrase your question?"

    # Predicted intent
    intent = model.classes_[probs.argmax()]

    # Debug (optional)
    print(f"Predicted intent: {intent}, Confidence: {max_prob:.2f}")

    # Select response (avoid repetition)
    for item in intents:
        if item["tag"] == intent:
            responses = item["responses"]
            response = random.choice(responses)

            if response == last_response and len(responses) > 1:
                response = random.choice(responses)

            last_response = response
            return response

    return "Sorry, I couldn't understand that."

# =========================================
# Career clarity score (FIXES YOUR ERROR)
# =========================================
def get_career_clarity_score() -> int:
    """
    Returns a career clarity score out of 100.
    More confusion → lower score.
    """
    return max(0, 100 - career_confusion * 10)
