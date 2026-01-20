import streamlit as st
import math

st.title("📚 Study Planner & Skill Tracker")

st.markdown("""
This module helps you:
- Create a **personalized study timetable**
- Track **skill learning progress** over time
""")

st.divider()

# ==================================================
# SESSION STATE INITIALIZATION
# ==================================================
if "skills_progress" not in st.session_state:
    st.session_state.skills_progress = {}

# ==================================================
# SECTION 1 — STUDY TIMETABLE GENERATOR
# ==================================================
st.subheader("🕒 Study Timetable Generator")

skill = st.text_input("Skill / Subject to Study", placeholder="e.g., Python, SQL, Machine Learning")
daily_hours = st.slider("Daily Study Hours", 1, 6, 2)
weeks = st.slider("Duration (Weeks)", 1, 12, 4)

if st.button("📅 Generate Timetable"):
    if not skill.strip():
        st.error("Please enter a skill or subject.")
    else:
        total_days = weeks * 7
        total_hours = total_days * daily_hours

        st.success(f"📌 Total Study Time: **{total_hours} hours**")

        st.markdown("### 🗓 Weekly Study Plan")

        topics = [
            "Basics & Fundamentals",
            "Core Concepts",
            "Hands-on Practice",
            "Mini Projects",
            "Revision & Assessment"
        ]

        days_per_topic = math.ceil(total_days / len(topics))

        day = 1
        for topic in topics:
            if day > total_days:
                break
            st.markdown(f"**Days {day}–{min(day+days_per_topic-1, total_days)}:** {skill} – {topic}")
            day += days_per_topic

        st.info("💡 Tip: Use the Chatbot to ask doubts while following this timetable.")

st.divider()

# ==================================================
# SECTION 2 — SKILL PROGRESS TRACKER
# ==================================================
st.subheader("📈 Skill Progress Tracker")

new_skill = st.text_input("Add a Skill to Track", placeholder="e.g., Python")

if st.button("➕ Add Skill"):
    if new_skill.strip():
        st.session_state.skills_progress[new_skill] = 0
        st.success(f"Skill **{new_skill}** added!")
    else:
        st.error("Please enter a skill name.")

st.markdown("### 🔍 Track Your Progress")

if not st.session_state.skills_progress:
    st.info("No skills added yet.")
else:
    for skill_name in list(st.session_state.skills_progress.keys()):
        col1, col2 = st.columns([3, 1])

        with col1:
            progress = st.slider(
                f"{skill_name} Progress (%)",
                0, 100,
                st.session_state.skills_progress[skill_name],
                key=skill_name
            )
            st.session_state.skills_progress[skill_name] = progress
            st.progress(progress / 100)

        with col2:
            if st.button("❌ Remove", key=f"remove_{skill_name}"):
                del st.session_state.skills_progress[skill_name]
                st.experimental_rerun()

st.divider()

# ==================================================
# INSIGHTS
# ==================================================
st.subheader("🧠 Learning Insights")

if st.session_state.skills_progress:
    avg_progress = sum(st.session_state.skills_progress.values()) / len(st.session_state.skills_progress)
    st.metric("📊 Average Skill Progress", f"{int(avg_progress)}%")

    if avg_progress < 40:
        st.warning("You are at an early stage. Stay consistent!")
    elif avg_progress < 70:
        st.info("Good progress. Increase practice time.")
    else:
        st.success("Excellent! You are close to mastery.")
