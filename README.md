# 🏠 Análisis de la Turistificación y Crisis Habitacional (2024-2025)

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3.0+-blue)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Exploratory-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)

</div>

## 📋 Descripción del Proyecto

Este proyecto analiza en profundidad el impacto de Airbnb en el mercado inmobiliario de Barcelona, revelando la correlación entre el crecimiento de alojamientos turísticos y la crisis habitacional que enfrenta la ciudad. El análisis se centra en datos del período 2024-2025, cuando se produjo un crecimiento exponencial de 69.6% en nuevos alojamientos Airbnb, coincidiendo con aumentos significativos en los precios de la vivienda.

### Objetivos Principales
- 🎯 **Objetivo 1:** Cuantificar con precisión el impacto económico de la turistificación en los precios residenciales
- 🎯 **Objetivo 2:** Identificar los patrones geográficos de concentración y expansión de alojamientos turísticos
- 🎯 **Objetivo 3:** Evaluar el cumplimiento normativo por zonas y tipos de operadores
- 🎯 **Objetivo 4:** Desarrollar recomendaciones basadas en datos para políticas públicas de vivienda

## 💾 Estructura del Repositorio

```plaintext
📁 Proyecto-2/
│
├── 📊 data/
│   ├── datos_vivienda_turistica_bcn_oficiales.csv    # Datos oficiales de licencias turísticas
│   ├── housing_prices_barcelona_2015_2025.csv        # Serie histórica de precios inmobiliarios
│   ├── limpio_airbnb_Barcelona.csv                   # Dataset limpio y procesado
│   └── listings.csv                                  # Dataset original de Airbnb
│
├── 💻 Código/
│   ├── EDA.ipynb                                     # Análisis exploratorio de datos
│   ├── preprocesamiento.ipynb                        # Limpieza y preparación de datos
│   └── app.py                                        # Aplicación Streamlit
│
├── 📝 Conclusiones y recomendaciones.md              # Informe completo con hallazgos
└── 📘 README.md                                      # Documentación del proyecto
```

## 🔍 Top 3 Insights Principales

### 1️⃣ Crecimiento Explosivo No Orgánico (69.6% en 24 meses)
<div align="center">
</div>

El 69.6% de los alojamientos Airbnb actuales fueron creados en los últimos 24 meses (2024-2025), evidenciando un crecimiento exponencial y no orgánico que coincide con un incremento del 43% en precios de alquiler residencial.


### 2️⃣ Distorsión Económica Estructural (6x Factor Multiplicador)
<div align="center">
</div>

Los alojamientos turísticos generan hasta 6 veces más ingresos que el alquiler residencial tradicional (hasta €7,285/mes vs €1,200/mes), creando un incentivo económico que hace irracional mantener viviendas en el mercado residencial.


### 3️⃣ Patrón de Incumplimiento Regulatorio (32% Sin Licencia)
<div align="center">
</div>

El 32.03% de alojamientos (6,222 propiedades) operan sin licencia turística, con marcada diferencia entre particulares (33.3% irregulares) y empresas (9.9%), mostrando un fallo sistémico regulatorio que afecta desproporcionadamente a barrios periféricos.

## 📊 Dashboard Interactivo

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://insideairbnbbarcelona.streamlit.app/)

</div>

### Funcionalidades:
- 🔍 Filtrar datos por barrio, tipo de anfitrión y estado de licencia
- 🗺️ Visualizar mapas interactivos de concentración de alojamientos
- 📈 Comparar tendencias de precios residenciales vs. turísticos
- 📊 Explorar métricas de rendimiento económico
- 📝 Acceder a recomendaciones detalladas por zona

## 🔧 Stack Tecnológico

### 🛠️ Tecnologías Utilizadas

<div align="center">

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.8+ | Lenguaje principal de programación |
| Pandas & NumPy | 1.3+ | Manipulación y procesamiento de datos |
| Matplotlib & Seaborn | Latest | Visualizaciones estáticas y análisis |
| Plotly | 5.10+ | Gráficos interactivos para dashboard |
| Streamlit | 1.28+ | Desarrollo de aplicación web |
| Scikit-learn | Latest | Normalización y segmentación |
| Git & GitHub | -- | Control de versiones |

</div>

