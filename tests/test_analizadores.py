import pytest
from src.procesador_documentos import ProcesadorDocumentos
from src.analizador_sentimientos import AnalizadorSentimientos
from src.generador_resumenes import GeneradorResumenes
from src.clasificador_documentos import ClasificadorDocumentos
from src.generador_contenido import GeneradorContenido

# Datos de ejemplo para tests
texto_documento = """
Informe de Ventas - Región Norte
Fecha: 15 de Noviembre 2023
Cliente: Empresa ABC
Producto: Software de Gestión
Cantidad: 5 licencias
Precio unitario: $1,200
Total: $6,000
Términos de pago: 30 días
"""

texto_contrato = """
CONTRATO DE SERVICIOS
Entre las partes:
- Proveedor: Servicios Tech SA
- Cliente: Empresa ABC
- Duración: 12 meses
- Valor mensual: $5,000
- Servicios incluidos: Mantenimiento, Soporte 24/7
"""

texto_factura = """
FACTURA
No: FAC-2023-001
Fecha: 20 de Noviembre 2023
EMISOR:
Servicios Tech SA
RFC: TECH231120ABC
RECEPTOR:
Empresa ABC
RFC: ABC850101XYZ
CONCEPTOS:
1. Licencia Software Gestión x 5
  Precio unitario: $1,200
  Subtotal: $6,000
2. Servicio Implementación
  Precio: $2,000
Subtotal: $8,000
IVA (16%): $1,280
Total: $9,280
"""

class TestProcesadorDocumentos:
   def test_extraer_datos_estructurados(self):
       procesador = ProcesadorDocumentos()
       resultado = procesador.extraer_datos_estructurados(texto_documento)
       print(f"Datos estructurados: {resultado}")
       assert isinstance(resultado, str)
       assert len(resultado) > 0

   def test_analizar_contrato(self):
       procesador = ProcesadorDocumentos()
       resultado = procesador.analizar_contrato(texto_contrato)
       print(f"Análisis de contrato: {resultado}")
       assert isinstance(resultado, str)
       assert len(resultado) > 0

   def test_procesar_factura(self):
       procesador = ProcesadorDocumentos()
       resultado = procesador.procesar_factura(texto_factura)
       print(f"Procesamiento de factura: {resultado}")
       assert isinstance(resultado, str)
       assert len(resultado) > 0

   def test_generar_resumen_ejecutivo(self):
       procesador = ProcesadorDocumentos()
       resultado = procesador.generar_resumen_ejecutivo(texto_contrato)
       print(f"Resumen ejecutivo: {resultado}")
       assert isinstance(resultado, str)
       assert len(resultado) > 0

   def test_identificar_puntos_clave(self):
       procesador = ProcesadorDocumentos()
       resultado = procesador.identificar_puntos_clave(texto_factura)
       print(f"Puntos clave: {resultado}")
       assert isinstance(resultado, str)
       assert len(resultado) > 0

   def test_validacion_formato_json(self):
       procesador = ProcesadorDocumentos()
       resultado = procesador.extraer_datos_estructurados(texto_documento)
       resultado = resultado.replace('```json', '').replace('```', '').strip()
       resultado_lower = resultado.lower()
       
       assert '{' in resultado
       assert '}' in resultado
       
       campos_requeridos = [
           ['region', 'región'],
           ['fecha'],
           ['cliente'],
           ['total']
       ]
       
       for campos in campos_requeridos:
           found = any(campo in resultado_lower for campo in campos)
           assert found, f"Ninguna variante de '{campos[0]}' encontrada en el JSON"

   def test_analisis_contrato_contenido(self):
       procesador = ProcesadorDocumentos()
       resultado = procesador.analizar_contrato(texto_contrato)
       assert "Servicios Tech SA" in resultado
       assert "Empresa ABC" in resultado
       assert "12 meses" in resultado
       assert "$5,000" in resultado

   def test_procesamiento_factura_contenido(self):
       procesador = ProcesadorDocumentos()
       resultado = procesador.procesar_factura(texto_factura)
       assert "FAC-2023-001" in resultado
       assert "Servicios Tech SA" in resultado
       assert "$9,280" in resultado
       assert "IVA" in resultado

