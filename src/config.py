from dotenv import load_dotenv
import os

load_dotenv()

AZURE_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")  # Cambiado de AZURE_API_KEY a AZURE_OPENAI_API_KEY
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_MODEL_NAME = os.getenv("AZURE_MODEL_NAME")