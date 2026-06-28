import streamlit as st

st.set_page_config(
    page_title="CodeMaster",
    page_icon="💻",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.main-title{
    font-size:55px;
    text-align:center;
    color:#4F46E5;
    font-weight:bold;
}

.tagline{
    text-align:center;
    font-size:22px;
    color:#555;
}

.card{
    background:#F8F9FA;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:2px 2px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>💻 CodeMaster</div>", unsafe_allow_html=True)

st.markdown("<div class='tagline'>Learn Programming the Smart Way 🚀</div>", unsafe_allow_html=True)

st.write("")

col1, col2 = st.columns(2)

with col1:
    st.button("🚀 Start Quiz", use_container_width=True)

with col2:
    st.button("👤 Login", use_container_width=True)

st.write("")
st.write("## 📚 Choose Your Subject")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.info("🐍 Python")

with c2:
    st.info("☕ Java")

with c3:
    st.info("💙 C")

with c4:
    st.info("🗄 SQL")

st.write("")

st.write("## 🏆 Features")

a,b,c = st.columns(3)

with a:
    st.success("🎯 Practice Coding")

with b:
    st.warning("📈 Track Progress")

with c:
    st.error("🏅 Earn Certificates")

st.write("---")

st.caption("Made with ❤️ by Kalyani")