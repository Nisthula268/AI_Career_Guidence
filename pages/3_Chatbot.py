import streamlit as st
from utils.ai_chatbot import get_ai_reply, get_career_clarity_score

st.title("🤖 AI Career Chatbot")
st.markdown("Ask questions about **careers, skills, resumes, interviews, or studies**.")

# =========================================
# SESSION STATE INITIALIZATION
# =========================================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================================
# SIDEBAR CONTROLS
# =========================================
st.sidebar.subheader("💬 Chat Controls")

if st.sidebar.button("🆕 New Chat"):
    st.session_state.chat_history = []
    st.sidebar.success("New chat started!")

st.sidebar.subheader("📊 Career Clarity")
st.sidebar.progress(get_career_clarity_score() / 100)
st.sidebar.write(f"{get_career_clarity_score()}% clarity")

# =========================================
# DISPLAY CHAT HISTORY
# =========================================
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"🧑 **You:** {chat['message']}")
    else:
        st.markdown(f"🤖 **AI:** {chat['message']}")

st.divider()

# =========================================
# USER INPUT
# =========================================
user_input = st.text_input("Type your message:")

if st.button("Send") and user_input.strip():
    # Store user message
    st.session_state.chat_history.append(
        {"role": "user", "message": user_input}
    )

    # Get AI response
    ai_reply = get_ai_reply(user_input)

    # Store AI message
    st.session_state.chat_history.append(
        {"role": "ai", "message": ai_reply}
    )

    # Correct rerun method (FIXED)
    st.rerun()
