# Proyecto de Aprendizaje Azure OpenAI

Implementación avanzada de Azure OpenAI para procesamiento de lenguaje natural y automatización empresarial.

## Requisitos

- Python 3.8+
- Cuenta de Azure con acceso a Azure OpenAI
- API Key de Azure OpenAI

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/gobiernodigitaleinnovacion/azure-openai-learning.git
cd azure-openai-learning
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar credenciales:
```bash
cp .env.example .env
# Editar .env con tus credenciales
```

## Funcionalidades

### 1. Análisis de Sentimientos
```python
from src.analizador_sentimientos import AnalizadorSentimientos

analizador = AnalizadorSentimientos()
# Análisis básico y por aspectos
resultado = analizador.analizar("Me encanta este proyecto")
aspectos = analizador.analizar_aspecto("El producto es bueno pero caro", "precio")
# Detección de urgencia
urgencia = analizador.detectar_urgencia("Necesito ayuda urgente")
# Análisis multilingüe
sentimiento = analizador.analizar_multilingue("C'est excellent!", "fr")
```

### 2. Generación de Resúmenes
```python
from src.generador_resumenes import GeneradorResumenes

generador = GeneradorResumenes()
# Resumen básico
resumen = generador.resumir(texto, max_palabras=100)
# Resumen por rol
resumen_ejecutivo = generador.resumir_por_rol(texto, "ejecutivo")
# Resumen con keywords
keywords = generador.resumir_con_keywords(texto, num_keywords=5)
# Generación de título
titulo = generador.generar_titulo(texto)
```

### 3. Clasificación de Documentos
```python
from src.clasificador_documentos import ClasificadorDocumentos

clasificador = ClasificadorDocumentos(["Tecnología", "Negocios", "Salud"])
# Clasificación simple
categoria = clasificador.clasificar(texto)
# Clasificación jerárquica
jerarquia = clasificador.clasificar_jerarquico(texto, ["Software", "Hardware"])
# Multi-etiqueta
etiquetas = clasificador.clasificar_multi_etiqueta(texto)
```

### 4. Procesamiento de Documentos
```python
from src.procesador_documentos import ProcesadorDocumentos

procesador = ProcesadorDocumentos()
# Extracción de datos
datos = procesador.extraer_datos_estructurados(documento)
# Análisis de contratos
analisis = procesador.analizar_contrato(contrato)
# Facturas
factura = procesador.procesar_factura(factura)
# Resumen ejecutivo
resumen = procesador.generar_resumen_ejecutivo(documento)
# Puntos clave
puntos = procesador.identificar_puntos_clave(documento)
```

### 5. Generación de Contenido
```python
from src.generador_contenido import GeneradorContenido

generador = GeneradorContenido()
# Emails
email = generador.generar_email("Reunión proyecto", "formal")
# Blogs
blog = generador.crear_blog("IA en Medicina")
# Productos
descripcion = generador.describir_producto("Smartwatch XYZ", caracteristicas)
# Informes
informe = generador.generar_informe(datos, "ejecutivo")
```

### 6. Automatización de Workflows
```python
from src.automatizador_workflows import AutomatizadorWorkflows

automatizador = AutomatizadorWorkflows()
# Diseño de workflows
workflow = automatizador.disenar_workflow("Proceso onboarding")
# Optimización
mejoras = automatizador.optimizar_proceso(proceso_actual)
# Cuellos de botella
analisis = automatizador.identificar_cuellos_botella(metricas)
```

### 7. OCR Mejorado
```python
from src.ocr_mejorado import OCRMejorado

ocr = OCRMejorado()
# Extracción
texto = ocr.extraer_texto(imagen)
# Estructura
estructura = ocr.analizar_estructura(documento)
# Corrección
corregido = ocr.corregir_errores(texto)
```

### 8. Traductor IA
```python
from src.traductor_ia import TraductorIA

traductor = TraductorIA()
# Traducción
traduccion = traductor.traducir("Hello world", "inglés", "español")
# Localización
localizado = traductor.localizar("Our product", "México")
```

