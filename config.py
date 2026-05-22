import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "research_assistant"
USER_ID = "user1"
SESSION_ID = "session1"

MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")