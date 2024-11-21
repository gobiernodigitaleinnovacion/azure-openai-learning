import pytest
from src.analizador_sentimientos import AnalizadorSentimientos
from src.generador_resumenes import GeneradorResumenes
from src.clasificador_documentos import ClasificadorDocumentos

def test_analizador_sentimientos():
    analizador = AnalizadorSentimientos()
    texto = "Me encanta este proyecto"
    resultado = analizador.analizar(texto)
    print(f"Resultado del análisis: {resultado}")
    assert resultado in ["POSITIVO", "NEGATIVO", "NEUTRAL"]

def test_generador_resumenes():
    generador = GeneradorResumenes()
    texto_largo = """
    La inteligencia artificial (IA) es una rama de la informática que busca crear 
    sistemas capaces de aprender y resolver problemas de manera similar a los humanos. 
    Utiliza técnicas como el aprendizaje automático y las redes neuronales para procesar 
    datos y tomar decisiones. Ha revolucionado campos como la medicina, la automoción 
    y el análisis de datos.
    """
    resultado = generador.resumir(texto_largo, max_palabras=20)
    print(f"Resumen generado: {resultado}")
    assert len(resultado.split()) <= 20

def test_clasificador():
    categorias = ["Tecnología", "Deportes", "Cultura"]
    clasificador = ClasificadorDocumentos(categorias)
    texto = "Python es un lenguaje de programación versátil y popular"
    resultado = clasificador.clasificar(texto)
    print(f"Clasificación: {resultado}")
    assert resultado in categorias