import streamlit as st
from autonomous_agent_new import autonomous_agent_new
from file_reader import read_pdf

# 🔥 Page Config
st.set_page_config(
    page_title="JARVIS AI Dashboard",
    page_icon="🤖",
    layout="wide"
)

# 🎨 UI STYLE
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #1f4037, #99f2c8);
}
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 10px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
}
.stButton>button {
    border-radius: 10px;
    height: 50px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 🧭 Sidebar
with st.sidebar:
    st.title("🤖 JARVIS AI")
    max_steps = st.slider("Max Steps", 1, 10, 5)

    uploaded_file = st.file_uploader("📂 Upload PDF", type=["pdf"])

# 📄 Read PDF
pdf_text = ""
if uploaded_file:
    pdf_text = read_pdf(uploaded_file)
    st.success("PDF uploaded successfully ✅")

    # 🔍 Debug preview
    st.write("Preview:", pdf_text[:300])

# 🏠 Main UI
st.title("🤖 JARVIS AI Dashboard")

user_input = st.text_area("💡 Enter your task:", height=150)

if st.button("🚀 Run Agent"):

    if user_input.strip() == "":
        st.warning("Enter a task")
    else:
        with st.spinner("Thinking... 🤔"):

            final_input = user_input
            if pdf_text:
                final_input += f"\n\nUse this PDF:\n{pdf_text[:2000]}"

            result = autonomous_agent_new(final_input, max_steps=max_steps)

        st.success("Done ✅")

        # 🧠 Steps
        st.subheader("🧠 Thinking Steps")
        for step in result["steps"]:
            st.markdown(f'<div class="card">{step}</div>', unsafe_allow_html=True)

        # 🎯 Final
        st.subheader("🎯 Final Answer")
        st.markdown(f'<div class="card">{result["final"]}</div>', unsafe_allow_html=True)