### 9. Chatbot IA
```python
from src.chatbot_ia import ChatbotIA

chatbot = ChatbotIA()
# Respuestas
respuesta = chatbot.responder("¿Cómo restablezco mi contraseña?", "soporte")
# Conversación
chatbot.responder("¿Qué servicios ofrecen?")
# Gestión
chatbot.limpiar_historial()
```

### 10. Asistente de Código
```python
from src.asistente_codigo import AsistenteCodigo

asistente = AsistenteCodigo()
# Generación
codigo = asistente.generar_codigo("Calcular factorial", "python")
# Explicación
explicacion = asistente.explicar_codigo(codigo)
# Mejoras
sugerencias = asistente.sugerir_mejoras(codigo)
```

### 11. Análisis Predictivo
```python
from src.analisis_predictivo import AnalizadorPredictivo

analizador = AnalizadorPredictivo()
# Predicción
prediccion = analizador.predecir_tendencia(datos_ventas)
# Patrones
patrones = analizador.analizar_patrones(datos)
# Recomendaciones
recomendaciones = analizador.generar_recomendaciones(analisis)
```

### 12. Recomendador
```python
from src.recomendador import Recomendador

recomendador = Recomendador()
# Recomendaciones
recomendaciones = recomendador.generar_recomendaciones(perfil, historial)
# Explicación
explicacion = recomendador.explicar_recomendacion(recomendacion, perfil)
# Ajustes
ajustes = recomendador.ajustar_recomendaciones(feedback, previas)
```
### 13. Analizador de Datos
```python
from src.analizador_datos import AnalizadorDatos

analizador = AnalizadorDatos()
# Interpretación de métricas
interpretacion = analizador.interpretar_metricas(datos_metricas)
# Análisis de tendencias
tendencias = analizador.analizar_tendencias(datos)
# Recomendaciones
recomendaciones = analizador.generar_recomendaciones(datos)
## Estructura del Proyecto
```
azure-openai-learning/
├── src/
│   ├── analizador_sentimientos.py
    ├── analizador_datos.py  
│   ├── generador_resumenes.py
│   ├── clasificador_documentos.py
│   ├── procesador_documentos.py
│   ├── generador_contenido.py
│   ├── automatizador_workflows.py
│   ├── ocr_mejorado.py
│   ├── traductor_ia.py
│   ├── chatbot_ia.py
│   ├── asistente_codigo.py
│   ├── analisis_predictivo.py
│   ├── recomendador.py
│   └── utils/
│       └── cliente_azure.py
├── tests/                  # Pruebas unitarias
│   └── test_analizadores.py
├── examples/              # Ejemplos y demostraciones
│   ├── notebooks/        # Jupyter notebooks
│   │   ├── analisis_sentimientos.ipynb
│   │   ├── clasificacion_avanzada.ipynb
│   │   ├── procesamiento_documentos.ipynb
│   │   └── resumenes_avanzados.ipynb
│   ├── outputs/          # Archivos generados
│   │   ├── blog_generado.txt
│   │   ├── email_generado.txt
│   │   └── informe_tecnico.txt
│   └── scripts/          # Scripts de ejemplo
│       └── generacion_contenido.py
└── .env                   # Configuración local
```

## Pruebas
```bash
# Ejecutar todas las pruebas
pytest tests/

# Ejecutar pruebas específicas
pytest tests/test_analizadores.py::TestAnalizadorSentimientos
pytest tests/test_analizadores.py::TestGeneradorResumenes
```

## Contribuir

1. Fork del repositorio
2. Crear rama feature
3. Commit cambios
4. Push a la rama
5. Crear Pull Request

## Contacto y Soporte

- **Desarrollador**: Juan Heriberto Rosas
- **Email**: juanheriberto.rosas@jhrjdata.com
- **Sitio Web**: www.jhrjdata.com
- **Empresa**: www.gobiernodigitaleinnovacion.com

## Licencia

MIT

---
Desarrollado por [JHRJ Data](https://www.jhrjdata.com) | [Gobierno Digital e Innovación](https://www.gobiernodigitaleinnovacion.com)