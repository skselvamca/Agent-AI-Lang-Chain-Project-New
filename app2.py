import streamlit as st
from autonomous_agent_new import autonomous_agent_new
from file_reader import read_pdf

# 🔥 Page Config
st.set_page_config(
    page_title="JARVIS AI",
    page_icon="🤖",
    layout="wide"
)

# 🎨 Custom CSS for Professional Look
st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
.stTextInput>div>div>input {
    background-color: #1E1E1E;
    color: white;
    border-radius: 10px;
}
.stButton>button {
    border-radius: 10px;
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
}
.chat-box {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# 🧭 Sidebar
with st.sidebar:
    st.title("🤖 JARVIS AI")
    st.markdown("### ⚙️ Settings")
    max_steps = st.slider("Max Steps", 1, 10, 5)
    st.markdown("---")
    st.markdown("### 📌 About")
    st.write("Autonomous AI Agent using LangChain + Groq")
    st.markdown("Made by Selvam Kumar 🚀")

# 🏠 Main Header
st.title("🤖 JARVIS AI Assistant")
st.markdown("### Your Autonomous AI Agent")

# 💬 User Input
user_input = st.text_input("💡 Enter your task:")

# 🚀 Run Button
if st.button("Run Agent"):

    if user_input.strip() == "":
        st.warning("Please enter a task!")
    else:
        with st.spinner("JARVIS is thinking... 🤔"):
            result = autonomous_agent_new(user_input, max_steps=max_steps)

        st.success("Task Completed ✅")

        # 🧠 Steps Output
        st.subheader("🧠 Agent Thinking Steps")
        for step in result["steps"]:
            st.markdown(f'<div class="chat-box">{step}</div>', unsafe_allow_html=True)

        # 🎯 Final Answer
        st.subheader("🎯 Final Answer")
        st.markdown(f'<div class="chat-box">{result["final"]}</div>', unsafe_allow_html=True)
