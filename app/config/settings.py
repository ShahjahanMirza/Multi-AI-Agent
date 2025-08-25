from dotenv import load_dotenv
import os

load_dotenv()

"""
Configuration settings module for the Multi AI Agent application.

This module handles loading and managing environment variables and configuration settings
for the application. It uses python-dotenv to load environment variables from a .env file.

Key Features:
- Loads API keys for GROQ and Tavily services
- Defines allowed AI model names that can be used
- Provides a Settings class to encapsulate all configuration parameters

Required Environment Variables:
- GROQ_API_KEY: API key for GROQ service
- TAVILY_API_KEY: API key for Tavily service

Usage:
    groq_key = settings.GROQ_API_KEY
"""


class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    ALLOWED_MODEL_NAMES = [
        "llama-3.3-70b-versatile",
        "deepseek-r1-distill-llama-70b"
        ]

settings = Settings()

