import streamlit as st

st.set_page_config(
    page_title="AI Career Guidance System",
    layout="wide"
)

# =============================
# SIDEBAR ACTIVE PAGE HIGHLIGHT (NEW)
# =============================
st.markdown(
    """
    <style>
    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #1f1f2e;
    }

    /* Sidebar links */
    section[data-testid="stSidebar"] a {
        color: #d1d5db !important;
        font-size: 16px;
        padding: 8px 12px;
        border-radius: 6px;
        display: block;
        text-decoration: none;
    }

    /* Hover effect */
    section[data-testid="stSidebar"] a:hover {
        background-color: #2e2e42;
        color: #ffffff !important;
    }

    /* ACTIVE PAGE */
    section[data-testid="stSidebar"] a[aria-current="page"] {
        background-color: #2563eb !important;
        color: #ffffff !important;
        font-weight: 700;
        border-left: 6px solid #22c55e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================
# HEADER
# =============================
st.markdown(
    """
    <h1 style='text-align: center;'>🎯 AI Career Guidance & Resume Intelligence System</h1>
    <p style='text-align: center; font-size:18px;'>
    An AI-powered platform to guide students and freshers in careers, skills, and resumes
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# =============================
# METRICS ROW
# =============================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🤖 AI Engine", "ML-Based")

with col2:
    st.metric("📄 Resume Score", "0 – 100")

with col3:
    st.metric("🎯 Career Paths", "10+")

with col4:
    st.metric("🧠 Decision Support", "Enabled")

st.divider()

# =============================
# MAIN CONTENT (2 COLUMNS)
# =============================
left, right = st.columns([2, 1])

with left:
    st.subheader("🚀 What This Application Does")

    st.markdown("""
    This system acts as a **career decision-support platform**, not just a chatbot.

    🔹 Understands user questions using **Machine Learning (NLP)**  
    🔹 Guides users through **career selection and skill development**  
    🔹 Reads and evaluates **entire resumes**  
    🔹 Assigns **marks based on real screening logic**  
    🔹 Helps users become **job-ready**
    """)

    st.subheader("🧠 AI Capabilities")

    st.markdown("""
    - Supervised ML-based intent classification  
    - Confidence-aware response generation  
    - Skill gap detection  
    - Resume intelligence & scoring  
    - Career clarity analysis  
    """)

with right:
    st.subheader("📌 Quick Navigation")

    st.info("Use the sidebar to explore modules")

    st.markdown("""
    👉 **Home** – Overview of the system  
    👉 **Roadmap** – Step-by-step career planning  
    👉 **Chatbot** – Ask career & skill questions  
    👉 **Resume** – Analyze resume strength  
    """)

    st.success("⬅ Select a page from the sidebar")

st.divider()

# =============================
# FEATURE CARDS
# =============================
st.subheader("🔑 Key Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    ### 🤖 AI Career Chatbot
    - Learns from training data  
    - Handles unseen questions  
    - Avoids random answers  
    """)

with c2:
    st.markdown("""
    ### 📄 Resume Intelligence
    - Reads full resume text  
    - Multi-factor scoring  
    - ATS-style evaluation  
    """)

with c3:
    st.markdown("""
    ### 🎯 Decision Support
    - Skill gap detection  
    - Career clarity score  
    - Actionable guidance  
    """)

st.divider()

# =============================
# EXPANDERS
# =============================
with st.expander("📘 How is this different from normal chatbots?"):
    st.markdown("""
    - Traditional chatbots are **rule-based**
    - This system uses **machine learning models**
    - Decisions are **data-driven and explainable**
    - Resume evaluation uses **real-world screening logic**
    """)

with st.expander("🎓 Who can use this system?"):
    st.markdown("""
    - College students  
    - Fresh graduates  
    - Job seekers  
    - Career switchers  
    """)

with st.expander("🛠 Technologies Used"):
    st.markdown("""
    - Python  
    - Streamlit  
    - Scikit-learn  
    - TF-IDF Vectorization  
    - Logistic Regression  
    """)

st.divider()

# =============================
# CALL TO ACTION
# =============================
st.success(
    "🚀 Start by selecting **Chatbot** or **Resume** from the sidebar to experience AI-powered guidance."
)
