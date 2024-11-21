# Proyecto de Aprendizaje Azure OpenAI

Implementaciones de ejemplo para Azure OpenAI con análisis de sentimientos, generación de resúmenes y clasificación de documentos.

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
cp .env 
# Editar .env con tus credenciales
```

## Funcionalidades

### Análisis de Sentimientos
```python
from src.analizador_sentimientos import AnalizadorSentimientos

analizador = AnalizadorSentimientos()
resultado = analizador.analizar("Me encanta este proyecto")
print(resultado)  # POSITIVO
```

### Generación de Resúmenes
```python
from src.generador_resumenes import GeneradorResumenes

generador = GeneradorResumenes()
resumen = generador.resumir("texto largo...", max_palabras=100)
```

### Clasificación de Documentos
```python
from src.clasificador_documentos import ClasificadorDocumentos

categorias = ["Tecnología", "Negocios", "Salud"]
clasificador = ClasificadorDocumentos(categorias)
categoria = clasificador.clasificar("texto a clasificar")
```

## Estructura del Proyecto
```
azure-openai-learning/
├── src/                    # Código fuente
│   ├── analizador_sentimientos.py
│   ├── generador_resumenes.py
│   ├── clasificador_documentos.py
│   └── utils/
│       └── cliente_azure.py
├── tests/                  # Pruebas unitarias
├── examples/               # Notebooks de ejemplo
└── .env                    # Configuración local
```

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
