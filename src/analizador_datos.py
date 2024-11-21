from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class AnalizadorDatos:
    def __init__(self):
        self.cliente = obtener_cliente_azure()

    def interpretar_metricas(self, datos):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Eres un analista de datos experto. Interpreta las métricas proporcionadas de manera profesional y concisa."},
                {"role": "user", "content": f"Interpreta estas métricas:\n{datos}"}
            ]
        )
        return respuesta.choices[0].message.content

    def analizar_tendencias(self, datos):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Analiza las tendencias en los datos y proporciona insights claros sobre patrones y comportamientos."},
                {"role": "user", "content": f"Analiza las tendencias en estos datos:\n{datos}"}
            ]
        )
        return respuesta.choices[0].message.content

    def generar_recomendaciones(self, datos):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Basado en los datos, genera recomendaciones estratégicas y accionables."},
                {"role": "user", "content": f"Genera recomendaciones basadas en estos datos:\n{datos}"}
            ]
        )
        return respuesta.choices[0].message.content