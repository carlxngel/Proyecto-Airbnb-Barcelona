## Análisis de la Turistificación y Crisis Habitacional (2024-2025)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3.0+-blue)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Exploratory-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)

## 📋 Descripción del Proyecto

Este proyecto analiza en profundidad el impacto de Airbnb en el mercado inmobiliario de Barcelona, revelando la correlación entre el crecimiento de alojamientos turísticos y la crisis habitacional que enfrenta la ciudad. El análisis se centra en datos del período 2024-2025, cuando se produjo un crecimiento exponencial de 69.6% en nuevos alojamientos Airbnb, coincidiendo con aumentos significativos en los precios de la vivienda.

Objetivo 1: Cuantificar con precisión el impacto económico de la turistificación en los precios residenciales
Objetivo 2: Identificar los patrones geográficos de concentración y expansión de alojamientos turísticos
Objetivo 3: Evaluar el cumplimiento normativo por zonas y tipos de operadores
Objetivo 4: Desarrollar recomendaciones basadas en datos para políticas públicas de vivienda

## 🔍 Top 3 Insights Principales

1️⃣ Crecimiento Explosivo No Orgánico (69.6% en 24 meses)
<img alt="Gráfico de Crecimiento" src="https://i.imgur.com/FRxGcZ5.png">
El 69.6% de los alojamientos Airbnb actuales fueron creados en los últimos 24 meses (2024-2025), evidenciando un crecimiento exponencial y no orgánico que coincide con un incremento del 43% en precios de alquiler residencial.

2️⃣ Distorsión Económica Estructural (6x Factor Multiplicador)
<img alt="Distorsión Económica" src="https://i.imgur.com/LR8nSfM.png">
Los alojamientos turísticos generan hasta 6 veces más ingresos que el alquiler residencial tradicional (hasta €7,285/mes vs €1,200/mes), creando un incentivo económico que hace irracional mantener viviendas en el mercado residencial.

3️⃣ Patrón de Incumplimiento Regulatorio (32% Sin Licencia)
<img alt="Mapa de Incumplimiento" src="https://i.imgur.com/PtQnxZ2.png">
El 32.03% de alojamientos (6,222 propiedades) operan sin licencia turística, con marcada diferencia entre particulares (33.3% irregulares) y empresas (9.9%), mostrando un fallo sistémico regulatorio que afecta desproporcionadamente a barrios periféricos.

## 📊 Dashboard Interactivo
Explore nuestro dashboard interactivo para profundizar en los datos y crear sus propios análisis:


<img alt="Streamlit App" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg">
URL del Dashboard: https://insideairbnbbarcelona.streamlit.app/

El dashboard permite:

Filtrar datos por barrio, tipo de anfitrión y estado de licencia
Visualizar mapas interactivos de concentración de alojamientos
Comparar tendencias de precios residenciales vs. turísticos
Explorar métricas de rendimiento económico
Acceder a recomendaciones detalladas por zona

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

## 📸 Visualizaciones Destacadas

Distribución Geográfica de Alojamientos
<img alt="Mapa de Calor" src="https://i.imgur.com/jKLZd1H.png">
Mapa interactivo mostrando la distribución de alojamientos turísticos, con color diferenciando entre particulares y empresas, y tamaño representando el rendimiento económico mensual.

Escalada de Precios Inmobiliarios (2015-2025)
<img alt="Evolución de Precios" src="https://i.imgur.com/wN0FYpC.png">
Evolución del precio de venta (€/m²) y alquiler (€/mes) en Barcelona, mostrando el incremento acelerado desde 2022.

Top 10 Barrios más Afectados
<img alt="Ranking de Barrios" src="https://i.imgur.com/RVs1kGt.png">
Barrios con mayor porcentaje de viviendas turísticas, destacando La Dreta de l'Exemple con 12.3% de sus viviendas convertidas en alojamientos turísticos.

## 🔧 Stack Tecnológico

Tecnologías Utilizadas
Python (3.8+): Lenguaje principal de programación
Pandas (1.3+) & NumPy: Manipulación y procesamiento de datos
Matplotlib & Seaborn: Visualizaciones estáticas y análisis exploratorio
Plotly (5.10+): Gráficos interactivos para el dashboard
Streamlit (1.28+): Desarrollo de aplicación web interactiva
Scikit-learn: Normalización de datos y segmentación de mercado
Git & GitHub: Control de versiones y colaboración

## 📚 Fuentes de Datos

Inside Airbnb (Datos de alojamientos turísticos): http://insideairbnb.com/barcelona/
Registro de Turismo de Cataluña (Licencias oficiales): https://registreturisme.catalunya.cat/
Idealista (Precios históricos residenciales): https://www.idealista.com/data/
INE (Datos socioeconómicos): https://www.ine.es/

