import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai_client = genai.Client(api_key=GEMINI_API_KEY)

EMBEDDING_MODEL_ID = "models/text-embedding-004"  #embedding-001
MODEL_ID = "gemini-2.0-flash"

CHROMA_PERSIST_DIRECTORY = "chroma_db"
CHROMA_COLLECTION_NAME = "docs"

