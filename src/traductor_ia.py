from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class TraductorIA:
    def __init__(self):
        self.cliente = obtener_cliente_azure()

    def traducir(self, texto, idioma_origen, idioma_destino):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Traduce del {idioma_origen} al {idioma_destino} manteniendo el contexto y estilo."},
                {"role": "user", "content": texto}
            ]
        )
        return respuesta.choices[0].message.content

    def localizar(self, texto, region, tipo_contenido="marketing"):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Adapta este contenido de {tipo_contenido} para la región {region}, considerando cultura y costumbres locales."},
                {"role": "user", "content": texto}
            ]
        )
        return respuesta.choices[0].message.content