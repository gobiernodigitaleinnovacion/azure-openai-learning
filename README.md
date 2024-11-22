# Proyecto de Aprendizaje Azure OpenAI

Implementaciones avanzadas de Azure OpenAI para procesamiento de lenguaje natural, análisis de sentimientos, generación de contenido y procesamiento de documentos.

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
# Análisis básico
resultado = analizador.analizar("Me encanta este proyecto")
# Análisis por aspectos
aspectos = analizador.analizar_aspecto("El producto es bueno pero caro", "precio")
# Análisis multilingüe
sentimiento = analizador.analizar_multilingue("C'est excellent!", "fr")
```

### 2. Procesamiento de Documentos
```python
from src.procesador_documentos import ProcesadorDocumentos

procesador = ProcesadorDocumentos()
# Procesar factura
datos_factura = procesador.procesar_factura("texto_factura")
# Analizar contrato
analisis = procesador.analizar_contrato("texto_contrato")
```

### 3. Clasificación de Documentos
```python
from src.clasificador_documentos import ClasificadorDocumentos

categorias = ["Tecnología", "Negocios", "Salud"]
clasificador = ClasificadorDocumentos(categorias)
# Clasificación simple
categoria = clasificador.clasificar("texto a clasificar")
# Clasificación jerárquica
resultado = clasificador.clasificar_jerarquico(texto, ["Software", "Hardware"])
```

### 4. Generador de Contenido
```python
from src.generador_contenido import GeneradorContenido

generador = GeneradorContenido()
# Generar email
email = generador.generar_email("Reunión proyecto", tipo="formal")
# Crear blog
blog = generador.crear_blog("IA en Medicina")
```

## Estructura del Proyecto
azure-openai-learning/
├── src/                    # Código fuente
│   ├── __init__.py
│   ├── analizador_sentimientos.py
│   ├── clasificador_documentos.py
│   ├── generador_resumenes.py
│   ├── procesador_documentos.py
│   ├── generador_contenido.py
│   ├── analizador_datos.py
│   ├── config.py
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

## Pruebas
```bash
pytest tests/
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