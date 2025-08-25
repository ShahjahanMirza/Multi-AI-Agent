import streamlit as st
import requests
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

st.set_page_config(
    page_title="Multi AI Agent Chat",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Multi AI Agent Chat using GROQ and Tavily")

selected_model = st.selectbox(
    "Select AI Model: ",
    options=settings.ALLOWED_MODEL_NAMES,
    index=0,
    help="Select the AI model to use for generating responses."
)

system_prompt = st.text_area("Define your AI Agent: ", height=70 )

allow_search = st.checkbox(
    "Allow Web Search",
    value=False,
    help="Enable web search capability for the AI agent."
)

user_query = st.text_area("Enter your query: ", height=150)

API_URL = "http://localhost:8000/chat"

if st.button("Ask Agent") and user_query.strip():
    
    payload = {
        "model_name": selected_model,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_search,
    }
    
    try:
        logger.info(f"Requesting response with payload: {payload}")
        
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            st.success("Response generated successfully!")
            agent_response = response.json()["response"]
            logger.info(f"Received response from AI Agent: {agent_response}")
            
            st.subheader("AI Agent Response:")
            st.markdown(agent_response.replace("\n", "<br>"), unsafe_allow_html=True)

        else:
            logger.error("Backend error")
            st.error("Backend error")
    
    except Exception as e:
        logger.error(f"Error: {e}")
        st.error(str(CustomException("Failed to get AI response.", e)))
        
        