from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME 

class AnalizadorSentimientos:
   def __init__(self):
       self.cliente = obtener_cliente_azure()

   def analizar(self, texto):
       respuesta = self.cliente.chat.completions.create(
           model=AZURE_MODEL_NAME,
           messages=[
               {"role": "system", "content": "Eres un analizador de sentimientos. Responde con POSITIVO, NEGATIVO o NEUTRAL."},
               {"role": "user", "content": f"Analiza el sentimiento: {texto}"}
           ]
       )
       return respuesta.choices[0].message.content
   
   def analizar_aspecto(self, texto, aspecto):
       respuesta = self.cliente.chat.completions.create(
           model=AZURE_MODEL_NAME,
           messages=[
               {"role": "system", "content": f"Analiza el sentimiento sobre {aspecto} en el texto. Responde solo POSITIVO, NEGATIVO o NEUTRAL"},
               {"role": "user", "content": texto}
           ]
       )
       return respuesta.choices[0].message.content
   
   def detectar_urgencia(self, texto):
       respuesta = self.cliente.chat.completions.create(
           model=AZURE_MODEL_NAME,
           messages=[
               {"role": "system", "content": "Determina el nivel de urgencia. Responde solo ALTA, MEDIA o BAJA"},
               {"role": "user", "content": texto}
           ]
       )
       return respuesta.choices[0].message.content
   
   def analizar_multilingue(self, texto, idioma):
       respuesta = self.cliente.chat.completions.create(
           model=AZURE_MODEL_NAME,
           messages=[
               {"role": "system", "content": f"Analiza el sentimiento del texto en {idioma}. Responde en el idioma original."},
               {"role": "user", "content": texto}
           ]
       )
       return respuesta.choices[0].message.content