import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from matplotlib import cm
from matplotlib.colors import ListedColormap
import warnings
warnings.filterwarnings("ignore")

# Set page configuration
st.set_page_config(
    page_title="Impacto de Airbnb en Barcelona",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #2563EB;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #3B82F6;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    .subsection-header {
        font-size: 1.2rem;
        color: #60A5FA;
        margin-top: 1.2rem;
        margin-bottom: 0.5rem;
    }
    .highlight {
        background-color: #EFF6FF;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.5rem solid #3B82F6;
        margin-bottom: 1rem;
    }
    .warning {
        background-color: #FEF2F2;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.5rem solid #EF4444;
        margin-bottom: 1rem;
    }
    .info {
        background-color: #ECFDF5;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.5rem solid #10B981;
        margin-bottom: 1rem;
    }
    .metric-container {
        background-color: #F3F4F6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #1E3A8A;
    }
    .metric-label {
        font-size: 1rem;
        color: #4B5563;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #E5E7EB;
        color: #6B7280;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(r'data/limpio_airbnb_Barcelona.csv')
    df2 = pd.read_csv(r'data/datos vivienda turistica bcn oficiales.csv')
    df3 = pd.read_csv(r'data/housing_prices_barcelona_2015_2025.csv')
    return df, df2, df3

try:
    df, df2, df3 = load_data()
    data_load_success = True
except Exception as e:
    st.error(f"Error cargando los datos: {e}")
    data_load_success = False

# Title and Introduction
st.markdown("""
    <div style="
        background: linear-gradient(120deg, #1E3A8A 0%, #3B82F6 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    ">
        <div class="main-header" style="color: white;">Impacto de Airbnb en el Mercado Inmobiliario de Barcelona</div>
        <div style="text-align: center; font-size: 1.5rem; color: #E5E7EB;">Análisis de la Turistificación y Crisis Habitacional (2024-2025)</div>
    </div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navegación")
app_mode = st.sidebar.radio("Secciones:", [
    "📊 Inicio", 
    "🏘️ Estructura del Mercado", 
    "💰 Impacto en Precios", 
    "🗺️ Geografía de la Turistificación", 
    "⚖️ Crisis Regulatoria", 
    "👥 Implicaciones Socioeconómicas", 
    "📝 Recomendaciones", 
    "🔍 Conclusiones"
])

if not data_load_success:
    st.warning("No se pudieron cargar los datos. Algunas visualizaciones no estarán disponibles.")

# Function to create sections
def create_section(title, content):
    st.markdown(f'<div class="section-header">{title}</div>', unsafe_allow_html=True)
    st.markdown(content)

# Function to create metrics
def create_metric_row(metrics_data):
    cols = st.columns(len(metrics_data))
    for i, (title, value, description) in enumerate(metrics_data):
        with cols[i]:
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-value">{value}</div>
                <div class="metric-label">{title}</div>
                <div>{description}</div>
            </div>
            """, unsafe_allow_html=True)

# INICIO
# Resumen Ejecutivo
if app_mode == "📊 Inicio":
    
    st.markdown("""
    <div class="highlight">
    Este estudio analiza el impacto de Airbnb en el mercado inmobiliario barcelonés, revelando una crisis habitacional 
    acelerada por el crecimiento exponencial de alojamientos turísticos. Con 19,422 propiedades activas y un 32% 
    operando sin licencia, Barcelona enfrenta una distorsión del mercado que ha incrementado los precios de alquiler un 43% en tres años.
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    # Calculate metrics from data
    total_listings = len(df)
    unlicensed = len(df[df['license'] == 'sin datos'])
    unlicensed_percentage = (unlicensed / total_listings) * 100
    
    # Calculate price increase from df3
    price_2022 = df3[df3['Year'] == 2022]['Avg_Rental_Price_EUR_month'].values[0]
    price_2025 = df3[df3['Year'] == 2025]['Avg_Rental_Price_EUR_month'].values[0]
    price_increase = ((price_2025 - price_2022) / price_2022) * 100
    
    # Format the numbers with thousand separators
    formatted_total = f"{total_listings:,}"
    formatted_unlicensed = f"{unlicensed:,}"
    
    # Define metrics with more detailed descriptions and consistent spacing
    metrics = [
        ("ALOJAMIENTOS TURÍSTICOS", 
         formatted_total, 
         "Propiedades activas en la plataforma Airbnb en la ciudad Barcelona"),
        
        ("TASA DE CRECIMIENTO", 
         "69.6%", 
         "Incremento en el número de alojamientos registrados entre 2023-2024"),
        
        ("ALOJAMIENTOS IRREGULARES", 
         f"{unlicensed_percentage:.1f}%", 
         f"Un total de {formatted_unlicensed} propiedades operan sin licencia turística"),
        
        ("INCREMENTOS DE PRECIO", 
         f"+{price_increase:.1f}%", 
         "Aumento en el precio medio del alquiler residencial entre 2022-2025")
    ]
    create_metric_row(metrics)
    
    if data_load_success:
        # Add section header for map
        st.markdown("""
        <div class="section-header">
            Distribución Geográfica de Alojamientos
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info">
            Explora la distribución de los alojamientos turísticos en Barcelona. El tamaño de los puntos representa 
            el rendimiento económico mensual y el color distingue entre anfitriones particulares y profesionales.
        </div>
        """, unsafe_allow_html=True)

        # Create filter for license status with custom styling
        st.markdown("""
            <style>
            div[data-baseweb="radio"] {
            background: linear-gradient(to right, #f8fafc, #f1f5f9);
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            }
            div[data-baseweb="radio"] > label {
            background-color: #ffffff;
            padding: 12px 24px;
            border-radius: 10px;
            margin-right: 12px;
            transition: all 0.2s ease;
            border: 1px solid #e2e8f0;
            }
            div[data-baseweb="radio"] > label:hover {
            background-color: #3b82f6;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(59, 130, 246, 0.1);
            }
            div[data-baseweb="radio"] > label[data-checked="true"] {
            background-color: #2563eb;
            color: white;
            border-color: #2563eb;
            }
            div[data-testid="stHorizontalBlock"] {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            }
            </style>
        """, unsafe_allow_html=True)

        license_filter = st.radio(
            "Mostrar alojamientos:",
            ["Todos", "Sin licencia", "Con licencia"],
            horizontal=True
        )

        # Filter data based on selection
        if license_filter == "Sin licencia":
            map_data = df[df['license'] == 'sin datos']
        elif license_filter == "Con licencia":
            map_data = df[df['license'] != 'sin datos']
        else:
            map_data = df

        # Create the map
        fig = px.scatter_mapbox(
            map_data,
            lat='latitude',
            lon='longitude',
            color='tipo_anfitrion',
            size='rendimiento_economico_mensual',
            hover_name='neighbourhood',
            hover_data={
            'license': True,
            'rendimiento_economico_mensual': ':.2f €',
            'room_type': True,
            'latitude': False,
            'longitude': False
            },
            color_discrete_sequence=['#3B82F6', '#EF4444'],  # More contrasting colors
            size_max=15,  # Control maximum marker size
            zoom=12,
            labels={
            'tipo_anfitrion': 'Tipo de Anfitrión',
            'rendimiento_economico_mensual': 'Rendimiento Mensual (€)',
            'room_type': 'Tipo de Alojamiento',
            'license': 'Licencia'
            }
        )

        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox=dict(
            center=dict(lat=41.3851, lon=2.1734)
            ),
            height=700,  # Increased height
            margin=dict(l=0, r=0, t=30, b=0),  # Adjusted margins
            legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(255, 255, 255, 0.8)'  # Semi-transparent background
            )
        )

        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("""
<div class="footer">
<i>Estudio realizado por Carla Molina para Upgrade Hub en 2025, basado en datos contrastados de Airbnb y licencias turísticas oficiales del Gobierno de España.</i>
</div>
""", unsafe_allow_html=True)
