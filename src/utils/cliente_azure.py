from openai import AzureOpenAI
from ..config import AZURE_API_KEY, AZURE_ENDPOINT, AZURE_MODEL_NAME

def obtener_cliente_azure():
    client = AzureOpenAI(
        api_key=AZURE_API_KEY,
        api_version="2024-08-01-preview",
        azure_endpoint=AZURE_ENDPOINT,
        azure_deployment=AZURE_MODEL_NAME
    )
    return client