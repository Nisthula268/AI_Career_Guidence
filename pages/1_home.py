import streamlit as st

st.title("🏠 Home – AI Career Guidance System")

st.markdown("""
Welcome to the **AI Career Guidance & Resume Intelligence System**.

This application is designed to help **students and fresh graduates**
make informed career decisions using **Machine Learning–based intelligence**.
""")

st.divider()

# =============================
# PROBLEM STATEMENT
# =============================
st.subheader("❓ Problem Statement")

st.markdown("""
Many students face difficulties such as:
- Confusion in choosing the right career path  
- Not knowing which skills are required for specific jobs  
- Weak resumes that fail to pass initial screening  
- Lack of structured guidance after graduation  

Existing platforms often provide **generic advice** or **static content**
that does not adapt to individual users.
""")

# =============================
# SOLUTION OVERVIEW
# =============================
st.subheader("💡 Proposed Solution")

st.markdown("""
This system provides a **personalized, AI-powered solution** by combining:

- Machine Learning–based chatbot for career guidance  
- Resume intelligence module that evaluates resumes objectively  
- Skill gap detection for targeted career roles  
- Structured career roadmaps for step-by-step planning  

The goal is to act as a **career decision-support system**, not just an information bot.
""")

st.divider()

# =============================
# HOW AI IS USED
# =============================
st.subheader("🤖 How Artificial Intelligence is Used")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **AI Techniques Used**
    - Natural Language Processing (NLP)
    - TF-IDF text vectorization
    - Supervised Machine Learning
    - Confidence-aware prediction logic
    """)

with col2:
    st.markdown("""
    **What AI Does Here**
    - Understands user questions  
    - Predicts user intent probabilistically  
    - Avoids random answers when confidence is low  
    - Analyzes resume text using multi-factor logic  
    """)

st.divider()

# =============================
# SYSTEM WORKFLOW
# =============================
st.subheader("🔄 System Workflow")

st.markdown("""
1️⃣ User enters a question or resume text  
2️⃣ Text is preprocessed and analyzed  
3️⃣ Machine Learning model predicts intent or relevance  
4️⃣ Confidence threshold is applied  
5️⃣ System generates guidance, scores, and suggestions  
""")

st.divider()

# =============================
# KEY MODULES
# =============================
st.subheader("🧩 Key Modules in the Application")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    ### 🤖 Career Chatbot
    - ML-based intent recognition  
    - Skill gap detection  
    - Follow-up mentoring questions  
    """)

with c2:
    st.markdown("""
    ### 📄 Resume Intelligence
    - Reads entire resume text  
    - Scores resume out of 100  
    - ATS-style keyword evaluation  
    """)

with c3:
    st.markdown("""
    ### 🗺️ Career Roadmap
    - Step-by-step guidance  
    - Skills → Projects → Jobs  
    - Interview preparation flow  
    """)

st.divider()

# =============================
# WHY THIS PROJECT IS UNIQUE
# =============================
st.subheader("🌟 Why This Project Is Unique")

st.markdown("""
✔ Uses **Machine Learning**, not rule-based logic  
✔ Works completely **offline** (no APIs, no billing)  
✔ Provides **explainable and transparent scoring**  
✔ Combines chatbot + resume analysis + decision support  
✔ Designed for **academic evaluation and real use**
""")

st.divider()

# =============================
# WHO SHOULD USE THIS
# =============================
st.subheader("🎓 Who Can Use This System?")

st.markdown("""
- College students exploring career options  
- Fresh graduates preparing for jobs  
- Students improving resumes and skills  
- Anyone seeking structured career guidance  
""")

st.divider()

# =============================
# CALL TO ACTION
# =============================
st.success("""
👉 Navigate using the **sidebar** to explore:
- **Chatbot** for AI-based career guidance  
- **Resume** for resume analysis and scoring  
- **Roadmap** for structured career planning  
""")
