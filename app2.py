import streamlit as st
from autonomous_agent_new import autonomous_agent_new
from file_reader import read_pdf

# 🔥 Page config
st.set_page_config(
    page_title="JARVIS AI Dashboard",
    page_icon="🤖",
    layout="wide"
)

# 🎨 PROFESSIONAL CSS (Gradient + Clean UI)
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #1f4037, #99f2c8);
}
.main {
    background-color: transparent;
}

/* Input box */
.stTextArea textarea {
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
}

/* Buttons */
.stButton>button {
    border-radius: 12px;
    background: linear-gradient(45deg, #4CAF50, #2E7D32);
    color: white;
    font-weight: bold;
    height: 50px;
}

/* Cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    margin-bottom: 15px;
}

/* Header */
h1, h2, h3 {
    color: #1f4037;
}
</style>
""", unsafe_allow_html=True)

# 🧭 Sidebar
with st.sidebar:
    st.title("🤖 JARVIS AI")
    st.markdown("### ⚙️ Settings")
    max_steps = st.slider("Max Steps", 1, 10, 5)

    st.markdown("---")
    st.markdown("### 📂 Upload PDF")
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

    st.markdown("---")
    st.markdown("Made by Selvam Kumar 🚀")

# 📄 PDF READER FUNCTION
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
pdf_text = ""
if uploaded_file is not None:
    pdf_text = read_pdf(uploaded_file)
    st.success("PDF uploaded successfully ✅")

# 🏠 HEADER
st.title("🤖 JARVIS AI Dashboard")
st.subheader("Autonomous AI Agent with Thinking + Search + Analysis")

# 💬 BIG INPUT AREA
user_input = st.text_area(
    "💡 Enter your task:",
    height=150,
    placeholder="Type your complex task here..."
)

# 🚀 RUN BUTTON
if st.button("🚀 Run Agent"):

    if user_input.strip() == "":
        st.warning("Please enter a task!")
    else:
        with st.spinner("JARVIS is thinking... 🤔"):
            
            # Combine PDF + User Input
            final_input = user_input
            if pdf_text:
                final_input += f"\n\nUse this PDF content:\n{pdf_text[:2000]}"

            result = autonomous_agent_new(final_input, max_steps=max_steps)

        st.success("Task Completed ✅")

        # 🧠 STEPS
        st.markdown("## 🧠 Agent Thinking")
        for step in result["steps"]:
            st.markdown(f'<div class="card">{step}</div>', unsafe_allow_html=True)

        # 🎯 FINAL OUTPUT
        st.markdown("## 🎯 Final Answer")
        st.markdown(f'<div class="card">{result["final"]}</div>', unsafe_allow_html=True)
