import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key not found! Ensure it is set in the .env file.")
