# 🤖 AI Career Assistant

AI Career Assistant is a Python-based web application built using Streamlit.  
It helps students and freshers by providing career guidance, resume tips, and skill development suggestions through a simple chatbot interface.

This project is designed to be easy to understand, modify, and extend.

---

## 🚀 Features

- Career guidance based on user queries
- Resume assistance and suggestions
- Study roadmap and skill recommendations
- Interactive chatbot interface
- Clean and modular project structure

---

## 🧠 How the Application Works

1. The user enters a question in the chatbot.
2. The system matches the input with predefined intents.
3. Responses are generated using rule-based logic.
4. The response is displayed on the Streamlit web interface.

---

## 🗂 Project Structure

AI_Career_Guidence/
│
├── app.py
├── README.md
├── .gitignore
│
├── data/
│ └── intents.json
│
├── pages/
│ ├── 1_home.py
│ ├── 2_Roadmap.py
│ ├── 3_Chatbot.py
│ ├── 4_Resume.py
│ └── 5_Study_and_Skills.py
│
├── utils/
│ ├── ai_chatbot.py
│ └── train_model.py


---

## ▶️ How to Run the Project

### Prerequisites
- Python 3.9 or above
- pip installed

---

### Steps to Run

```bash
git clone https://github.com/Nisthula268/AI_Career_Guidence.git
cd AI_Career_Guidence
pip install streamlit
streamlit run app.py
The application will open in your browser at:

http://localhost:8501
🌐 Deployment
The project can be deployed using Streamlit Community Cloud.

Push the project to GitHub

Go to https://share.streamlit.io

Select the repository

Choose branch main and file app.py

Click Deploy

👤 Author
Name: Nisthula
Email: nisthula268@gmail.com
GitHub: https://github.com/Nisthula268

📜 License
This project is developed for academic and learning purposes.
