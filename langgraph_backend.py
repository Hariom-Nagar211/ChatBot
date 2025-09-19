from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os

# Load environment variables for local development
load_dotenv()

# Get API key from Streamlit secrets or environment variable
def get_api_key():
    try:
        # Try Streamlit secrets first (for deployment)
        import streamlit as st
        return st.secrets["GEMINI_API_KEY"]
    except:
        # Fallback to environment variable (for local development)
        return os.getenv("GEMINI_API_KEY")

api_key = get_api_key()
if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY not found. For local development, add it to .env file. "
        "For Streamlit deployment, add it to Streamlit secrets."
    )

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=api_key,
)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

# Checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)
