import streamlit as st
import pandas as pd
import altair as alt

# ----- CONFIGURACIÓN DE LA PÁGINA -----
st.set_page_config(page_title="Mi CV", page_icon="💼", layout="wide")

# ----- ESTILO: Fondo negro y texto blanco -----
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: white;
    }
    .css-1d391kg, .css-1v3fvcr {
        color: white;
    }
    a {
        color: #0a66c2;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- NOMBRE CON R AZUL GRANDE -----
st.markdown(
    """
    <h1 style="font-family:sans-serif; color:white; margin-bottom: 0;">
        <span style="color:#1f77b4; font-size:70px; font-weight:bold;">R</span>UT GONZÁLEZ
    </h1>
    """,
    unsafe_allow_html=True
)

# ----- COLUMNA IZQUIERDA CON FOTO -----
col1, col2 = st.columns([1, 2])

with col1:
    st.image("rut.jpg", width=200)

with col2:
    st.markdown('<p style="font-size:20px; font-family:sans-serif;">💼 DATA ANALYST</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:18px; font-family:sans-serif;">📧 rut.18.gonzalez@gmail.com</p>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/rut-gonz%C3%A1lez-81259b165/" target="_blank">🔗 LinkedIn</a>', unsafe_allow_html=True)

# ----- BOTONES DE DESCARGA -----
st.subheader("Secciones del CV")

with st.container():
    col3, col4 = st.columns(2)

    with col3:
        with open("experiencia-profesional.pdf", "rb") as file:
            st.download_button(
                label="📄 Experiencia Profesional",
                data=file,
                file_name="experiencia-profesional.pdf",
                mime="application/pdf"
            )

        with open("Carta_Recomendacion_Rut_Gonzalez_1pagina.pdf", "rb") as file:
            st.download_button(
                label="✉️ Cartas de Recomendación",
                data=file,
                file_name="Carta_Recomendacion_Rut_Gonzalez_1pagina.pdf",
                mime="application/pdf"
            )

# ----- GRÁFICO DE NIVELES DE IDIOMA -----
st.subheader("Idiomas")

df_idiomas = pd.DataFrame({
    'Idioma': ['Inglés', 'Francés'],
    'Nivel': [4, 3]
})

base = alt.Chart(df_idiomas).encode(
    x=alt.X('Idioma', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
    y=alt.Y('Nivel', scale=alt.Scale(domain=[0,5], clamp=True), axis=alt.Axis(labelColor='white', titleColor='white', tickMinStep=1))
)

bars = base.mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3).encode(
    color=alt.condition(
        alt.datum.Nivel > 3,
        alt.value('#1f77b4'),  # azul fuerte para niveles altos
        alt.value('#6495ED')   # azul más claro para niveles bajos
    )
)

text = base.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    color='white',
    fontWeight='bold'
).encode(
    text='Nivel'
)

chart = (bars + text).properties(width=400, height=250)

st.altair_chart(chart, use_container_width=True)

# ----- SECCIÓN DIGITAL SKILLS CON LOGOS -----
st.subheader("DIGITAL SKILLS")

# Lista de imágenes con logos, cámbialos por tus rutas o URLs
logos = [
    "python_logo.png",
    "sql_logo.png",
    "powerbi_logo.png",
    "excel_logo.png"
]

cols = st.columns(len(logos))

for i, logo in enumerate(logos):
    with cols[i]:
        st.image(logo, width=60)
