import streamlit as st

# -------------------- PAGE SETTINGS --------------------
st.set_page_config(
    page_title="CodeMaster",
    page_icon="💻",
    layout="wide"
)

# -------------------- HERO BANNER --------------------
st.image("assets/hero_banner.png", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------- BUTTONS --------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Start Learning", use_container_width=True):
        st.success("Quiz Module Coming Soon!")

with col2:
    if st.button("👤 Login", use_container_width=True):
        st.info("Login Page Coming Soon!")

st.write("")
st.write("---")

# -------------------- SUBJECTS --------------------
st.markdown("## 📚 Choose Your Subject")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🐍 Python")

with col2:
    st.info("☕ Java")

with col3:
    st.info("💙 C Programming")

with col4:
    st.info("🗄 SQL")

st.write("")
st.write("---")

# -------------------- FEATURES --------------------
st.markdown("## 🌟 Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("🎯 1000+ Programming Questions")

with c2:
    st.warning("📈 Track Your Progress")

with c3:
    st.success("🏆 Earn Certificates")

st.write("")

c4, c5, c6 = st.columns(3)

with c4:
    st.info("🤖 AI Explanations")

with c5:
    st.info("🥇 Leaderboard")

with c6:
    st.info("📊 Performance Analytics")

st.write("")
st.write("---")

# -------------------- ABOUT --------------------
st.markdown("## 💡 About CodeMaster")

st.write("""
CodeMaster is an AI-powered Programming Quiz Platform where students can:

- ✅ Practice Programming Questions
- ✅ Improve Coding Skills
- ✅ Track Performance
- ✅ Compete on Leaderboards
- ✅ Earn Certificates
- ✅ Learn with AI Explanations
""")

st.write("---")

# -------------------- FOOTER --------------------
st.markdown(
    "<center>❤️ Developed by <b>Kalyani</b> | CodeMaster 2026</center>",
    unsafe_allow_html=True
)