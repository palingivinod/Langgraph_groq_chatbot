import streamlit as st
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
import os
from typing import Annotated
from typing_extensions import TypedDict
from dotenv import load_dotenv
load_dotenv()

langsmith_api = os.getenv("LANGSMITH_API_KEY")
groq_api_key = os.getenv("groq_api_key")
os.environ["LANGCHAIN_API_KEY"]=langsmith_api
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="chatbot"

llm = ChatGroq(groq_api_key=groq_api_key,model_name="gemma2-9b-it")

class State(TypedDict):
    messages:Annotated[list,add_messages]
graph_builder = StateGraph(State)


def chatbot(state:State):
    return {"messages":llm.invoke(state['messages'])}

graph_builder.add_node("chatbot",chatbot)
graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot",END)

graph=graph_builder.compile()
st.title("Q&A Chatbot using Langgraph & Groq_api")


user_input = st.text_input("Ask question..")

if user_input:
    if user_input.lower() == "quit":
        st.write("Assistant: Good bye")
        st.stop()   
    else:
        for event in graph.stream({"messages": ("user", user_input)}):
            for value in event.values():
                assistant_response = value["messages"].content
                st.write("Assistant:  ",assistant_response)
               

       
