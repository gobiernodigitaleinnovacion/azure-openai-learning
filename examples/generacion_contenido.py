# examples/generacion_contenido.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(''))))

from src.generador_contenido import GeneradorContenido

generador = GeneradorContenido()

# Ejemplo de Email
contexto_email = "Solicitud de reunión para discutir el nuevo proyecto de IA"
email = generador.generar_email(contexto_email, tipo="formal")
print("=== EMAIL GENERADO ===")
print(email)
print()

# Ejemplo de Blog
tema_blog = "Impacto de la Inteligencia Artificial en la Medicina Moderna"
blog = generador.crear_blog(tema_blog, longitud="media")
print("=== ARTÍCULO DE BLOG ===")
print(blog)
print()

# Ejemplo de Descripción de Producto
producto = "Smartwatch XYZ"
caracteristicas = """
- Pantalla AMOLED de 1.4"
- Batería de 7 días
- Resistente al agua
- Monitores de salud
- GPS integrado
"""
descripcion = generador.describir_producto(producto, caracteristicas)
print("=== DESCRIPCIÓN DE PRODUCTO ===")
print(descripcion)
print()

# Ejemplo de Informe Técnico
datos_informe = """
Métricas del Proyecto Q4 2024:
- Tiempo de desarrollo: 3 meses
- Recursos utilizados: 5 desarrolladores
- Presupuesto ejecutado: 80%
- Objetivos completados: 90%
"""
informe = generador.generar_informe(datos_informe, tipo_informe="ejecutivo")
print("=== INFORME TÉCNICO ===")
print(informe)