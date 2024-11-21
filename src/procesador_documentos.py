from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class ProcesadorDocumentos:
    def __init__(self):
        self.cliente = obtener_cliente_azure()

    def extraer_datos_estructurados(self, texto):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Extrae datos estructurados del texto proporcionado en formato JSON."},
                {"role": "user", "content": f"Extrae datos estructurados de este texto:\n{texto}"}
            ]
        )
        return respuesta.choices[0].message.content

    def analizar_contrato(self, texto_contrato):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Analiza el contrato y extrae los puntos clave, cláusulas importantes y obligaciones."},
                {"role": "user", "content": f"Analiza este contrato:\n{texto_contrato}"}
            ]
        )
        return respuesta.choices[0].message.content

    def procesar_factura(self, texto_factura):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Analiza la factura y extrae información relevante como montos, conceptos, datos fiscales y fechas."},
                {"role": "user", "content": f"Procesa esta factura:\n{texto_factura}"}
            ]
        )
        return respuesta.choices[0].message.content

    def generar_resumen_ejecutivo(self, texto):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Genera un resumen ejecutivo conciso y profesional del documento."},
                {"role": "user", "content": f"Genera un resumen ejecutivo de:\n{texto}"}
            ]
        )
        return respuesta.choices[0].message.content

    def identificar_puntos_clave(self, texto):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Identifica y enumera los puntos clave más importantes del documento."},
                {"role": "user", "content": f"Identifica los puntos clave de:\n{texto}"}
            ]
        )
        return respuesta.choices[0].message.content