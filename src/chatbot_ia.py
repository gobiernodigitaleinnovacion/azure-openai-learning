# src/chatbot_ia.py
from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class ChatbotIA:
    def __init__(self):
        self.cliente = obtener_cliente_azure()
        self.historial = []

    def responder(self, mensaje, contexto="soporte"):
        # Añadir mensaje al historial
        self.historial.append({"role": "user", "content": mensaje})
        
        # Crear el sistema de mensajes
        mensajes = [
            {"role": "system", "content": f"Eres un chatbot de {contexto} amigable y profesional."},
            *self.historial
        ]
        
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=mensajes
        )
        
        # Añadir respuesta al historial
        self.historial.append({"role": "assistant", "content": respuesta.choices[0].message.content})
        return respuesta.choices[0].message.content

    def limpiar_historial(self):
        self.historial = []