import streamlit as st
from langchain_groq import ChatGroq
from tools import search_tool

# ✅ Load API Key safely
api_key = st.secrets["GROQ_API_KEY"]

# ✅ Create LLM (GLOBAL)
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant"
)

# ✅ LLM function
def ask_llm(prompt):
    response = llm.invoke(prompt)
    return response.content


# ✅ MAIN AGENT FUNCTION
def autonomous_agent_new(user_task, max_steps=5):
    memory = []
    context = ""

    for step in range(max_steps):

        prompt = f"""
You are JARVIS AI.

Task: {user_task}

Memory:
{context}

Decide next step:
- THINK
- SEARCH
- FINAL

Format:
ACTION:
CONTENT:
"""

        response = ask_llm(prompt)

        memory.append(response)
        context += "\n" + response

        # 🔍 SEARCH ACTION
        if "SEARCH" in response:
            query = response.split("CONTENT:")[-1].strip()
            results = search_tool(query)
            context += "\n" + "\n".join(results)

        # ✅ FINAL ANSWER
        if "FINAL" in response:
            return {
                "steps": memory,
                "final": response
            }

    return {"steps": memory, "final": "Stopped"}
