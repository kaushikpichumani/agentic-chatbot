# 🧠 Basic LangGraph Chatbot (Python)

A **minimal, modular chatbot** built using **LangGraph** and **LangChain**, designed to demonstrate how to define **state**, **nodes**, **edges**, and **graph execution** in a clean Python project.

This repository intentionally keeps complexity low so developers can **clearly understand agentic workflows** before scaling to multi-agent or tool-based systems.

---

## ✨ Features

- ✅ LangGraph-based conversational workflow
- ✅ Clear separation of **LLM**, **state**, **nodes**, and **graph**
- ✅ Groq LLM integration
- ✅ Streamlit UI for interactive chatting
- ✅ Beginner-friendly and extensible design
- ✅ Ideal for learning LangGraph fundamentals

---

## 🗂️ Project Structure

BasicChatbot/
│
├── app.py                     # Entry point
├── requirements.txt           # Python dependencies
├── .gitignore
│
├── src/
│   └── langgraphagenticai/
│       ├── graph/
│       │   └── graph_builder.py     # LangGraph definition (nodes & edges)
│       │
│       ├── nodes/
│       │   └── basic_chatbot_node.py # Chatbot node logic
│       │
│       ├── state/
│       │   └── state.py              # Graph state definition
│       │
│       ├── LLMS/
│       │   └── groqllm.py             # Groq LLM wrapper
│       │
│       └── ui/
│           ├── uiconfigfile.ini
│           └── streamlitui/
│               ├── loadui.py          # UI loader
│               └── display_result.py  # Chat output renderer


## ⚙️ Installation

### 1️⃣ Clone the repository

git clone https://github.com/your-username/basic-langgraph-chatbot.git
cd basic-langgraph-chatbot


python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

## Install requirements.txt to install dependencies 
pip install -r requirements.txt

## run the streamlit app by giving the below command

streamlit run app.py



How It Works
1️⃣ State (state.py)

Defines the structure of data flowing through the graph (e.g., user input and model response).

2️⃣ Node (basic_chatbot_node.py)

Implements the chatbot logic:

Receives user input

Calls the LLM

Updates and returns state

3️⃣ Graph (graph_builder.py)

Registers nodes

Defines execution order

Compiles the LangGraph

4️⃣ UI (Streamlit)

Captures user input

Executes the LangGraph

Displays the chatbot response
