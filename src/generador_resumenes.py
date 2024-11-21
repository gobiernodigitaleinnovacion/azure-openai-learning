from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME 

class GeneradorResumenes:
    def __init__(self):
        self.cliente = obtener_cliente_azure()
    
    def resumir(self, texto, max_palabras=100):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Resume el siguiente texto en {max_palabras} palabras o menos:"},
                {"role": "user", "content": texto}
            ]
        )
        return respuesta.choices[0].message.content