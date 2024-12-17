import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# Access the API key

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("OpenAI API Key loaded successfully!")
else:
    print("Failed to load OpenAI API Key.")