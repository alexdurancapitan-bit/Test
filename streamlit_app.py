import streamlit as st

# 1. EL ARCHIVADOR (Base de datos con 10 preguntas)
preguntas = [
    {
        "texto": "¿El perfume 9pm en que momento se deberia usar?",
        "opciones": ["", "a las 9pm", "clima frio", "por la mañana", "nunca"],
       index=None,
        "correcta": "clima frio"
    },
    
   {     "texto": "¿Cual es la mejor variante del one million?",
        "opciones": ["", "one million prive", "elixir", "intense", "one millon original"],
        index=None,
         "correcta": "elixir"
    },
    {
        "texto": "¿Que forma tiene la familia de invictus?",
        "opciones": ["", "trofeo", "salchicha", "lingote de oro"],
       index=None,
        "correcta": "trofeo"
    },
    {
        "texto": "¿Qué diseñador/a creo la bad boy cobalto?",
        "opciones": ["", "Carolina Herrera", "Paco Rabanne", "Antonio Banderas", "Apple"],
       index=None, 
        "correcta": "Carolina Herrera"
    },
    {
        "texto": "¿Como se llama el fundador de jean paul gaultier?",
        "opciones": ["", "jean paul gaultier", "Francis Menuge", "Paco Rabbanne"],
       index=None, 
        "correcta": "Francis Menuge"
    },
    {
        "texto": "¿Cual de estas frases indica que el perfume es muy duradero?",
        "opciones": ["", "eau de parfum", "elixir", "eau de toilet", "parfum"],
       index=None,
        "correcta": "elixir"
    },
   
{
    "texto": "¿Qué familia olfativa incluye aromas como rosa y jazmín?",
    "opciones": ["", "Amaderada", "Cítrica", "Floral", "Fougère"],
    index=None, 
    "correcta": "Floral"
},
{
    "texto": "¿Dónde se recomienda aplicar el perfume para mayor duración?",
    "opciones": ["", "En la ropa solamente", "En puntos de pulso", "En el cabello mojado", "En las manos"],
    index=None, 
    "correcta": "En puntos de pulso"
},
{
    "texto": "¿Qué nota suele aportar profundidad y duración al perfume?",
    "opciones": ["", "Nota de salida", "Nota media", "Nota de fondo", "Nota fresca"],
    index=None, 
    "correcta": "Nota de fondo"
}

]

st.title("Examen Interactivo Sobre Perfumes🎓")
st.write("Responde a las preguntas y pulsa el botón para saber tu nota.")

with st.form("quiz_form"):

    respuestas_usuario = []

    for pregunta in preguntas:
        st.subheader(pregunta["texto"])
        eleccion = st.radio(
            "Elige una opción:",
            pregunta["opciones"],
            key=pregunta["texto"]
        )
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar Examen")


# 3. CORRECCIÓN
if boton_enviar:

    aciertos = 0
    errores = 0
    total = len(preguntas)

    for i in range(total):
        if respuestas_usuario[i] == "":
            continue  # en blanco no suma ni resta
        elif respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1
        else:
            errores += 1

    # Penalización: cada error resta 0.25
    puntuacion_bruta = aciertos - (errores * 0.25)

    # Nota sobre 10 (redondeada)
    nota = round((puntuacion_bruta / total) * 10, 2)

    # Evitar nota negativa
    if nota < 0:
        nota = 0

    # Crear pestañas
    tab1, tab2 = st.tabs(["📊 Resultado", "📝 Informe detallado"])

    with tab1:
        st.header(f"Nota final: {nota} / 10")
        st.divider()

        # Feedback por tramos
        if nota < 2:
            st.error("Muy insuficiente 😢 Debes estudiar mucho más.")
            st. snow()
        elif 2 <= nota < 5:
            st. snow()
            st.error("Insuficiente 📚 Necesitas repasar.")
        elif 5 <= nota < 6:
            st.warning("Suficiente 👍 Has aprobado por poco.")
        elif 6 <= nota < 7:
            st.info("Bien 🙂 Buen trabajo.")
        elif 7 <= nota < 9:
            st.success("Notable 👏 Muy buen resultado.")
            st.balloons()
        elif 9 <= nota < 10:
            st.success("Sobresaliente 🌟 Excelente trabajo.")
            st.balloons()
        elif nota == 10:
            st.success("Excelente 🏆 ¡Examen perfecto!")
            st.balloons()

    with tab2:
        st.header("Informe en Markdown")

        informe = ""

        for i in range(total):
            informe += f"### Pregunta {i+1}\n"
            informe += f"**Enunciado:** {preguntas[i]['texto']}\n\n"
            informe += f"- Respuesta del alumno: {respuestas_usuario[i]}\n"
            informe += f"- Respuesta correcta: {preguntas[i]['correcta']}\n"

            if respuestas_usuario[i] == preguntas[i]["correcta"]:
                informe += "✅ Correcta\n\n"
            elif respuestas_usuario[i] == "":
                informe += "➖ En blanco\n\n"
            else:
                informe += "❌ Incorrecta\n\n"

        st.markdown(informe)
