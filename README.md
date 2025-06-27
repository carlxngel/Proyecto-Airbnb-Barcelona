Collecting workspace information# Impacto de Airbnb en el Mercado Inmobiliario de Barcelona

## Análisis de la Turistificación y Crisis Habitacional (2024-2025)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3.0+-blue)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Exploratory-green)

## 📋 Descripción del Proyecto

Este proyecto analiza en profundidad el impacto de Airbnb en el mercado inmobiliario de Barcelona, revelando la correlación entre el crecimiento de alojamientos turísticos y la crisis habitacional que enfrenta la ciudad. El análisis se centra en datos del período 2024-2025, cuando se produjo un crecimiento exponencial de 69.6% en nuevos alojamientos Airbnb, coincidiendo con aumentos significativos en los precios de la vivienda.

## 🔍 Objetivos

- Cuantificar el impacto de los alojamientos turísticos en el mercado inmobiliario residencial
- Analizar la distribución geográfica de Airbnb por barrios y su correlación con precios de vivienda
- Evaluar el cumplimiento normativo y la prevalencia de alojamientos sin licencia
- Proporcionar recomendaciones basadas en datos para políticas públicas

## 📊 Metodología

El proyecto sigue una metodología rigurosa basada en ciencia de datos:

1. **Preprocesamiento de datos**: Limpieza, normalización y transformación de datos de múltiples fuentes
2. **Análisis exploratorio**: Identificación de patrones, correlaciones y anomalías
3. **Análisis geoespacial**: Visualización de la distribución territorial de alojamientos y precios
4. **Análisis económico**: Cuantificación de rendimientos y distorsiones del mercado
5. **Análisis regulatorio**: Evaluación del cumplimiento normativo por zonas y tipos de anfitrión

## 💾 Estructura del Repositorio

```
├── data/
│   ├── datos vivienda turistica bcn oficiales.csv    # Datos oficiales de licencias turísticas
│   ├── housing_prices_barcelona_2015_2025.csv        # Serie histórica de precios inmobiliarios
│   ├── limpio_airbnb_Barcelona.csv                   # Dataset limpio y procesado
│   └── listings.csv                                  # Dataset original de Airbnb
├── Código/
│   ├── EDA.ipynb                                     # Análisis exploratorio de datos
│   └── preprocesamiento.ipynb                        # Limpieza y preparación de datos
├── Conclusiones y recomandaciones.md                 # Informe completo con hallazgos y recomendaciones
└── README.md                                         # Documentación del proyecto
```

## 🔑 Hallazgos Clave

- **Composición del mercado**: 94.4% de los alojamientos (18,343) son gestionados por particulares vs. 5.6% (1,079) por empresas
- **Crecimiento acelerado**: 69.6% del total de alojamientos fueron creados solo en los últimos 24 meses
- **Impacto en precios**: Incremento del 43% en alquileres y 34% en precios de venta (2022-2025)
- **Distorsión económica**: Alojamientos turísticos hasta 6 veces más rentables que alquileres tradicionales
- **Concentración geográfica**: La Dreta de l'Eixample (12.3%), El Raval (8.2%) y Barri Gòtic (6.3%) son los barrios más afectados
- **Incumplimiento normativo**: 32.03% de alojamientos operan sin licencia turística
- **Patrón regulatorio**: Los particulares incumplen más (33.3%) que las empresas (9.9%)

## 📈 Visualizaciones

El repositorio incluye visualizaciones detalladas como:
- Mapas de concentración de alojamientos por barrio
- Gráficos de evolución temporal de precios y oferta
- Visualizaciones del porcentaje de incumplimiento normativo
- Análisis comparativos de rentabilidad por zona

## 🔬 Recomendaciones Basadas en Datos

Basado en el análisis, se proponen recomendaciones estructuradas en:
- **Medidas regulatorias**: Moratoria de licencias y límites máximos por barrio
- **Fiscalidad redistributiva**: Incentivos para reconversión a alquiler residencial
- **Diversificación económica**: Promoción de sectores alternativos no turísticos
- **Gobernanza participativa**: Participación ciudadana en la gestión turística

## 🔧 Tecnologías Utilizadas

- **Python**: Lenguaje principal de análisis
- **Pandas & NumPy**: Manipulación y análisis de datos
- **Matplotlib & Seaborn**: Visualización de datos
- **Folium**: Visualizaciones geoespaciales interactivas
- **Scikit-learn**: Normalización y procesamiento de datos

## 📚 Fuentes de Datos

- Datos de listados Airbnb (Inside Airbnb)
- Registro oficial de licencias turísticas (Gobierno de España)
- Serie histórica de precios inmobiliarios (2015-2025)
- Datos demográficos y urbanísticos de Barcelona

## 👥 Contribuciones

Las contribuciones son bienvenidas. Si desea contribuir:
1. Haga un fork del repositorio
2. Cree una nueva rama (`git checkout -b feature/analysis`)
3. Realice sus cambios y documente adecuadamente
4. Envíe un pull request con descripción detallada

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - vea el archivo LICENSE para más detalles.

## 📧 Contacto

Para cualquier pregunta o sugerencia, no dude en abrir un issue en este repositorio o contactar directamente a los autores.

---

*Este estudio fue realizado con datos contrastados de Airbnb y licencias turísticas oficiales del Gobierno de España para el período 2024-2025.*

Similar code found with 1 license type

