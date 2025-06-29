## Análisis de la Turistificación y Crisis Habitacional (2024-2025)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3.0+-blue)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Exploratory-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)

## 📋 Descripción del Proyecto

Este proyecto analiza en profundidad el impacto de Airbnb en el mercado inmobiliario de Barcelona, revelando la correlación entre el crecimiento de alojamientos turísticos y la crisis habitacional que enfrenta la ciudad. El análisis se centra en datos del período 2024-2025, cuando se produjo un crecimiento exponencial de 69.6% en nuevos alojamientos Airbnb, coincidiendo con aumentos significativos en los precios de la vivienda.

## 🔍 Objetivos

- Cuantificar el impacto de los alojamientos turísticos en el mercado inmobiliario residencial
- Analizar la distribución geográfica de Airbnb por barrios y su correlación con precios de vivienda
- Evaluar el cumplimiento normativo y la prevalencia de alojamientos sin licencia
- Proporcionar recomendaciones basadas en datos para políticas públicas
- Visualizar los datos de forma interactiva mediante una aplicación web

## 📊 Metodología

El proyecto sigue una metodología rigurosa basada en ciencia de datos:

1. **Preprocesamiento de datos**: Limpieza, normalización y transformación de datos de múltiples fuentes
2. **Análisis exploratorio**: Identificación de patrones, correlaciones y anomalías
3. **Análisis geoespacial**: Visualización de la distribución territorial de alojamientos y precios
4. **Análisis económico**: Cuantificación de rendimientos y distorsiones del mercado
5. **Análisis regulatorio**: Evaluación del cumplimiento normativo por zonas y tipos de anfitrión
6. **Visualización interactiva**: Desarrollo de dashboard con Streamlit

## 💾 Estructura del Repositorio

```
├── data/
│   ├── datos vivienda turistica bcn oficiales.csv    # Datos oficiales de licencias turísticas
│   ├── housing_prices_barcelona_2015_2025.csv        # Serie histórica de precios inmobiliarios
│   ├── limpio_airbnb_Barcelona.csv                   # Dataset limpio y procesado
│   └── listings.csv                                  # Dataset original de Airbnb
├── Código/
│   ├── EDA.ipynb                                     # Análisis exploratorio de datos
│   ├── preprocesamiento.ipynb                        # Limpieza y preparación de datos
│   └── app.py                                        # Aplicación Streamlit
├── Conclusiones y recomandaciones.md                 # Informe completo con hallazgos y recomendaciones
└── README.md                                         # Documentación del proyecto
```

[resto del contenido se mantiene igual...]

## 🔧 Tecnologías Utilizadas

- **Python**: Lenguaje principal de análisis
- **Pandas & NumPy**: Manipulación y análisis de datos
- **Matplotlib & Seaborn**: Visualización de datos
- **Folium**: Visualizaciones geoespaciales interactivas
- **Scikit-learn**: Normalización y procesamiento de datos
- **Streamlit**: Desarrollo de aplicación web interactiva

## 🚀 Aplicación Web

La aplicación web desarrollada con Streamlit permite:
- Visualizar datos interactivamente
- Filtrar información por barrios
- Explorar tendencias temporales
- Comparar métricas clave
- Acceder a mapas interactivos

Para ejecutar la aplicación:
```bash
streamlit run Código/app.py
```

[resto del contenido se mantiene igual...]

