import streamlit as st
import pandas as pd
from extractor import extraer_texto_pdf, extraer_secciones

st.set_page_config(page_title="🧠 Análisis de VAD - ML", layout="wide")
st.title("📄 Análisis de Sustentos VAD – Segunda Fase")

st.markdown("Sube **dos archivos PDF**: uno de la empresa distribuidora y otro con la respuesta del regulador.")

col1, col2 = st.columns(2)

with col1:
    archivo_empresa = st.file_uploader("📤 Archivo Empresa Distribuidora (PDF)", type="pdf")

with col2:
    archivo_regulador = st.file_uploader("📥 Archivo Respuesta Regulador (PDF)", type="pdf")

if archivo_empresa and archivo_regulador:
    texto_empresa = extraer_texto_pdf(archivo_empresa)
    texto_regulador = extraer_texto_pdf(archivo_regulador)

    secciones = extraer_secciones(texto_empresa, texto_regulador)
    df = pd.DataFrame([secciones])

    st.subheader("🔍 Secciones extraídas")
    st.dataframe(df.T, use_container_width=True)

    nombre_archivo = st.text_input("📁 Nombre del archivo de salida (sin .xlsx)", "observacion_vad")

    import io
    output = io.BytesIO()
    df.to_excel(output, index=False, engine='openpyxl')
    st.download_button(
        label="💾 Descargar Excel",
        data=output.getvalue(),
        file_name=f"{nombre_archivo}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
