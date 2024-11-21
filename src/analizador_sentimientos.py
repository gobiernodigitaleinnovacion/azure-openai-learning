from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME 

class AnalizadorSentimientos:
    def __init__(self):
        self.cliente = obtener_cliente_azure()
    
    def analizar(self, texto):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Eres un analizador de sentimientos. Responde con POSITIVO, NEGATIVO o NEUTRAL."},
                {"role": "user", "content": f"Analiza el sentimiento: {texto}"}
            ]
        )
        return respuesta.choices[0].message.content