# src/recomendador.py
from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class Recomendador:
    def __init__(self):
        self.cliente = obtener_cliente_azure()

    def generar_recomendaciones(self, perfil_usuario, historial_interacciones):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Analiza el perfil e historial del usuario y genera recomendaciones personalizadas."},
                {"role": "user", "content": f"Perfil:\n{perfil_usuario}\nHistorial:\n{historial_interacciones}"}
            ]
        )
        return respuesta.choices[0].message.content

    def explicar_recomendacion(self, recomendacion, perfil_usuario):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Explica por qué esta recomendación es relevante para el usuario."},
                {"role": "user", "content": f"Recomendación:\n{recomendacion}\nPerfil:\n{perfil_usuario}"}
            ]
        )
        return respuesta.choices[0].message.content

    def ajustar_recomendaciones(self, feedback_usuario, recomendaciones_previas):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Ajusta las recomendaciones basado en el feedback del usuario."},
                {"role": "user", "content": f"Feedback:\n{feedback_usuario}\nRecomendaciones previas:\n{recomendaciones_previas}"}
            ]
        )
        return respuesta.choices[0].message.content