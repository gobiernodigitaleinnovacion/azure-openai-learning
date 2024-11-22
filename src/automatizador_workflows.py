# src/automatizador_workflows.py
from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class AutomatizadorWorkflows:
    def __init__(self):
        self.cliente = obtener_cliente_azure()

    def disenar_workflow(self, descripcion_proceso):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Diseña un workflow detallado con pasos, roles y tiempos estimados. No uses markdown, símbolos especiales o formateo. Usa un formato limpio y legible."},
                {"role": "user", "content": f"Diseña un workflow en formato limpio y sin símbolos especiales para: {descripcion_proceso}"}
            ]
        )
        return respuesta.choices[0].message.content

    def optimizar_proceso(self, proceso_actual):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Analiza el proceso actual y sugiere optimizaciones para reducir tiempos y mejorar eficiencia."},
                {"role": "user", "content": f"Optimiza este proceso:\n{proceso_actual}"}
            ]
        )
        return respuesta.choices[0].message.content

    def identificar_cuellos_botella(self, metricas_proceso):
        respuesta = self.cliente.chat.completions.create(
            model=AZURE_MODEL_NAME,
            messages=[
                {"role": "system", "content": "Identifica cuellos de botella y problemas potenciales en el proceso."},
                {"role": "user", "content": f"Analiza estas métricas:\n{metricas_proceso}"}
            ]
        )
        return respuesta.choices[0].message.content