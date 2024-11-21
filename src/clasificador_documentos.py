from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME 
class ClasificadorDocumentos:
    def __init__(self, categorias):
        self.cliente = obtener_cliente_azure()
        self.categorias = categorias
    
    def clasificar(self, texto):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Clasifica el texto en una de estas categorías: {', '.join(self.categorias)}"},
                {"role": "user", "content": texto}
            ]
        )
        return respuesta.choices[0].message.content