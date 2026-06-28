import streamlit as st

st.set_page_config(
    page_title="CodeMaster",
    page_icon="💻",
    layout="wide"
)

# ---------------- HERO SECTION ---------------- #

st.markdown("""
<h1 style='text-align:center;
color:#4F46E5;
font-size:60px;'>
💻 CodeMaster
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;color:gray;'>
Learn Programming the Smart Way 🚀
</h3>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.button("🚀 Start Learning", use_container_width=True)
    st.button("👤 Login", use_container_width=True)

st.write("---")

st.markdown("## 📚 Choose Your Subject")

col1, col2 = st.columns(2)

with col1:
    st.success("🐍 Python")
    st.success("💙 C Programming")

with col2:
    st.info("☕ Java")
    st.info("🗄 SQL")

st.write("---")

st.markdown("## 🌟 Why CodeMaster?")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Questions", "1000+")

with c2:
    st.metric("Subjects", "4")

with c3:
    st.metric("Certificates", "Unlimited")

st.write("---")

st.caption("Made with ❤️ by Kalyani")