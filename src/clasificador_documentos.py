# src/clasificador_documentos.py

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

    # Nuevos métodos
    def clasificar_jerarquico(self, texto, subcategorias):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Clasifica el texto en una categoría principal ({', '.join(self.categorias)}) y una subcategoría ({', '.join(subcategorias)})"},
                {"role": "user", "content": texto}
            ]
        )
        return respuesta.choices[0].message.content

    def clasificar_multi_etiqueta(self, texto):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Clasifica el texto en una o más de estas categorías: {', '.join(self.categorias)}. Lista todas las categorías relevantes."},
                {"role": "user", "content": texto}
            ]
        )
        return respuesta.choices[0].message.content