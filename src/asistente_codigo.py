# src/asistente_codigo.py
from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class AsistenteCodigo:
    def __init__(self):
        self.cliente = obtener_cliente_azure()

    def generar_codigo(self, descripcion, lenguaje="python"):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Genera código en {lenguaje} que cumpla con las mejores prácticas y esté bien documentado."},
                {"role": "user", "content": descripcion}
            ]
        )
        return respuesta.choices[0].message.content

    def explicar_codigo(self, codigo, nivel="intermedio"):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": f"Explica este código a nivel {nivel}, detallando su funcionamiento."},
                {"role": "user", "content": f"Explica este código:\n{codigo}"}
            ]
        )
        return respuesta.choices[0].message.content

    def sugerir_mejoras(self, codigo):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Analiza el código y sugiere mejoras en rendimiento, legibilidad y mejores prácticas."},
                {"role": "user", "content": f"Sugiere mejoras para este código:\n{codigo}"}
            ]
        )
        return respuesta.choices[0].message.content