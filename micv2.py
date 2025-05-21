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

        with open("Carta_Recomendacion_Rut_Gonzalez_1pagina.pdf", "rb") as file:
            btn = st.download_button(
                label="✉️ Cartas de Recomendación",
                data=file,
                file_name="Carta_Recomendacion_Rut_Gonzalez_1pagina.pdf",
                mime="application/pdf"
            )