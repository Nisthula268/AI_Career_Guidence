import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load data
with open("data/intents.json") as f:
    intents = json.load(f)["intents"]

X = []
y = []

for intent in intents:
    for pattern in intent["patterns"]:
        X.append(pattern)
        y.append(intent["tag"])

# Vectorize text
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vec, y)

# Save model
joblib.dump(model, "utils/model.pkl")
joblib.dump(vectorizer, "utils/vectorizer.pkl")

print("Model trained successfully")
