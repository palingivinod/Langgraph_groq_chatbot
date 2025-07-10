# Q&A Chatbot using LangGraph and Groq API

This project is a simple, single-page chatbot interface built with Streamlit, LangGraph, and Groq's LLM API (Gemma-2 9B-IT). The chatbot processes user input and streams AI-generated responses.


## 🚀 Features

* Real-time Q\&A chatbot using Groq's gemma-2-9b-it model
* Built with LangGraph's StateGraph for flow-based message handling
* Designed for local development with .env secrets handling
* Responsive frontend using Streamlit

## 📦 Requirements

Install dependencies with pip:
bash
pip install streamlit langchain langgraph langchain_groq python-dotenv typing_extensions

## 🔑 Environment Variables

Create a .env file in the root directory with the following content:


LANGSMITH_API_KEY=your_langsmith_key_here
GROQ_API_KEY=your_groq_api_key_here


These will be loaded using python-dotenv.



## 🧠 Model Info

Model: gemma-2-9b-it
Provider: Groq (via langchain_groq)
Tracking: Langsmith (enabled via LANGCHAIN_API_KEY)



## 🧰 Project Structure

├── .env
├── app.py             # Streamlit chatbot application


## 🖥️ How to Run

bash
streamlit run app.py

Then visit http://localhost:8501 in your browser.

## 📤 Deployment (optional)

This app is intended for local use. For deployment:

* You can use Streamlit Cloud or host it on an internal server
* Ensure environment variables are securely managed


Type quit to end the session.

## 🛠 Troubleshooting

* If st.rerun() or Streamlit fails to update, ensure your version is 1.30+
* Missing .env file or keys will raise NoneType errors


This project is open source and free to use for educational and internal prototyping purposes.

## Project Screenshorts

<img width="1920" height="684" alt="image" src="https://github.com/user-attachments/assets/cebf9026-12ac-4b48-af18-744da774e00b" />

AI Response
<img width="1920" height="748" alt="image" src="https://github.com/user-attachments/assets/5705ff16-d522-4fff-a682-818bd7f5b973" />

