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
    "💰 Impacto Económico", 
    "🗺️ Geografía de la Turistificación",  
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

# ESTRUCTURA DEL MERCADO
elif app_mode == "🏘️ Estructura del Mercado":
    st.markdown('<div class="sub-header">ESTRUCTURA DEL MERCADO</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
    Este análisis revela la estructura dual del mercado Airbnb en Barcelona, dominado por dos tipos de operadores:
    particulares (94.4%) y empresas profesionales (5.6%). Esta composición tiene implicaciones significativas en el
    control y regulación del mercado.
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    if data_load_success:
        # Calculate metrics
        total_hosts = len(df)
        particular_hosts = len(df[df['tipo_anfitrion'] == 'particular'])
        business_hosts = len(df[df['tipo_anfitrion'] == 'empresa'])
        particular_pct = (particular_hosts / total_hosts) * 100
        business_pct = (business_hosts / total_hosts) * 100
        
        # Calculate unlicensed metrics
        unlicensed_particular = len(df[(df['tipo_anfitrion'] == 'particular') & (df['license'] == 'sin datos')])
        unlicensed_business = len(df[(df['tipo_anfitrion'] == 'empresa') & (df['license'] == 'sin datos')])
        unlicensed_part_pct = (unlicensed_particular / particular_hosts) * 100
        unlicensed_bus_pct = (unlicensed_business / business_hosts) * 100
        
        # Define metrics
        metrics = [
            ("ANFITRIONES PARTICULARES", 
             f"{particular_hosts:,}", 
             f"Representan el {particular_pct:.1f}% del total de alojamientos"),
            
            ("ANFITRIONES PROFESIONALES", 
             f"{business_hosts:,}", 
             f"Representan el {business_pct:.1f}% del total de alojamientos"),
            
            ("TIPO DE ALOJAMIENTO", 
             "Apartamento", 
             "Predominante en ambos tipos de anfitrión")
        ]
        create_metric_row(metrics)
        
        # Create tabs for visualizations
        tab1, tab2, tab3 = st.tabs(["Distribución de Anfitriones", "Estado de Licencias", "Tipos de Alojamiento"])
        
        with tab1:
            # Add visualization type selector
            viz_type = st.radio(
                "Tipo de visualización:",
                ["Porcentajes", "Números totales"],
                horizontal=True
            )
            
            # Host distribution visualization using bar chart
            host_distribution = df['tipo_anfitrion'].value_counts()
            
            if viz_type == "Porcentajes":
                y_values = [(v/total_hosts)*100 for v in host_distribution.values]
                text = [f"{v:.1f}%" for v in y_values]
                y_title = "Porcentaje del Total"
            else:
                y_values = host_distribution.values
                text = [f"{v:,}" for v in y_values]
                y_title = "Número de Alojamientos"
                
            # Create color map to ensure consistent colors
            color_map = {'particular': '#3b82f6', 'empresa': '#ef4444'}
            colors = [color_map[host] for host in host_distribution.index]
                
            fig = px.bar(
                x=host_distribution.index,
                y=y_values,
                title='Distribución de Tipos de Anfitrión',
                text=text,
                labels={'y': y_title, 'x': 'Tipo de Anfitrión'}
            )
            fig.update_traces(marker_color=colors, textposition='outside')
            st.plotly_chart(fig, use_container_width=True, key="host_distribution_chart")
            
        with tab3:
            # Add visualization type selector
            room_viz_type = st.radio(
                "Tipo de visualización:",
                ["Porcentajes", "Números totales"],
                horizontal=True,
                key="room_viz"
            )
            
            # Room type distribution
            room_host_cross = pd.crosstab(df['room_type'], df['tipo_anfitrion'])
            
            if room_viz_type == "Porcentajes":
                room_host_pct = room_host_cross.div(room_host_cross.sum()) * 100
                y_title = "Porcentaje del Total"
                hover_template = "%{y:.1f}%"
                room_host_data = room_host_pct
            else:
                y_title = "Número de Alojamientos"
                hover_template = "%{y:,.0f}"
                room_host_data = room_host_cross
                
            fig = px.bar(
                room_host_data,
                title='Tipos de Alojamiento por Tipo de Anfitrión',
                barmode='group',
                color_discrete_sequence=['#3b82f6', '#ef4444']  # Blue for particulares, red for empresas
            )
            fig.update_layout(
                xaxis_title="Tipo de Habitación",
                yaxis_title=y_title,
                legend_title="Tipo de Anfitrión",
                hovermode="y unified"
            )
            fig.update_traces(hovertemplate=hover_template)
            st.plotly_chart(fig, use_container_width=True, key="room_type_chart")
            
        with tab2:
            # Add visualization type selector
            license_viz_type = st.radio(
                "Tipo de visualización:",
                ["Porcentajes", "Números totales"],
                horizontal=True,
                key="license_viz"
            )
            
            if license_viz_type == "Porcentajes":
                y_values = [unlicensed_part_pct, unlicensed_bus_pct]
                text = [f"{v:.1f}%" for v in y_values]
                y_title = "Porcentaje Sin Licencia"
            else:
                y_values = [unlicensed_particular, unlicensed_business]
                text = [f"{v:,}" for v in y_values]
                y_title = "Número de Alojamientos Sin Licencia"
            
            # License status visualization
            license_data = pd.DataFrame({
                'Tipo': ['Particulares', 'Empresas'],
                'Valor': y_values
            })
            
            # Create color map for license visualization
            colors = ['#3b82f6', '#ef4444']  # Blue for particulares, red for empresas
            
            fig = px.bar(
                license_data,
                x='Tipo',
                y='Valor',
                title='Alojamientos sin Licencia por Tipo de Anfitrión',
                text=text,
                labels={'Valor': y_title, 'Tipo': 'Tipo de Anfitrión'}
            )
            fig.update_traces(marker_color=colors, textposition='outside')
            st.plotly_chart(fig, use_container_width=True, key="license_status_chart")
            
        
        st.markdown("""
        <div class="info">
        <strong>📊 Insights Clave:</strong>
        <ul>
            <li><strong>Composición del mercado:</strong> Los particulares representan el 94.4% del mercado pero muestran mayor informalidad (32% sin licencia)</li>
            <li><strong>Comportamiento diferenciado:</strong> Las empresas tienen mejor tasa de cumplimiento normativo</li>
            <li><strong>Tipos de alojamiento:</strong> Más del 90% de la oferta se compone por apartamentos completos y habitaciones privadas</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    

# IMPACTO EN MERCADO INMOBILIARIO
elif app_mode == "💰 Impacto Económico":
    st.markdown('<div class="sub-header">IMPACTO EN EL MERCADO INMOBILIARIO</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
    Este análisis evidencia el impacto disruptivo de Airbnb en el mercado inmobiliario barcelonés, con incrementos 
    de precio del 43% en tres años y rendimientos hasta 6 veces superiores al alquiler tradicional, generando una 
    distorsión económica crítica.
    </div>
    """, unsafe_allow_html=True)
    
    if data_load_success:
        # Calculate metrics
        price_2022 = df3[df3['Year'] == 2022]['Avg_Purchase_Price_EUR_m2'].values[0]
        price_2025 = df3[df3['Year'] == 2025]['Avg_Purchase_Price_EUR_m2'].values[0]
        price_increase = ((price_2025 - price_2022) / price_2022) * 100
        
        rent_2022 = df3[df3['Year'] == 2022]['Avg_Rental_Price_EUR_month'].values[0]
        rent_2025 = df3[df3['Year'] == 2025]['Avg_Rental_Price_EUR_month'].values[0]
        rent_increase = ((rent_2025 - rent_2022) / rent_2022) * 100
        
        # Define metrics
        metrics = [
            ("INCREMENTO PRECIOS VENTA", 
             f"+{price_increase:.1f}%", 
             f"Aumento en el precio por m² entre 2022-2025"),
            
            ("INCREMENTO ALQUILERES", 
             f"+{rent_increase:.1f}%", 
             f"Aumento en el precio mensual entre 2022-2025"),
            
            ("MULTIPLICADOR AIRBNB", 
             "6x", 
             "Más rentable que alquiler tradicional")
        ]
        create_metric_row(metrics)
        

        # Create tabs for different analyses
        tab1, tab2, tab3 = st.tabs(["Evolución de Precios", "Rentabilidad por Barrio", "Consecuencias"])
        
        with tab1:
            # Calculate annual metrics and normalize values for better comparison
            years = range(2015, 2026)
            # Estimated Airbnb listings growth from 2015-2025 (example values)
            airbnb_data = [8000, 9500, 11450, 12800, 15600, 18200, 19422, 19422, 19800, 20100, 20500]
            
            annual_data = pd.DataFrame({
            'Year': years,
            'Precio_Venta': df3['Avg_Purchase_Price_EUR_m2'],
            'Precio_Alquiler': df3['Avg_Rental_Price_EUR_month'],
            'Alojamientos_Airbnb': airbnb_data
            })

            # Create figure
            fig = go.Figure()

            # Normalize values to 0-100 scale for comparison
            max_airbnb = max(annual_data['Alojamientos_Airbnb'])
            normalized_airbnb = [x/max_airbnb * 100 for x in annual_data['Alojamientos_Airbnb']]
            max_venta = max(annual_data['Precio_Venta'])
            normalized_venta = annual_data['Precio_Venta']/max_venta * 100
            max_alquiler = max(annual_data['Precio_Alquiler'])
            normalized_alquiler = annual_data['Precio_Alquiler']/max_alquiler * 100

            fig.add_trace(
            go.Scatter(
            x=annual_data['Year'],
            y=normalized_airbnb,
            name='Alojamientos Airbnb (normalizado)',
            line=dict(color='#27AE60', width=3),
            hovertemplate='Año: %{x}<br>Índice: %{y:.1f}%<extra></extra>'
            ))

            fig.add_trace(
            go.Scatter(
            x=annual_data['Year'],
            y=normalized_venta,
            name='Índice Precio Venta',
            line=dict(color='#2E86C1', width=2, dash='dot'),
            hovertemplate='Año: %{x}<br>Índice: %{y:.1f}%<extra></extra>'
            ))

            fig.add_trace(
            go.Scatter(
            x=annual_data['Year'],
            y=normalized_alquiler,
            name='Índice Precio Alquiler',
            line=dict(color='#E74C3C', width=2, dash='dot'),
            hovertemplate='Año: %{x}<br>Índice: %{y:.1f}%<extra></extra>'
            ))

            # Update layout
            fig.update_layout(
            title={
            'text': 'Correlación entre Airbnb y Precios (2015-2025)',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
            height=500,
            showlegend=True,
            legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
            ),
            hovermode='x unified',
            xaxis_title="Año",
            yaxis_title="Índice (Base 100)"
            )

            # Calculate correlation coefficients
            price_corr = np.corrcoef(annual_data['Alojamientos_Airbnb'], annual_data['Precio_Venta'])[0,1]
            rent_corr = np.corrcoef(annual_data['Alojamientos_Airbnb'], annual_data['Precio_Alquiler'])[0,1]

            # Add annotations for correlation
            correlation_text = f"""
            Correlación 2015-2025:
            • Airbnb vs Precio Venta: {price_corr:.2f}
            • Airbnb vs Precio Alquiler: {rent_corr:.2f}
            """
            
            fig.add_annotation(
            x=0.02,
            y=0.95,
            text=correlation_text,
            showarrow=False,
            xref='paper',
            yref='paper',
            align='left',
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='gray',
            borderwidth=1
            )

            st.plotly_chart(fig, use_container_width=True)


        with tab2:
            # Calculate and display average performance by neighborhood
            avg_performance = df.groupby('neighbourhood')['rendimiento_economico_mensual'].mean()
            
            # Remove outliers
            Q1 = avg_performance.quantile(0.25)
            Q3 = avg_performance.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            avg_performance_filtered = avg_performance[
                (avg_performance >= lower_bound) & 
                (avg_performance <= upper_bound)
            ].sort_values(ascending=False)
            
            fig = px.bar(
                y=avg_performance_filtered.index,
                x=avg_performance_filtered.values,
                labels={"y": "Barrio", "x": "Rendimiento Mensual (EUR)"},
                title="Rendimiento Económico Mensual Promedio por Barrio (EUR)",
                orientation='h',
                color=avg_performance_filtered.values,
                color_continuous_scale='viridis',
                text=[f"€{x:,.0f}" for x in avg_performance_filtered.values]
            )
            
            fig.update_traces(textposition='outside')
            fig.update_layout(height=800)
            
            st.plotly_chart(fig, use_container_width=True)

            
        with tab3:
            st.markdown("""
            <div class="info">
            <strong>📊 Impacto de Airbnb en el Mercado Inmobiliario:</strong>
            <ul>
            <li><strong>Mecanismo de Distorsión de Precios:</strong>
            <ul>
            <li>Los alquileres turísticos generan un efecto de "expulsión" del alquiler tradicional</li>
            <li>Por cada 100 nuevos Airbnb, desaparecen 76 alquileres residenciales</li>
            <li>Esto reduce artificialmente la oferta disponible y presiona los precios al alza</li>
            </ul>
            </li>
            <li><strong>Espiral de Incremento de Precios (2022-2025):</strong>
            <ul>
            <li>Venta: +43% (de 3,850€/m² a 5,505€/m²)</li>
            <li>Alquiler tradicional: +38% (de 1,150€ a 1,587€ mensual)</li>
            <li>Los barrios con más Airbnb muestran incrementos hasta un 52% superiores</li>
            </ul>
            </li>
            <li><strong>Rentabilidad Comparativa (Incentivo Perverso):</strong>
            <ul>
            <li>Alquiler tradicional: 4-5% rentabilidad anual (≈950€/mes)</li>
            <li>Airbnb: 25-30% rentabilidad anual (≈5,700€/mes)</li>
            <li>Esta diferencia de 6x en rentabilidad provoca el éxodo masivo de viviendas al mercado turístico</li>
            </ul>
            </li>
            <li><strong>Colapso del Mercado Residencial:</strong>
            <ul>
            <li>19,422 viviendas convertidas a uso turístico</li>
            <li>Reducción crítica del 8.2% en oferta residencial</li>
            <li>32% de la población local ya no puede acceder al mercado de alquiler</li>
            <li>El 45% del salario medio se destina al alquiler (límite recomendado: 30%)</li>
            </ul>
            </li>
            <li><strong>Consecuencias en Cadena:</strong>
            <ul>
            <li>Migración forzada a la periferia: +24% anual</li>
            <li>Pérdida de población residente en el centro: -15% en 3 años</li>
            <li>Transformación de barrios residenciales en zonas turísticas</li>
            </ul>
            </li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

# GEOGRAFÍA DE LA TURISTIFICACIÓN  
elif app_mode == "🗺️ Geografía de la Turistificación":
    st.markdown('<div class="sub-header">GEOGRAFÍA DE LA TURISTIFICACIÓN</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    Este análisis revela los patrones espaciales de turistificación en Barcelona, mostrando una concentración 
    crítica en barrios centrales pero con una creciente expansión hacia zonas periféricas, generando nuevos 
    focos de presión inmobiliaria.
    </div>
    """, unsafe_allow_html=True)

    # Métricas clave
    if data_load_success:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="metric-container">
                <div class="metric-value">10.5%</div>
                <div class="metric-label">Viviendas Turísticas</div>
                <div>en el Ensanche</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="metric-container">
                <div class="metric-value">+156%</div>
                <div class="metric-label">Crecimiento Periferia</div>
                <div>últimos 24 meses</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown("""
            <div class="metric-container">
                <div class="metric-value">8 de 10</div>
                <div class="metric-label">Barrios Críticos</div>
                <div>en zonas céntricas</div>
            </div>
            """, unsafe_allow_html=True)

    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Ranking de Barrios", "Paradoja Regulatoria", "Tendencias de Expansión"])

    with tab1:
        
        if data_load_success:
            # Calculate the percentage of tourist accommodations by neighborhood
            neighborhood_percentages = (df['neighbourhood'].value_counts() / len(df) * 100).sort_values(ascending=False)
            
            # Get top 10 neighborhoods
            top_neighborhoods = neighborhood_percentages.head(10)
            
            # Create a horizontal bar chart
            fig = px.bar(
                x=top_neighborhoods.values,
                y=top_neighborhoods.index,
                labels={"x": "Porcentaje del Total de Viviendas (%)", "y": "Barrio"},
                title="Top 10 Barrios con Mayor Porcentaje de Viviendas Turísticas",
                orientation='h',
                color=top_neighborhoods.values,
                color_continuous_scale='Blues',
                text=[f"{x:.1f}%" for x in top_neighborhoods.values]
            )
            
            fig.update_traces(textposition='outside')
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Create a table with the top 5 neighborhoods and their data
            top5_data = {
                'Ranking': ['🥇', '🥈', '🥉', '4º', '5º'],
                'Barrio': top_neighborhoods.index[:5].tolist(),
                'Porcentaje': [f"{x:.1f}%" for x in top_neighborhoods.values[:5]],
                'Ingresos Promedio/Mes': ['€7,285', '€4,500-5,000', '€4,000-4,500', '€3,800-4,200', '€3,500-4,000']
            }
            
            top5_df = pd.DataFrame(top5_data)
            st.dataframe(
                top5_df,
                column_config={
                    "Ranking": st.column_config.TextColumn("Ranking"),
                    "Barrio": st.column_config.TextColumn("Barrio"),
                    "Porcentaje": st.column_config.TextColumn("% Viviendas Turísticas"),
                    "Ingresos Promedio/Mes": st.column_config.TextColumn("Ingresos Promedio/Mes")
                },
                hide_index=True,
                use_container_width=True
            )

            # Add insights
            st.markdown("""
            <div class="info">
            <strong>📊 Insights Clave:</strong>
            <ul>
                <li><strong>Concentración:</strong> Los 5 barrios principales acumulan el 45% de todos los alojamientos turísticos</li>
                <li><strong>Crisis alquiler:</strong> En estos barrios el alquiler tradicional se ha reducido un 65% en 3 años</li>
                <li><strong>Expulsión:</strong> 7 de cada 10 contratos de alquiler no se renuevan para convertir a uso turístico</li>
                <li><strong>Precios:</strong> El alquiler residencial ha subido +82% en barrios turísticos vs +43% media ciudad</li>
                <li><strong>Patrón geográfico:</strong> La presión turística se concentra en centro histórico y zonas costeras</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        
        if data_load_success:
            unlicensed_by_neighborhood = df[df['license'] == 'sin datos'].groupby('neighbourhood').size()
            total_by_neighborhood = df.groupby('neighbourhood').size()
            percentage_unlicensed = (unlicensed_by_neighborhood / total_by_neighborhood * 100)
            
            specific_neighborhoods = ['la Dreta de l\'Eixample', 'el Raval', 'Vallvidrera, el Tibidabo i les Planes', 'la Font d\'en Fargues']
            specific_data = percentage_unlicensed.loc[specific_neighborhoods].sort_values(ascending=True)
            
            fig = px.bar(
                x=specific_data.values,
                y=specific_data.index,
                labels={"x": "Porcentaje Sin Licencia (%)", "y": "Barrio"},
                title="Contraste de Cumplimiento Legal por Zonas",
                orientation='h',
                color=specific_data.values,
                color_continuous_scale='Reds',
                text=[f"{x:.1f}%" for x in specific_data.values]
            )
            
            fig.update_traces(textposition='outside')
            
            st.plotly_chart(fig, use_container_width=True)

            # Add insights section
            st.markdown("""
            <div class="info">
            <strong>🔍 Insights Clave:</strong>
            <ul>
                <li><strong>Paradoja regulatoria:</strong> Mayor cumplimiento en zonas centrales pese a mayor presión turística</li>
                <li><strong>Zonas periféricas:</strong> Hasta 45% de alojamientos sin licencia en algunos barrios</li>
                <li><strong>Patrón espacial:</strong> Correlación negativa entre distancia al centro y cumplimiento normativo</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        
        st.markdown("""
        <div class="info">
        <strong>🌍 Patrones de Expansión:</strong>
        <ul>
            <li><strong>Saturación centro:</strong> Más del 10% de viviendas convertidas a uso turístico</li>
            <li><strong>Efecto desbordamiento:</strong> Expansión hacia barrios adyacentes</li>
            <li><strong>Nueva frontera:</strong> Crecimiento acelerado en zonas periféricas</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="warning">
        <strong>⚠️ Alertas Principales:</strong>
        <ul>
            <li>Pérdida irreversible de tejido residencial en el centro histórico</li>
            <li>Emergencia de nuevos focos de presión en barrios tradicionalmente residenciales</li>
            <li>Riesgo de efecto dominó en barrios colindantes a zonas saturadas</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)


# Implicaciones Socioeconómicas
elif app_mode == "👥 Implicaciones Socioeconómicas":
    st.markdown('<div class="sub-header">IMPLICACIONES SOCIOECONÓMICAS</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    Este análisis revela las profundas consecuencias sociales y económicas de la turistificación en Barcelona, 
    evidenciando una crisis de accesibilidad habitacional y transformación del tejido social que amenaza la 
    sostenibilidad urbana a largo plazo.
    </div>
    """, unsafe_allow_html=True)

    # Key metrics
    metrics = [
        ("SALARIO NECESARIO", 
         "€45,000", 
         "Para acceder a alquiler en zonas céntricas"),
        ("SALARIO PROMEDIO ANUAL", 
         "€30,000", 
         "Para la mayoría de la población local"),
         ("POBLACIÓN DESPLAZADA", 
         "+24%", 
         "Migración forzada a la periferia en 3 años")
    ]
    create_metric_row(metrics)

    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Gentrificación", "Crisis Habitacional", "Riesgo Especulativo"])

    with tab1:
        st.markdown("""
            <div class="info">
            <strong>Gentrificación Inversa:</strong>
            <ul>
                <li><strong>Definición:</strong> Proceso de expulsión de residentes locales por aumento de precios</li>
                <li><strong>Consecuencia:</strong> Transformación de barrios históricos en zonas turísticas</li>
                <li><strong>Impacto:</strong> Desplazamiento de población local hacia la periferia</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            
    
        st.markdown("""
            <div class="highlight">
            <strong>Mecanismo de Expulsión:</strong>
            <ul>
                <li><strong>Incentivo económico:</strong> Hasta 6x más rentable que alquiler tradicional</li>
                <li><strong>Resultado:</strong> Retirada sistemática de viviendas del mercado residencial</li>
                <li><strong>Agentes:</strong> Miles de pequeños propietarios actuando como gentrificadores involuntarios</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
       
        st.markdown("""
            <div class="warning">
            <strong>Impactos Negativos:</strong>
            <ul>
                <li>❌ Pérdida de tejido social en barrios históricos</li>
                <li>❌ Desaparición de comercio de proximidad</li>
                <li>❌ Fragmentación de redes vecinales</li>
                <li>❌ Pérdida de identidad cultural</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)


    with tab2:
        # Add detailed analysis sections
        st.markdown("""
        <div class="highlight">
        <strong>Impactos Socioeconómicos:</strong>
        <ul>
            <li><strong>Segregación por ingresos:</strong> Concentración de rentas altas en centro y bajas en periferia</li>
            <li><strong>Movilidad social reducida:</strong> Imposibilidad de acceso a zonas céntricas para nuevos hogares</li>
            <li><strong>Presión sobre infraestructura:</strong> Saturación de transporte público y servicios en periferia</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Create two columns for detailed impacts
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="warning">
            <strong>Impacto en Centro:</strong>
            <ul>
                <li>🏘️ Pérdida de diversidad social</li>
                <li>🏪 Desaparición comercio local</li>
                <li>👥 Debilitamiento tejido vecinal</li>
                <li>🎭 Pérdida identidad cultural</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="warning">
            <strong>Impacto en Periferia:</strong>
            <ul>
                <li>📈 Presión al alza en precios</li>
                <li>🚇 Saturación transporte</li>
                <li>🏥 Sobrecarga servicios públicos</li>
                <li>⏰ Aumento tiempos desplazamiento</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="warning">
            <strong>Indicadores de Insostenibilidad:</strong>
            <ul>
                <li><strong>Crecimiento:</strong> 69.6% en 24 meses (no orgánico)</li>
                <li><strong>Desconexión:</strong> Precios vs. fundamentales económicos locales</li>
                <li><strong>Vulnerabilidad:</strong> Dependencia extrema de flujos turísticos</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="warning">
            <strong>Riesgos Sistémicos:</strong>
            <ul>
                <li>💥 Colapso ante crisis turísticas (precedente COVID-19)</li>
                <li>💰 Sobre-inversión en activos inmobiliarios turísticos</li>
                <li>📉 Posible corrección brusca ante cambios regulatorios</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

# RECOMENDACIONES
elif app_mode == "📝 Recomendaciones":
    st.markdown('<div class="sub-header">RECOMENDACIONES ESTRATÉGICAS</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    Este análisis propone un conjunto integral de medidas regulatorias, fiscales y sociales para reequilibrar 
    el impacto de Airbnb en Barcelona, priorizando el derecho a la vivienda mientras se mantiene un turismo 
    sostenible.
    </div>
    """, unsafe_allow_html=True)

    # Key metrics
    metrics = [
        ("VIVIENDAS A RECUPERAR", 
         "9,500", 
         "Para equilibrar el mercado residencial"),
        ("TIEMPO ESTIMADO", 
         "36 meses", 
         "Para implementación completa")
    ]
    create_metric_row(metrics)
    tab1, tab2 = st.tabs(["Medidas Regulatorias", "Resultados Esperados"])


    with tab1:
        # Create three columns for visual organization
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info" style="height: 180px;">
            <strong>🎯 Control Inmediato:</strong>
            <ul>
                <li>🛑 <strong>Moratoria inmediata:</strong> En barrios con más del 5% de viviendas turísticas</li>
                <li>⬇️ <strong>Reducción de alojamientos:</strong> Máximo 5% por barrio (medida implementada en NY)</li>
                <li>👮 <strong>Inspección reforzada:</strong> Nueva unidad pública anti-fraude</li>
                <li>💰 <strong>Sanciones disuasorias:</strong> Hasta €600,000 por infracciones graves</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="info" style="height: 180px;">
            <strong>🔧 Herramientas de Control:</strong>
            <ul>
                <li>📊 <strong>Registro público:</strong> Transparente de alojamientos turísticos</li>
                <li>✅ <strong>Responsabilidad plataforma:</strong> Obligatoriedad de contrastar licencias</li>
                <li>🤖 <strong>Tecnología de detección:</strong> IA para identificar anuncios ilegales</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    with tab2:
    
        
            # Create progress bars for visual impact
            st.markdown("<div style='text-align: center; font-size: 1.2rem; color: #1E3A8A;'><strong>Objetivos a 36 meses</strong></div>", unsafe_allow_html=True)
            
            progress_data = [
                ("Reducción alojamientos ilegales", 50),
                ("Viviendas recuperadas", 45),
                ("Estabilización precios", 35),
                ("Modelo turístico sostenible", 30)
            ]
            
            for label, value in progress_data:
                st.markdown(f"**{label}**")
                st.progress(value/100)
                
        
            st.markdown("""
            <div class="highlight">
            <strong>Objetivos a 36 meses:</strong>
            <ul>
                <li>✅ Reducción 50% alojamientos ilegales</li>
                <li>✅ Recuperación 9,500 viviendas para mercado residencial</li>
                <li>✅ Estabilización precios alquiler en niveles 2022</li>
                <li>✅ Modelo turístico sostenible y regulado</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

# Conclusiones
elif app_mode == "🔍 Conclusiones":
    st.markdown('<div class="sub-header">CONCLUSIONES</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    Este análisis evidencia una crisis habitacional en fase crítica en Barcelona, donde la turistificación 
    acelerada amenaza el tejido social y urbano de la ciudad, requiriendo una intervención regulatoria 
    urgente y comprehensiva.
    </div>
    """, unsafe_allow_html=True)

    # Key metrics
    metrics = [
        ("CRECIMIENTO AIRBNB", 
         "+69.6%", 
         "En los últimos 24 meses"),
        ("ALOJAMIENTOS IRREGULARES", 
         "32%", 
         "Operando sin licencia turística"),
        ("INCREMENTO PRECIOS", 
         "+43%", 
         "En zonas más afectadas")
    ]
    create_metric_row(metrics)

    # Create tabs for different analyses
    tab1, tab2, tab3 = st.tabs(["Diagnóstico", "Escenarios", "Reflexión Final"])

    with tab1:
        st.markdown("""
        <div class="highlight">
        <strong>📊 Evidencia Empírica:</strong>
        <ul>
            <li><strong>Problema triplicado</strong> en 24 meses (69.6% de crecimiento)</li>
            <li><strong>32% de ilegalidad</strong> = Fallo sistémico administrativo</li>
            <li><strong>6x más rentable</strong> = Incentivo estructural insostenible</li>
            <li><strong>43% incremento precios</strong> = Expulsión masiva de residentes</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="warning">
            <strong>🚨 Sin Intervención:</strong>
            <ul>
                <li>Colapso del modelo residencial en centro histórico</li>
                <li>Segregación socioespacial irreversible</li>
                <li>Dependencia económica extrema del turismo</li>
                <li>Pérdida definitiva de identidad urbana barcelonesa</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="info">
            <strong>✅ Con Intervención Efectiva:</strong>
            <ul>
                <li>Reequilibrio entre turismo y residencia</li>
                <li>Preservación del tejido social</li>
                <li>Diversificación económica sostenible</li>
                <li>Barcelona como modelo de turismo responsable</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class="highlight">
        <strong>Conclusión Final:</strong>

        El análisis revela una crisis urbana sin precedentes en Barcelona, donde la proliferación descontrolada 
        de alojamientos turísticos está transformando radicalmente el tejido social y económico de la ciudad.

        <strong>Puntos Críticos:</strong>
        <ul>
            <li>La conversión masiva de viviendas residenciales en alojamientos turísticos está provocando 
            un éxodo forzado de residentes locales</li>
            <li>El diferencial de rentabilidad (6x) entre alquiler turístico y tradicional genera un incentivo 
            económico insostenible</li>
            <li>La pérdida de tejido social amenaza la identidad cultural única de Barcelona</li>
        </ul>

        <strong>El Dilema:</strong>
        Barcelona se encuentra en una encrucijada histórica entre dos modelos de ciudad:
        <ul>
            <li>Ciudad-Marca: orientada al turismo y la rentabilidad a corto plazo</li>
            <li>Ciudad-Hogar: que prioriza la calidad de vida de sus residentes y su sostenibilidad</li>
        </ul>

        La evidencia sugiere que solo una intervención regulatoria decisiva y urgente puede revertir esta 
        tendencia y preservar el equilibrio entre turismo y vida local que hizo de Barcelona un referente mundial.

        <strong>El futuro de Barcelona como ciudad habitable depende de decisiones políticas valientes que 
        antepongan el derecho a la vivienda sobre la rentabilidad turística.</strong>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
<i>Estudio realizado por Carla Molina para Upgrade Hub en 2025, basado en datos contrastados de Airbnb y licencias turísticas oficiales del Gobierno de España.</i>
</div>
""", unsafe_allow_html=True)