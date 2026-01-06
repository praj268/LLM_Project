# Python
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI # Correct import for OpenAI LLM
import os

# Load environment variables from .env file
load_dotenv()

# Title for the app
st.title("Simple Question-Answering App")

# Get API key from .env file
api_key = os.getenv("OPENAI_API_KEY")

# Sidebar for API key input (optional override)
st.sidebar.header("Configuration")
user_api_key = st.sidebar.text_input("Enter your OpenAI API Key (optional)", type="password")

# Use the user-provided API key if available, otherwise use the .env key
api_key = user_api_key if user_api_key else api_key

# Input field for the question
question = st.text_input("Ask a question:")

# Button to submit the question
if st.button("Get Answer"):
    if not api_key:
        st.error("Please provide an OpenAI API Key in the sidebar or .env file.")
    elif not question:
        st.error("Please enter a question.")
    else:
        try:
            # Initialize the LLM with the API key
            llm = ChatOpenAI(openai_api_key=api_key)  # Correct initialization

            # Generate an answer using LangChain
            answer = llm.predict(question)  # Use the `predict` method for ChatOpenAI

            # Display the answer
            st.success(f"Answer: {answer}")
        except Exception as e:
            st.error(f"An error occurred: {e}")