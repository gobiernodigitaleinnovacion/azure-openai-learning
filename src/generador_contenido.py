# src/generador_contenido.py
from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class GeneradorContenido:
    def __init__(self):
        self.cliente = obtener_cliente_azure()
    
    def generar_email(self, contexto, tipo="formal"):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Genera un email {tipo} con el siguiente contexto:"},
                {"role": "user", "content": contexto}
            ]
        )
        return respuesta.choices[0].message.content

    def crear_blog(self, tema, longitud="media"):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Crea un artículo de blog de longitud {longitud} sobre:"},
                {"role": "user", "content": tema}
            ]
        )
        return respuesta.choices[0].message.content

    def describir_producto(self, producto, caracteristicas):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Genera una descripción comercial del producto con sus características:"},
                {"role": "user", "content": f"Producto: {producto}\nCaracterísticas: {caracteristicas}"}
            ]
        )
        return respuesta.choices[0].message.content

    def generar_informe(self, datos, tipo_informe):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Genera un informe técnico tipo {tipo_informe} con los siguientes datos:"},
                {"role": "user", "content": datos}
            ]
        )
        return respuesta.choices[0].message.content