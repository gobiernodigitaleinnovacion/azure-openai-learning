# src/ocr_mejorado.py
from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class OCRMejorado:
    def __init__(self):
        self.cliente = obtener_cliente_azure()

    def extraer_texto(self, texto_imagen):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Extrae y estructura el texto de la imagen, corrigiendo errores comunes de OCR."},
                {"role": "user", "content": f"Extrae el texto de esta imagen:\n{texto_imagen}"}
            ]
        )
        return respuesta.choices[0].message.content

    def analizar_estructura(self, texto_imagen):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Analiza la estructura del documento e identifica secciones y elementos clave. Usa un formato limpio, sin markdown ni caracteres especiales."},
                {"role": "user", "content": f"Analiza la estructura de este documento de forma clara y simple:\n{texto_imagen}"}
            ]
        )
        return respuesta.choices[0].message.content

    def corregir_errores(self, texto):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Corrige errores comunes de OCR y mejora la calidad del texto."},
                {"role": "user", "content": f"Corrige este texto:\n{texto}"}
            ]
        )
        return respuesta.choices[0].message.content