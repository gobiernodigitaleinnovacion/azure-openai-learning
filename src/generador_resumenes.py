# src/generador_resumenes.py
from .utils.cliente_azure import obtener_cliente_azure
from .config import AZURE_MODEL_NAME

class GeneradorResumenes:
   def __init__(self):
       self.cliente = obtener_cliente_azure()
   
   def resumir(self, texto, max_palabras=30):
       respuesta = self.cliente.chat.completions.create(
           model=AZURE_MODEL_NAME, 
           messages=[
               {"role": "system", "content": f"Resume el siguiente texto en máximo {max_palabras} palabras:"},
               {"role": "user", "content": texto}
           ]
       )
       return respuesta.choices[0].message.content

   def generar_titulo(self, texto):
       respuesta = self.cliente.chat.completions.create(
           model=AZURE_MODEL_NAME,
           messages=[
               {"role": "system", "content": "Genera un título conciso (máximo 10 palabras) para el siguiente texto:"},
               {"role": "user", "content": texto}
           ]
       )
       titulo = respuesta.choices[0].message.content
       palabras = titulo.split()
       if len(palabras) > 10:
           titulo = ' '.join(palabras[:10])
       return titulo

   def resumir_por_rol(self, texto, rol):
       respuesta = self.cliente.chat.completions.create(
           model=AZURE_MODEL_NAME,
           messages=[
               {"role": "system", "content": f"Genera un resumen orientado a un {rol}:"},
               {"role": "user", "content": texto}
           ]
       )
       return respuesta.choices[0].message.content

   def resumir_con_keywords(self, texto, num_keywords=5):
       respuesta = self.cliente.chat.completions.create(
           model=AZURE_MODEL_NAME,
           messages=[
               {"role": "system", "content": f"Resume el texto y extrae las {num_keywords} palabras clave más importantes:"},
               {"role": "user", "content": texto}
           ]
       )
       return respuesta.choices[0].message.content