class TestAnalizadorSentimientos:
   def test_analizador_sentimientos(self):
       analizador = AnalizadorSentimientos()
       texto = "Me encanta este proyecto"
       resultado = analizador.analizar(texto)
       print(f"Resultado del análisis: {resultado}")
       assert resultado in ["POSITIVO", "NEGATIVO", "NEUTRAL"]

   def test_analisis_por_aspectos(self):
       analizador = AnalizadorSentimientos()
       texto = "El producto tiene excelente calidad pero el precio es muy alto"
       resultado_calidad = analizador.analizar_aspecto(texto, "calidad")
       resultado_precio = analizador.analizar_aspecto(texto, "precio")
       assert resultado_calidad in ["POSITIVO", "NEGATIVO", "NEUTRAL"]
       assert resultado_precio in ["POSITIVO", "NEGATIVO", "NEUTRAL"]

   def test_deteccion_urgencia(self):
       analizador = AnalizadorSentimientos()
       texto_urgente = "Necesito ayuda urgente, el sistema está caído"
       texto_normal = "Me gustaría saber más sobre el producto"
       resultado_urgente = analizador.detectar_urgencia(texto_urgente)
       resultado_normal = analizador.detectar_urgencia(texto_normal)
       assert resultado_urgente in ["ALTA", "MEDIA", "BAJA"]
       assert resultado_normal in ["ALTA", "MEDIA", "BAJA"]

   def test_analisis_multilingue(self):
       analizador = AnalizadorSentimientos()
       textos = {
           "es": "Me encanta este producto",
           "en": "I love this product",
           "fr": "J'adore ce produit"
       }
       for idioma, texto in textos.items():
           resultado = analizador.analizar_multilingue(texto, idioma)
           assert isinstance(resultado, str)
           assert len(resultado) > 0

class TestClasificador:
   def test_clasificador(self):
       categorias = ["Tecnología", "Deportes", "Cultura"]
       clasificador = ClasificadorDocumentos(categorias)
       texto = "Python es un lenguaje de programación versátil y popular"
       resultado = clasificador.clasificar(texto)
       assert resultado in categorias

   def test_clasificacion_jerarquica(self):
       categorias = ["Tecnología", "Deportes", "Cultura"]
       subcategorias = ["Software", "Hardware", "IA"]
       clasificador = ClasificadorDocumentos(categorias)
       texto = "Python es un lenguaje de programación usado en IA"
       resultado = clasificador.clasificar_jerarquico(texto, subcategorias)
       assert isinstance(resultado, str)

   def test_clasificacion_multi_etiqueta(self):
       categorias = ["Tecnología", "Ciencia", "Educación"]
       clasificador = ClasificadorDocumentos(categorias)
       texto = "Nuevo software educativo utiliza IA para enseñar ciencias"
       resultado = clasificador.clasificar_multi_etiqueta(texto)
       assert isinstance(resultado, str)

class TestGeneradorResumenes:
   def test_generador_resumenes(self):
       generador = GeneradorResumenes()
       texto_largo = """
       La inteligencia artificial (IA) es una rama de la informática que busca crear 
       sistemas capaces de aprender y resolver problemas de manera similar a los humanos.
       """
       resultado = generador.resumir(texto_largo, max_palabras=20)
       assert len(resultado.split()) <= 20

   def test_resumen_por_rol(self):
       generador = GeneradorResumenes()
       texto = "La IA está revolucionando la industria tecnológica."
       roles = ["ejecutivo", "técnico", "marketing"]
       for rol in roles:
           resumen = generador.resumir_por_rol(texto, rol)
           assert isinstance(resumen, str)

   def test_resumen_con_keywords(self):
       generador = GeneradorResumenes()
       texto = "Python es un lenguaje de programación versátil."
       resultado = generador.resumir_con_keywords(texto, num_keywords=5)
       assert isinstance(resultado, str)

   def test_generar_titulo(self):
       generador = GeneradorResumenes()
       texto = "La tecnología 5G revoluciona las comunicaciones."
       titulo = generador.generar_titulo(texto)
       assert isinstance(titulo, str)
       assert len(titulo.split()) <= 10

class TestGeneradorContenido:
   def test_generar_email(self):
       generador = GeneradorContenido()
       contexto = "Solicitud de reunión para proyecto IA"
       resultado = generador.generar_email(contexto, tipo="formal")
       assert isinstance(resultado, str)

   def test_crear_blog(self):
       generador = GeneradorContenido()
       tema = "IA en Medicina"
       resultado = generador.crear_blog(tema, longitud="media")
       assert isinstance(resultado, str)

   def test_describir_producto(self):
       generador = GeneradorContenido()
       producto = "Smartwatch XYZ"
       caracteristicas = "Pantalla AMOLED, Batería 7 días"
       resultado = generador.describir_producto(producto, caracteristicas)
       assert isinstance(resultado, str)

   def test_generar_informe(self):
       generador = GeneradorContenido()
       datos = "Tiempo: 3 meses, Presupuesto: 80%"
       resultado = generador.generar_informe(datos, tipo_informe="ejecutivo")
       assert isinstance(resultado, str)
