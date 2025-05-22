import streamlit as st

# ----- CONFIGURACIÓN DE LA PÁGINA -----
st.set_page_config(page_title="Mi CV", page_icon="💼", layout="wide")

# ----- ESTILO: Fondo tipo Power BI y estilos de texto -----
st.markdown(
    """
    <style>
    /* Fondo con imagen */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1470&q=80');
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        color: white;
    }

    /* Caja para foto con borde y sombra */
    .foto-container {
        border: 3px solid #0078D4;
        border-radius: 10px;
        padding: 5px;
        box-shadow: 2px 2px 10px rgba(0,120,212,0.7);
        width: fit-content;
        margin-bottom: 15px;
    }

    /* Enlaces de LinkedIn estilo botón */
    .linkedin-link {
        display: inline-block;
        margin-top: 8px;
        font-weight: 600;
        color: #0A66C2;
        text-decoration: none;
        border: 2px solid #0A66C2;
        padding: 5px 10px;
        border-radius: 5px;
        transition: background-color 0.3s, color 0.3s;
    }
    .linkedin-link:hover {
        background-color: #0A66C2;
        color: white;
        text-decoration: none;
    }

    /* Texto "DATA ANALYST" y email más sencillo y más grande */
    .simple-large-text {
        font-family: Arial, Helvetica, sans-serif;
        font-size: 20px;  /* Tamaño más grande */
        font-weight: normal;
        margin-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- COLUMNA IZQUIERDA CON FOTO -----
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="foto-container">', unsafe_allow_html=True)
    st.image("rut.jpg", width=200)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.title("RUT GONZÁLEZ")
    st.markdown('<div class="simple-large-text">💼 DATA ANALYST</div>', unsafe_allow_html=True)
    st.markdown('<div class="simple-large-text">📧 rut.18.gonzalez@gmail.com</div>', unsafe_allow_html=True)
    linkedin_url = "https://www.linkedin.com/in/rut-gonz%C3%A1lez-81259b165/"
    st.markdown(
        f'<a href="{linkedin_url}" target="_blank" class="linkedin-link">🔗 LinkedIn</a>',
        unsafe_allow_html=True
    )

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

