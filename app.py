import streamlit as st
import openai
from openai import OpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# load_dotenv()
# client = OpenAI(
#     api_key=os.getenv('OPENAI_API_KEY'),
# )
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# def get_response(user_question, chat_history):
#     template = """
#     Chat history:
#     {chat_history}

#     User question:
#     {user_question}
#     """
#     formatted_prompt = template.format(
#         chat_history="\n".join([msg.content for msg in chat_history]),
#         user_question=user_question
#     )
#     response = client.chat.completions.create(
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": formatted_prompt}
#         ],
#         model=st.session_state["openai_model"],
#     )
#     return response.choices[0].message.content

st.set_page_config(page_title="LLM ChatBot", page_icon='🤖')

# load custom scss
with open("llm/style.scss") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def clear_chat():
    st.session_state.chat_history = []

st.title("LLM ChatBot 🤖")
st.write("Welcome to the LLM ChatBot! Start by typing your message below!")

with st.sidebar:
    st.header("Settings")
    clear_button = st.button("Clear Chat History", on_click=clear_chat)

# conversation
# for message in st.session_state.chat_history:
#     if isinstance(message, HumanMessage):
#         with st.chat_message("Human"):
#             st.markdown(message.content)
#     else:
#         with st.chat_message("AI"):
#             st.markdown(message.content)

user_query = st.chat_input("Type your message...")
if user_query is not None and user_query != "":
    # st.session_state.chat_history.append(HumanMessage(user_query))

    with st.chat_message("Human"):
        st.markdown(f"<div class='chat-message'>{user_query}</div>", unsafe_allow_html=True)
    
    with st.chat_message("AI"):
        # response = get_response(user_query, st.session_state.chat_history)
        response = 'hehe'
        # st.session_state.chat_history.append(AIMessage(response))
        st.markdown(f"<div class='chat-message'>{response}</div>", unsafe_allow_html=True)
