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

# Estructura del Mercado
elif app_mode == "🏘️ Estructura del Mercado":
    st.markdown('<div class="sub-header">Estructura del Mercado Airbnb</div>', unsafe_allow_html=True)
    
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
    

# Impacto en Precios
elif app_mode == "💰 Impacto en Precios":
    st.markdown('<div class="sub-header">2. Impacto en Precios Inmobiliarios</div>', unsafe_allow_html=True)
    
    # Section 2.1
    st.markdown('<div class="section-header">2.1 Escalada de Precios (2022-2025)</div>', unsafe_allow_html=True)
    
    if data_load_success:
        # Filter data for years 2022-2025
        df3_filtered = df3[df3['Year'] >= 2022]
        
        # Create tabs for different visualizations
        tab1, tab2 = st.tabs(["Gráfico de Evolución", "Tabla de Incrementos"])
        
        with tab1:
            # Plot with dual y-axis
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            
            # Add price per m2 line
            fig.add_trace(
                go.Scatter(
                    x=df3['Year'],
                    y=df3['Avg_Purchase_Price_EUR_m2'],
                    name="Precio de Venta (EUR/m²)",
                    line=dict(color="#2E86C1", width=3)
                ),
                secondary_y=False
            )
            
            # Add rental price line
            fig.add_trace(
                go.Scatter(
                    x=df3['Year'],
                    y=df3['Avg_Rental_Price_EUR_month'],
                    name="Precio de Alquiler (EUR/mes)",
                    line=dict(color="#E74C3C", width=3)
                ),
                secondary_y=True
            )
            
            # Calculate percentage increases
            price_2022 = df3[df3['Year'] == 2022]['Avg_Purchase_Price_EUR_m2'].values[0]
            price_2025 = df3[df3['Year'] == 2025]['Avg_Purchase_Price_EUR_m2'].values[0]
            price_increase = ((price_2025 - price_2022) / price_2022) * 100
            
            rent_2022 = df3[df3['Year'] == 2022]['Avg_Rental_Price_EUR_month'].values[0]
            rent_2025 = df3[df3['Year'] == 2025]['Avg_Rental_Price_EUR_month'].values[0]
            rent_increase = ((rent_2025 - rent_2022) / rent_2022) * 100
            
            # Add annotations
            fig.add_annotation(
                x=2023.5, 
                y=4500,
                text=f"Incremento 2022-2025: {price_increase:.1f}%",
                showarrow=False,
                bgcolor="white",
                bordercolor="gray",
                borderwidth=1
            )
            
            fig.add_annotation(
                x=2023.5, 
                y=1400,
                text=f"Incremento 2022-2025: {rent_increase:.1f}%",
                showarrow=False,
                bgcolor="white",
                bordercolor="gray",
                borderwidth=1,
                yref="y2"
            )
            
            # Update layout
            fig.update_layout(
                title="Evolución del Precio de Venta y Alquiler en Barcelona (2015-2025)",
                xaxis_title="Año",
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                )
            )
            
            # Set y-axes titles
            fig.update_yaxes(title_text="Precio Venta (EUR/m²)", secondary_y=False)
            fig.update_yaxes(title_text="Precio Alquiler (EUR/mes)", secondary_y=True)
            
            st.plotly_chart(fig, use_container_width=True)
            
        with tab2:
            # Create a table with price increases
            price_data = {
                'Mercado': ['Venta (€/m²)', 'Alquiler (€/mes)'],
                '2022': [price_2022, rent_2022],
                '2025': [price_2025, rent_2025],
                'Incremento': [f"+{price_increase:.1f}%", f"+{rent_increase:.1f}%"],
                'Velocidad': [f"{price_increase/3:.1f}% anual", f"{rent_increase/3:.1f}% anual"]
            }
            
            price_df = pd.DataFrame(price_data)
            st.dataframe(
                price_df,
                column_config={
                    "Mercado": st.column_config.TextColumn("Mercado"),
                    "2022": st.column_config.NumberColumn("2022", format="%.0f"),
                    "2025": st.column_config.NumberColumn("2025", format="%.0f"),
                    "Incremento": st.column_config.TextColumn("Incremento"),
                    "Velocidad": st.column_config.TextColumn("Velocidad")
                },
                hide_index=True,
                use_container_width=True
            )
    
    # Section 2.2
    st.markdown('<div class="section-header">2.2 Distorsión Económica Crítica</div>', unsafe_allow_html=True)
    st.markdown('<div class="subsection-header">Comparativa de Rentabilidad</div>', unsafe_allow_html=True)
    
    if data_load_success:
        # Calculate average monthly economic performance by neighborhood
        avg_performance = df.groupby('neighbourhood')['rendimiento_economico_mensual'].mean()
        
        # Remove outliers using the IQR method
        Q1 = avg_performance.quantile(0.25)
        Q3 = avg_performance.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Filter out outliers and sort values
        avg_performance_filtered = avg_performance[
            (avg_performance >= lower_bound) & 
            (avg_performance <= upper_bound)
        ].sort_values(ascending=False)
        
        # Create a horizontal bar chart
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
    
    st.markdown("""
    <div class="info">
    <strong>Comparativa de Rentabilidad:</strong><br>
    • <strong>Alquiler tradicional:</strong> 1,100-1,600 €/mes (barrios céntricos)<br>
    • <strong>Airbnb premium:</strong> Hasta 7,285 €/mes (La Dreta de l'Exemple)<br>
    • <strong>Factor multiplicador:</strong> <strong>6x más rentable</strong> que alquiler tradicional
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning">
    <strong>💰 Incentivo perverso:</strong> Esta diferencia hace económicamente irracional mantener viviendas en mercado residencial
    </div>
    """, unsafe_allow_html=True)
    
    # Section 2.3
    st.markdown('<div class="section-header">2.3 Contexto Salarial</div>', unsafe_allow_html=True)
    
    # Create columns for metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-value">€28,000</div>
            <div class="metric-label">Salario medio anual</div>
            <div>en Barcelona</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-value">>70%</div>
            <div class="metric-label">Ingresos para vivienda</div>
            <div>en zonas céntricas</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-value">6x</div>
            <div class="metric-label">Más rentable</div>
            <div>Airbnb vs. alquiler tradicional</div>
        </div>
        """, unsafe_allow_html=True)

# Geografía de la Turistificación
elif app_mode == "🗺️ Geografía de la Turistificación":
    st.markdown('<div class="sub-header">3. Geografía de la Turistificación</div>', unsafe_allow_html=True)
    
    # Section 3.1
    st.markdown('<div class="section-header">3.1 Ranking de Barrios Más Afectados</div>', unsafe_allow_html=True)
    
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
    
    st.markdown("""
    <div class="info">
    <strong>🏘️ Contexto:</strong> Más de 1 de cada 10 viviendas en el Ensanche ya no tiene uso residencial
    </div>
    """, unsafe_allow_html=True)
    
    # Section 3.2
    st.markdown('<div class="section-header">3.2 Paradoja Regulatoria</div>', unsafe_allow_html=True)
    st.markdown('<div class="subsection-header">Cumplimiento Legal por Zona</div>', unsafe_allow_html=True)
    
    if data_load_success:
        # Calculate the percentage of unlicensed accommodations by neighborhood
        unlicensed_by_neighborhood = df[df['license'] == 'sin datos'].groupby('neighbourhood').size()
        total_by_neighborhood = df.groupby('neighbourhood').size()
        percentage_unlicensed = (unlicensed_by_neighborhood / total_by_neighborhood * 100)
        
        # Get data for specific neighborhoods mentioned in the report
        specific_neighborhoods = ['la Dreta de l\'Eixample', 'el Raval', 'Vallvidrera, el Tibidabo i les Planes', 'la Font d\'en Fargues']
        specific_data = percentage_unlicensed.loc[specific_neighborhoods].sort_values(ascending=True)
        
        # Create a horizontal bar chart
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
        
    st.markdown("""
    <div class="highlight">
    <strong>🎯 Interpretación:</strong> Regulación de "dos velocidades" - más estricta en zonas visibles, más laxa en periferia:
    <ul>
        <li><strong>Zonas turísticas céntricas:</strong> Mejor cumplimiento (22.9% sin licencia en La Dreta de l'Exemple)</li>
        <li><strong>Zonas periféricas:</strong> Peor cumplimiento (66.7% sin licencia en Vallvidrera)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Crisis Regulatoria
elif app_mode == "⚖️ Crisis Regulatoria":
    st.markdown('<div class="sub-header">4. Crisis Regulatoria</div>', unsafe_allow_html=True)
    
    # Section 4.1
    st.markdown('<div class="section-header">4.1 Dimensión del Incumplimiento Legal</div>', unsafe_allow_html=True)
    st.markdown('<div class="subsection-header">Cifras Generales</div>', unsafe_allow_html=True)
    
    if data_load_success:
        # Count unlicensed accommodations
        unlicensed_count = len(df[df['license'] == 'sin datos'])
        total_count = len(df)
        unlicensed_percentage = (unlicensed_count / total_count) * 100
        
        # Display metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-value">6,222</div>
                <div class="metric-label">Alojamientos ilegales</div>
                <div>sin licencia turística</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-value">{unlicensed_percentage:.2f}%</div>
                <div class="metric-label">Porcentaje sin licencia</div>
                <div>del total de alojamientos</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-value">1 de cada 3</div>
                <div class="metric-label">Alojamientos</div>
                <div>opera al margen de la ley</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<div class="subsection-header">Incumplimiento por Tipo de Gestor</div>', unsafe_allow_html=True)
    
    if data_load_success:
        # Calculate percentages of unlicensed properties by host type
        unlicensed_particulares = df[(df['license'] == 'sin datos') & (df['tipo_anfitrion'] == 'particular')]
        total_particulares = df[df['tipo_anfitrion'] == 'particular']
        
        unlicensed_empresas = df[(df['license'] == 'sin datos') & (df['tipo_anfitrion'] == 'empresa')]
        total_empresas = df[df['tipo_anfitrion'] == 'empresa']
        
        # Calculate percentages
        part_count = len(total_particulares)
        unlicensed_part_count = len(unlicensed_particulares)
        licensed_part_count = part_count - unlicensed_part_count
        part_unlicensed_percentage = (unlicensed_part_count / part_count) * 100
        
        emp_count = len(total_empresas)
        unlicensed_emp_count = len(unlicensed_empresas)
        licensed_emp_count = emp_count - unlicensed_emp_count
        emp_unlicensed_percentage = (unlicensed_emp_count / emp_count) * 100
        
        # Create tabs for different visualizations
        tab1, tab2 = st.tabs(["Gráficos", "Tabla Comparativa"])
        
        with tab1:
            # Create two columns for pie charts
            col1, col2 = st.columns(2)
            
            with col1:
                # Pie chart for particulares
                part_fig = px.pie(
                    values=[licensed_part_count, unlicensed_part_count],
                    names=['Con Licencia', 'Sin Licencia'],
                    title="Distribución de Licencias en Alojamientos de Particulares",
                    color_discrete_sequence=['#66B2FF', '#FF9999'],
                    hole=0.4
                )
                part_fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(part_fig, use_container_width=True)
                
            with col2:
                # Pie chart for empresas
                emp_fig = px.pie(
                    values=[licensed_emp_count, unlicensed_emp_count],
                    names=['Con Licencia', 'Sin Licencia'],
                    title="Distribución de Licencias en Alojamientos de Empresas",
                    color_discrete_sequence=['#66B2FF', '#FF9999'],
                    hole=0.4
                )
                emp_fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(emp_fig, use_container_width=True)
        
        with tab2:
            # Create a table comparing both types
            comparison_data = {
                'Tipo': ['Particulares', 'Empresas', 'Diferencia'],
                '% Sin Licencia': [f"{part_unlicensed_percentage:.1f}%", 
                                  f"{emp_unlicensed_percentage:.1f}%", 
                                  f"{part_unlicensed_percentage - emp_unlicensed_percentage:.1f}%"],
                'Interpretación': ['Informalidad inherente al modelo', 
                                   'Mejor cultura de cumplimiento',
                                   'Los particulares incumplen 3 veces más']
            }
            
            comparison_df = pd.DataFrame(comparison_data)
            st.dataframe(
                comparison_df,
                column_config={
                    "Tipo": st.column_config.TextColumn("Tipo de Gestor"),
                    "% Sin Licencia": st.column_config.TextColumn("% Sin Licencia"),
                    "Interpretación": st.column_config.TextColumn("Interpretación")
                },
                hide_index=True,
                use_container_width=True
            )
    
    # Section 4.2
    st.markdown('<div class="section-header">4.2 Mapa de la Ilegalidad</div>', unsafe_allow_html=True)
    st.markdown('<div class="subsection-header">Barrios con Mayor Irregularidad</div>', unsafe_allow_html=True)
    
    if data_load_success:
        # Calculate the percentage of unlicensed accommodations by neighborhood
        unlicensed_by_neighborhood = df[df['license'] == 'sin datos'].groupby('neighbourhood').size()
        total_by_neighborhood = df.groupby('neighbourhood').size()
        percentage_unlicensed = (unlicensed_by_neighborhood / total_by_neighborhood * 100).sort_values(ascending=False)
        
        # Get top 10 neighborhoods with highest percentage of unlicensed accommodations
        top_unlicensed = percentage_unlicensed.head(10)
        
        # Create a horizontal bar chart
        fig = px.bar(
            x=top_unlicensed.values,
            y=top_unlicensed.index,
            labels={"x": "Porcentaje Sin Licencia (%)", "y": "Barrio"},
            title="Top 10 Barrios con Mayor Porcentaje de Alojamientos Sin Licencia",
            orientation='h',
            color=top_unlicensed.values,
            color_continuous_scale='Reds',
            text=[f"{x:.1f}%" for x in top_unlicensed.values]
        )
        
        fig.update_traces(textposition='outside')
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="info">
    <strong>🔍 Patrón:</strong> Periferia descontrolada vs. centro más regulado
    </div>
    """, unsafe_allow_html=True)

# Implicaciones Socioeconómicas
elif app_mode == "👥 Implicaciones Socioeconómicas":
    st.markdown('<div class="sub-header">5. Implicaciones Socioeconómicas</div>', unsafe_allow_html=True)
    
    # Section 5.1
    st.markdown('<div class="section-header">5.1 Gentrificación Acelerada</div>', unsafe_allow_html=True)
    st.markdown('<div class="subsection-header">Mecanismo de Expulsión</div>', unsafe_allow_html=True)
    
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
    
    st.markdown('<div class="subsection-header">Impacto en Comunidades Locales</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
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
    
    with col2:
        st.image("https://images.unsplash.com/photo-1557094005-176cbfe3554d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", 
                 caption="Barrio transformado por turistificación", use_column_width=True)
    
    # Section 5.2
    st.markdown('<div class="section-header">5.2 Crisis de Accesibilidad Habitacional</div>', unsafe_allow_html=True)
    st.markdown('<div class="subsection-header">Realidad Económica</div>', unsafe_allow_html=True)
    
    # Create metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-value">€28,000</div>
            <div class="metric-label">Salario medio anual</div>
            <div>en Barcelona</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-value">>70%</div>
            <div class="metric-label">Ingresos para alquiler</div>
            <div>en zonas céntricas</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-value">Expulsión</div>
            <div class="metric-label">Consecuencia</div>
            <div>de jóvenes hacia periferia</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="subsection-header">Segregación Socioespacial</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info">
    <strong>Segregación Socioespacial:</strong>
    <ul>
        <li><strong>Centro:</strong> Turistificación + población flotante</li>
        <li><strong>Periferia:</strong> Concentración de población con menor poder adquisitivo</li>
        <li><strong>Resultado:</strong> Barcelona de "dos velocidades"</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Section 5.3
    st.markdown('<div class="section-header">5.3 Distorsión del Mercado Laboral</div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Precarización Laboral", "Impacto en Sectores Productivos"])
    
    with tab1:
        st.markdown("""
        <div class="highlight">
        <strong>Precarización Laboral:</strong>
        <ul>
            <li>↗️ Trabajos estacionales y baja cualificación</li>
            <li>↘️ Empleos estables en sectores tradicionales</li>
            <li>⚠️ Dependencia económica excesiva del turismo</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.markdown("""
        <div class="highlight">
        <strong>Impacto en Sectores Productivos:</strong>
        <ul>
            <li>🧠 Dificultad para retener talento (altos costes residenciales)</li>
            <li>🏭 Desplazamiento de actividad económica no turística</li>
            <li>📉 Pérdida de diversificación económica</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Section 5.4
    st.markdown('<div class="section-header">5.4 Riesgo de Burbuja Especulativa</div>', unsafe_allow_html=True)
    
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

# Recomendaciones
elif app_mode == "📝 Recomendaciones":
    st.markdown('<div class="sub-header">6. Recomendaciones Estratégicas</div>', unsafe_allow_html=True)
    
    # Section 6.1
    st.markdown('<div class="section-header">6.1 Medidas Regulatorias Inmediatas</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
    <strong>Control de Oferta y Moratoria:</strong>
    <ul>
        <li><strong>Moratoria total</strong> en nuevas licencias turísticas en barrios con más del 5% de viviendas turistificadas</li>
        <li><strong>Límite máximo del 5%</strong> de viviendas turísticas por barrio en toda la ciudad (medida utilizada en ciudades como Nueva York)</li>
        <li><strong>Reducción progresiva</strong> del 20% anual en barrios que superen el límite hasta alcanzar el objetivo</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
    <strong>Refuerzo del Control y Sanciones:</strong>
    <ul>
        <li><strong>Incremento de sanciones:</strong> Multas para alojamientos ilegales</li>
        <li><strong>Unidad especial de inspección:</strong> Inspectores dedicados exclusivamente al control turístico</li>
        <li><strong>Tecnología de detección:</strong> Sistema de inteligencia artificial para identificar anuncios ilegales</li>
        <li><strong>Responsabilidad de plataformas:</strong> Airbnb debe verificar licencias antes de publicar anuncios</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Section 6.2
    st.markdown('<div class="section-header">6.2 Medidas Fiscales Redistributivas</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info">
    <strong>Incentivos para Alquiler Residencial:</strong>
    <ul>
        <li><strong>Bonificación fiscal del 30%</strong> para propietarios que conviertan alojamientos turísticos en residenciales</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Section 6.3
    st.markdown('<div class="section-header">6.3 Diversificación Económica</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info">
    <strong>Promoción de Sectores Alternativos:</strong>
    <ul>
        <li><strong>Incentivos fiscales</strong> para empresas no turísticas que se instalen en zonas turistificadas</li>
        <li><strong>Espacios de coworking municipales</strong> para atraer talento tecnológico y creativo</li>
        <li><strong>Apoyo al comercio local</strong> con bonificaciones fiscales y programas de mentorización</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Section 6.4
    st.markdown('<div class="section-header">6.4 Participación Ciudadana y Transparencia</div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Gobernanza Participativa", "Transparencia y Datos Abiertos"])
    
    with tab1:
        st.markdown("""
        <div class="highlight">
        <strong>Gobernanza Participativa:</strong>
        <ul>
            <li><strong>Consejos de barrio</strong> con poder decisorio sobre nuevas licencias turísticas</li>
            <li><strong>Consultas ciudadanas vinculantes</strong> para cambios normativos significativos</li>
            <li><strong>Observatorio del turismo</strong> con participación vecinal y académica</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.markdown("""
        <div class="highlight">
        <strong>Transparencia y Datos Abiertos:</strong>
        <ul>
            <li><strong>Portal público de datos</strong> con información actualizada sobre licencias y precios</li>
            <li><strong>Informes trimestrales</strong> sobre impacto del turismo en cada barrio</li>
            <li><strong>Indicadores de alerta temprana</strong> para prevenir procesos de turistificación</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# Conclusiones
elif app_mode == "🔍 Conclusiones":
    st.markdown('<div class="sub-header">7. Conclusiones</div>', unsafe_allow_html=True)
    
    # Section 7.1
    st.markdown('<div class="section-header">Diagnóstico: Crisis Habitacional en Fase Crítica</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning">
    Barcelona se encuentra en un <strong>punto de inflexión crítico</strong>. Los datos revelan:
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Urgencia Temporal", "Evidencia Empírica", "Naturaleza del Problema"])
    
    with tab1:
        st.markdown("""
        <div class="highlight">
        <strong>🔥 Urgencia Temporal:</strong>
        <ul>
            <li><strong>Problema triplicado</strong> en 24 meses (69.6% de crecimiento)</li>
            <li><strong>Ventana de oportunidad</strong> cerrándose rápidamente</li>
            <li><strong>Coste de inacción</strong> exponencialmente mayor que coste de acción</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.markdown("""
        <div class="highlight">
        <strong>📊 Evidencia Empírica:</strong>
        <ul>
            <li><strong>32% de ilegalidad</strong> = Fallo sistémico administrativo</li>
            <li><strong>6x más rentable</strong> = Incentivo estructural insostenible</li>
            <li><strong>43% incremento precios</strong> = Expulsión masiva de residentes</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab3:
        st.markdown("""
        <div class="highlight">
        <strong>⚖️ Naturaleza del Problema:</strong>
        <ul>
            <li><strong>No es efecto colateral</strong> de actividad económica legítima</li>
            <li><strong>Es consecuencia directa</strong> de modelo que prioriza rentabilidad turística sobre derecho a vivienda</li>
            <li><strong>Requiere intervención regulatoria</strong> urgente y comprehensiva</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Section 7.2
    st.markdown('<div class="section-header">Escenarios Futuros</div>', unsafe_allow_html=True)
    
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
    
    # Section 7.3
    st.markdown('<div class="section-header">Reflexión Final</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
    El éxito de cualquier estrategia dependerá de la <strong>capacidad política</strong> para equilibrar beneficios económicos del turismo con el <strong>derecho fundamental a la vivienda</strong>.
    
    No estamos ante un problema técnico sino ante una <strong>decisión política</strong>: ¿Qué modelo de ciudad queremos? ¿Barcelona para barceloneses o Barcelona para turistas?
    
    <strong>La respuesta a esta pregunta determinará el futuro de la ciudad para las próximas décadas.</strong>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
<i>Estudio realizado por Carla Molina para Upgrade Hub en 2025, basado en datos contrastados de Airbnb y licencias turísticas oficiales del Gobierno de España.</i>
</div>
""", unsafe_allow_html=True)