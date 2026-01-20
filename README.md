# AI Career Assistant 🤖

AI Career Assistant is a Python-based chatbot designed to help students and freshers with
career guidance, resume support, and study/skill recommendations.

⚠️ **Note:** This project is a **rule-based chatbot with optional machine learning support**.  
It is **not a generative AI system** (like ChatGPT), but a structured chatbot built for learning and guidance purposes.

---

## 🚀 Features

- Career guidance based on user queries
- Resume-related assistance
- Study and skill roadmap suggestions
- Modular page-based application design
- Easy to extend with Machine Learning or NLP models

---

## 🧠 How It Works

1. The user enters a query through the application interface.
2. The chatbot matches the query with predefined intents.
3. Responses are generated using:
   - **Rule-based logic** defined in `intents.json`
   - **Optional ML-based classification** (if a trained model is available)
4. The appropriate response is displayed to the user.

---

## 🗂 Project Structure

AI_Career_Assistant/
│
├── app.py # Main entry point of the application
├── README.md # Project documentation
├── .gitignore
│
├── data/
│ └── intents.json # Intent and response definitions
│
├── pages/
│ ├── 1_home.py # Home page
│ ├── 2_Roadmap.py # Career roadmap page
│ ├── 3_Chatbot.py # Chatbot interface
│ ├── 4_Resume.py # Resume guidance page
│ └── 5_Study_and_Skills.py
│
├── utils/
│ ├── ai_chatbot.py # Core chatbot logic
│ └── train_model.py # Optional ML model training script


---

## ▶️ How to Run the Project

1. Make sure **Python 3.9 or above** is installed on your system.

2. Clone the repository:
   ```bash
   git clone https://github.com/Pavithraa2005/AI-_Career_Assistant.git
Navigate to the project directory:

cd AI-_Career_Assistant
Run the application:

python app.py
📦 Requirements
Python 3.9 or higher

Standard Python libraries

(Optional) Machine Learning libraries if training the model

🔮 Future Improvements
Integrate NLP libraries such as spaCy or NLTK

Replace rule-based logic with a full ML/NLP-based chatbot

Add user authentication and profile tracking

Deploy the application using Streamlit or Flask

Connect to a database for persistent data storage

👩‍💻 Author
Pavithra
Undergraduate Student | Aspiring Software Engineer
Interested in AI, software development, and career-oriented applications