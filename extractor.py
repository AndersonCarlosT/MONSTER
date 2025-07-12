import PyPDF2

def extraer_texto_pdf(archivo):
    texto = ""
    pdf = PyPDF2.PdfReader(archivo)
    for pagina in pdf.pages:
        texto += pagina.extract_text()
    return texto.upper()

def extraer_secciones(texto_empresa, texto_regulador):
    def extraer_entre(texto, ini, fin):
        start = texto.find(ini)
        if start == -1:
            return ""
        end = texto.find(fin, start + len(ini)) if fin else len(texto)
        return texto[start + len(ini):end].strip()

    secciones = {
        "observacion": "",
        "sustento_empresa": "",
        "solicitud": "",
        "analisis_regulador": "",
        "sustento_regulador": "",
        "resultado": ""
    }

    # Empresa distribuidora
    secciones["observacion"] = extraer_entre(texto_empresa, "OBSERVACIÓN", "SUSTENTO")
    secciones["sustento_empresa"] = extraer_entre(texto_empresa, "SUSTENTO", "SOLICITUD")
    secciones["solicitud"] = extraer_entre(texto_empresa, "SOLICITUD", "")

    # Regulador
    secciones["analisis_regulador"] = extraer_entre(texto_regulador, "ANALISIS", "SUSTENTO")
    secciones["sustento_regulador"] = extraer_entre(texto_regulador, "SUSTENTO", "RESULTADO")
    resultado = texto_regulador.split("RESULTADO")[-1].strip()
    secciones["resultado"] = resultado.split("\n")[0].strip()

    return secciones
