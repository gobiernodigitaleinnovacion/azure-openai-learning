# src/analisis_predictivo.py
from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class AnalizadorPredictivo:
    def __init__(self):
        self.cliente = obtener_cliente_azure()

    def predecir_tendencia(self, datos_historicos, contexto):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Analiza los datos históricos y predice tendencias futuras basadas en patrones observados."},
                {"role": "user", "content": f"Datos históricos:\n{datos_historicos}\nContexto: {contexto}"}
            ]
        )
        return respuesta.choices[0].message.content

    def analizar_patrones(self, datos, periodo="mensual"):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Identifica patrones y ciclos en los datos con frecuencia {periodo}."},
                {"role": "user", "content": f"Analiza estos datos:\n{datos}"}
            ]
        )
        return respuesta.choices[0].message.content

    def generar_recomendaciones(self, analisis):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Genera recomendaciones estratégicas basadas en el análisis predictivo."},
                {"role": "user", "content": f"Basado en este análisis:\n{analisis}"}
            ]
        )
        return respuesta.choices[0].message.content