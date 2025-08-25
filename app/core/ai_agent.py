from re import L
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages.ai import AIMessage

from langgraph.prebuilt import create_react_agent

from app.config.settings import settings

def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):
    """
    Get responses from AI agents using the specified LLM and optional search capability.

    Args:
        llm_id (str): The identifier for the language model to use
        query (str): The input query/prompt to send to the AI agent
        allow_search (bool): Whether to enable web search capability
        system_prompt (str): System prompts/instructions for the AI agent

    Returns:
        dict: Response from the AI agent containing the generated content
    """
    llm = ChatGroq(
        model_name=llm_id,
        groq_api_key=settings.GROQ_API_KEY
    )
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
        )

    state = {"messages": query}

    response = agent.invoke(state)

    messages = response.get("messages")
    
    ai_messages = [message for message in messages if isinstance(message, AIMessage)]
    
    latest_ai_message = ai_messages[-1]
    
    
    return latest_ai_message.content

