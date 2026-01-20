import streamlit as st
import re

st.title("📄 AI Resume Intelligence & Scoring")

st.markdown("""
This module **reads your entire resume** and evaluates it using
**multi-factor scoring logic**, similar to real-world screening systems.
""")

# -----------------------------
# Input
# -----------------------------
resume_text = st.text_area(
    "📌 Paste your full resume text below:",
    height=300
)

career = st.selectbox(
    "🎯 Target Career Role",
    [
        "Software Developer",
        "Data Analyst",
        "AI / ML Engineer",
        "Web Developer",
        "General"
    ]
)

# -----------------------------
# Knowledge Base
# -----------------------------
CAREER_KEYWORDS = {
    "Software Developer": ["java", "python", "coding", "project", "problem solving"],
    "Data Analyst": ["python", "sql", "excel", "data analysis", "power bi", "tableau"],
    "AI / ML Engineer": ["python", "machine learning", "model", "data", "statistics"],
    "Web Developer": ["html", "css", "javascript", "react", "frontend", "backend"],
    "General": ["project", "skill", "internship", "certification"]
}

SECTIONS = ["skill", "project", "internship", "experience", "certification", "education"]

ACTION_WORDS = [
    "developed", "built", "implemented", "designed",
    "created", "analyzed", "optimized", "worked"
]

# -----------------------------
# Helper functions
# -----------------------------
def clean(text):
    text = text.lower()
    return re.sub(r"[^a-z\s]", "", text)

def count_presence(text, words):
    return sum(1 for w in words if w in text)

# -----------------------------
# Analysis
# -----------------------------
if st.button("🧠 Analyze Resume"):
    if not resume_text.strip():
        st.error("Please paste your resume text.")
    else:
        text = clean(resume_text)

        # 1️⃣ Section Coverage (20)
        section_count = count_presence(text, SECTIONS)
        section_score = min(section_count * 4, 20)

        # 2️⃣ Skill Density (20)
        skill_score = min(len(re.findall(r"\b(skill|technology|tool)\b", text)) * 5, 20)

        # 3️⃣ Project Quality (20)
        project_score = min(count_presence(text, ACTION_WORDS) * 4, 20)

        # 4️⃣ Experience / Internship (20)
        experience_score = 20 if ("internship" in text or "experience" in text) else 10

        # 5️⃣ ATS Keyword Match (20)
        keywords = CAREER_KEYWORDS[career]
        matched = count_presence(text, keywords)
        ats_score = int((matched / len(keywords)) * 20)

        # TOTAL
        total_score = (
            section_score +
            skill_score +
            project_score +
            experience_score +
            ats_score
        )

        # -----------------------------
        # Display Results
        # -----------------------------
        st.subheader("📊 Resume Scoring Breakdown")

        st.write(f"📁 Section Coverage: **{section_score}/20**")
        st.write(f"🛠 Skill Density: **{skill_score}/20**")
        st.write(f"🚀 Project Quality: **{project_score}/20**")
        st.write(f"🏢 Experience / Internship: **{experience_score}/20**")
        st.write(f"🤖 ATS Keyword Match: **{ats_score}/20**")

        st.divider()

        st.metric("🏆 Final Resume Score", f"{total_score} / 100")

        # -----------------------------
        # Interpretation
        # -----------------------------
        if total_score < 40:
            st.error("❌ Resume is weak. Needs major improvement.")
        elif total_score < 70:
            st.warning("⚠ Resume is average. Improve skills and projects.")
        else:
            st.success("✅ Resume is strong and job-ready!")

        # -----------------------------
        # Suggestions
        # -----------------------------
        st.subheader("🛠 Improvement Suggestions")

        if section_score < 15:
            st.write("- Add missing resume sections like skills, projects, or certifications.")
        if project_score < 15:
            st.write("- Describe projects using action words (developed, built, implemented).")
        if ats_score < 15:
            st.write("- Include more role-specific keywords for better ATS performance.")
