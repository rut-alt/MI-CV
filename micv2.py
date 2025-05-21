import streamlit as st

# ----- CONFIGURACIÓN DE LA PÁGINA -----
st.set_page_config(page_title="Mi CV", page_icon="💼", layout="wide")

# ----- COLUMNA IZQUIERDA CON FOTO -----
col1, col2 = st.columns([1, 2])

with col1:
    st.image("rut.jpg", width=200)

with col2:
    st.title("RUT GONZÁLEZ")
    st.write("💼 DATA ANALYST")
    st.write("📧 rut.18.gonzalez@gmail.com")

# ----- BOTONES DE DESCARGA -----
st.subheader("Secciones del CV")

with st.container():
    col3, col4 = st.columns(2)

    with col3:
        with open("experiencia-profesional.pdf", "rb") as file:
            btn = st.download_button(
                label="📄 Experiencia Profesional",
                data=file,
                file_name="experiencia-profesional.pdf",
                mime="application/pdf"
            )

        with open("portfolio_datos.pdf", "rb") as file:
            btn = st.download_button(
                label="📊 Portfolio de Datos",
                data=file,
                file_name="portfolio_datos.pdf",
                mime="application/pdf"
            )

    with col4:
        with open("portfolio_diseno.pdf", "rb") as file:
            btn = st.download_button(
                label="🎨 Portfolio de Diseño",
                data=file,
                file_name="portfolio_diseno.pdf",
                mime="application/pdf"
            )

        with open("cartas_recomendacion.pdf", "rb") as file:
            btn = st.download_button(
                label="✉️ Cartas de Recomendación",
                data=file,
                file_name="cartas_recomendacion.pdf",
                mime="application/pdf"
            )