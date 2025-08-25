import subprocess
import threading
import time
from dotenv import load_dotenv

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

load_dotenv()

def run_backend():
    try:
        logger.info("Running backend server...")
        subprocess.run(["uvicorn", "app.backend.api:app", "--host", "localhost", "--port", "8000"], check=True)
    except CustomException as e:
        logger.error(f"Backend server failed to start: {e}")
        raise CustomException(f"Backend server failed to start: {e}")

def run_frontend():
    try:
        logger.info("Running frontend server...")
        subprocess.run(["streamlit", "run", "app/frontend/ui.py"], check=True)
    except CustomException as e:
        logger.error(f"Frontend server failed to start: {e}")
        raise CustomException(f"Frontend server failed to start: {e}")
    

if __name__ == "__main__":
    try:
        backend_thread = threading.Thread(target=run_backend)
        backend_thread.start()
        
        time.sleep(5)
        run_frontend()
        
    except CustomException as e:
        logger.error(f"Application failed: {e}")