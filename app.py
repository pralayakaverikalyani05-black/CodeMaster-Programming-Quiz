import streamlit as st

st.set_page_config(
    page_title="CodeMaster",
    page_icon="💻",
    layout="wide"
)

st.markdown("""
# 💻 CodeMaster

### AI-Powered Programming Quiz Platform

Welcome to **CodeMaster**.

Improve your Programming Skills with interactive quizzes.

---
""")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Start Quiz", use_container_width=True):
        st.info("Quiz module is coming soon!")

with col2:
    if st.button("👤 Login", use_container_width=True):
        st.info("Login page is coming soon!")

st.markdown("---")

st.subheader("📚 Available Subjects")

st.write("🐍 Python")
st.write("☕ Java")
st.write("💙 C Programming")
st.write("🗄 SQL")

st.markdown("---")

st.caption("Developed by Kalyani ❤️")
st.markdown("""
### 🚀 Why Choose CodeMaster?

✅ Practice Programming Questions

✅ Improve Coding Skills

✅ Track Your Progress

✅ AI Explanations (Coming Soon)

✅ Earn Certificates (Coming Soon)

✅ Leaderboard (Coming Soon)
""")