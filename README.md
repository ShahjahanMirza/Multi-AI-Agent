# Multi AI Agent Chat Application

A sophisticated AI-powered chat application that leverages multiple language models through GROQ API and provides web search capabilities via Tavily. Built with FastAPI backend, Streamlit frontend, and LangGraph for agent orchestration.

## 🚀 Features

- **Multiple AI Models**: Support for various language models including Llama 3.3 70B and DeepSeek R1
- **Web Search Integration**: Optional web search capability powered by Tavily API
- **Custom System Prompts**: Define custom AI agent personalities and behaviors
- **Real-time Chat Interface**: Interactive Streamlit-based web interface
- **RESTful API**: FastAPI backend for scalable AI agent interactions
- **Comprehensive Logging**: Detailed logging system for monitoring and debugging
- **Error Handling**: Robust custom exception handling throughout the application

## 🏗️ Architecture

The application follows a modular architecture with clear separation of concerns:

```
app/
├── backend/          # FastAPI REST API server
├── frontend/         # Streamlit web interface
├── core/            # AI agent logic and LangGraph integration
├── config/          # Configuration and settings management
├── common/          # Shared utilities (logging, exceptions)
└── main.py          # Application entry point
```

### Core Components

#### 1. **Backend API** (`app/backend/api.py`)
- FastAPI-based REST API server
- Handles chat requests and model validation
- Processes AI agent responses
- Runs on `http://localhost:8000`

#### 2. **Frontend Interface** (`app/frontend/ui.py`)
- Streamlit-based web interface
- Model selection dropdown
- System prompt configuration
- Web search toggle
- Real-time chat interaction
- Runs on `http://localhost:8501`

#### 3. **AI Agent Core** (`app/core/ai_agent.py`)
- LangGraph-powered ReAct agent implementation
- GROQ API integration for language models
- Tavily search tool integration
- Dynamic tool selection based on user preferences

#### 4. **Configuration Management** (`app/config/settings.py`)
- Environment variable management
- API key configuration
- Supported model definitions
- Centralized settings access

#### 5. **Common Utilities**
- **Logger** (`app/common/logger.py`): Comprehensive logging with file and console output
- **Custom Exceptions** (`app/common/custom_exception.py`): Structured error handling

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- GROQ API Key
- Tavily API Key (for web search functionality)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd "Multi AI Agent"
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
GROQ_API_KEY="your_groq_api_key_here"
TAVILY_API_KEY="your_tavily_api_key_here"
```

**Getting API Keys:**
- **GROQ API**: Sign up at [console.groq.com](https://console.groq.com)
- **Tavily API**: Register at [tavily.com](https://tavily.com)

### 5. Install Package (Optional)

```bash
pip install -e .
```

## 🚀 Usage

### Starting the Application

```bash
python app/main.py
```

This command will:
1. Start the FastAPI backend server on `http://localhost:8000`
2. Launch the Streamlit frontend on `http://localhost:8501`

### Using the Web Interface

1. **Select AI Model**: Choose from available models (Llama 3.3 70B, DeepSeek R1)
2. **Define AI Agent**: Enter custom system prompts to define agent behavior
3. **Enable Web Search**: Toggle web search capability for real-time information
4. **Enter Query**: Type your question or request
5. **Get Response**: Click "Ask Agent" to receive AI-generated responses

### API Usage

The backend provides a REST API endpoint for programmatic access:

**Endpoint**: `POST http://localhost:8000/chat`

**Request Body**:
```json
{
  "model_name": "llama-3.3-70b-versatile",
  "system_prompt": "You are a helpful assistant",
  "messages": ["What is artificial intelligence?"],
  "allow_search": true
}
```

**Response**:
```json
{
  "response": "AI-generated response content..."
}
```

## 🔧 Configuration

### Supported Models

Currently supported AI models:
- `llama-3.3-70b-versatile`
- `deepseek-r1-distill-llama-70b`

To add new models, update the `ALLOWED_MODEL_NAMES` list in `app/config/settings.py`.

### Logging

Logs are automatically generated in the `logs/` directory with timestamps:
- Format: `MM_DD_YYYY_HH_MM_SS.log`
- Includes both file and console output
- Configurable log levels and formats

## 🧠 How It Works

### AI Agent Flow

1. **Request Processing**: Frontend sends user query to backend API
2. **Model Initialization**: GROQ ChatModel is initialized with selected model
3. **Tool Configuration**: Tavily search tool is conditionally added based on user preference
4. **Agent Creation**: LangGraph creates a ReAct agent with model, tools, and system prompt
5. **Query Execution**: Agent processes the query using ReAct (Reasoning + Acting) pattern
6. **Response Generation**: Latest AI message is extracted and returned to frontend

### ReAct Agent Pattern

The application uses the ReAct (Reasoning and Acting) pattern:
- **Reasoning**: Agent thinks about the problem step by step
- **Acting**: Agent can use tools (web search) to gather information
- **Iteration**: Process repeats until a final answer is reached

## 📁 Project Structure

```
Multi AI Agent/
├── .env                          # Environment variables
├── .vscode/                      # VS Code settings
├── app/
│   ├── __init__.py
│   ├── main.py                   # Application entry point
│   ├── backend/
│   │   ├── __init__.py
│   │   └── api.py                # FastAPI REST API
│   ├── frontend/
│   │   ├── __init__.py
│   │   └── ui.py                 # Streamlit web interface
│   ├── core/
│   │   ├── __init__.py
│   │   └── ai_agent.py           # AI agent logic
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py           # Configuration management
│   └── common/
│       ├── __init__.py
│       ├── logger.py             # Logging utilities
│       └── custom_exception.py   # Custom exception handling
├── logs/                         # Application logs
├── venv/                         # Virtual environment
├── requirements.txt              # Python dependencies
├── setup.py                      # Package setup
└── README.md                     # This file
```

## 🔍 Dependencies

### Core Dependencies
- **langchain-groq**: GROQ API integration
- **langchain-community**: Community tools and utilities
- **langgraph**: Agent orchestration and workflow management
- **fastapi**: Modern web framework for building APIs
- **streamlit**: Web app framework for data science
- **uvicorn**: ASGI server for FastAPI
- **pydantic**: Data validation and settings management
- **python-dotenv**: Environment variable management

## 🚨 Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure `.env` file contains valid GROQ and Tavily API keys
2. **Port Conflicts**: Check if ports 8000 or 8501 are already in use
3. **Module Import Errors**: Verify virtual environment is activated and dependencies are installed
4. **Model Not Found**: Ensure selected model is in the `ALLOWED_MODEL_NAMES` list

### Logs

Check the `logs/` directory for detailed error information and application behavior.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is part of the "LLMOps And AIOps Bootcamp" course materials.

## 👨‍💻 Author

**Shahjahan** - Course Instructor

---

**Note**: This application is designed for educational purposes as part of the LLMOps and AIOps bootcamp curriculum. It demonstrates practical implementation of AI agents, API development, and modern web technologies.