from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.core.ai_agent import get_response_from_ai_agents
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

app = FastAPI(
    title="Multi AI Agent API",
    version="1.0"
    )

class RequestState(BaseModel):
    model_name: str
    # query: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

@app.post("/chat")
async def chat_endpoint(request: RequestState):
    logger.info(f"Received Request for model: {request.model_name}")
    
    if request.model_name not in settings.ALLOWED_MODEL_NAMES:
        logger.warning(f"Model {request.model_name} not allowed")
        raise HTTPException(status_code=400, detail="Model not allowed")
    
    try:
        response = get_response_from_ai_agents(
            llm_id=request.model_name,
            query=request.messages,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
        )
        logger.info(f"Successfully received response from AI Agent model {request.model_name}: {response}")
        return {"response": response}

    except Exception as e:
        logger.error(f"Error occurred while processing request for model {request.model_name}: {e}")
        raise HTTPException(
            status_code=500,
            detail=str(CustomException(
                "Failed to get AI response.",
                error_details=e
            )))
