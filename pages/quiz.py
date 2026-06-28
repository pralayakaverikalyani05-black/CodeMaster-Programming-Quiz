import streamlit as st
from questions.python_questions import python_questions

st.set_page_config(page_title="Python Quiz", page_icon="🐍")

st.title("🐍 Python Quiz")

score = 0

for i, q in enumerate(python_questions):

    st.subheader(f"Question {i+1}")

    answer = st.radio(
        q["question"],
        q["options"],
        key=i
    )

    if answer == q["answer"]:
        score += 1

if st.button("Submit Quiz"):
    st.success(f"🎉 Your Score: {score}/{len(python_questions)}")