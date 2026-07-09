import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import google.generativeai as genai

st.set_page_config(page_title="MathModel AI", layout="centered")


API_KEY = "AQ.Ab8RN6JZjvZUY51yW5mtpQquj59WVRR5MNzBKOue7FcB2kS1oA"
genai.configure(api_key=API_KEY)

st.title("Asistente de Modelado Matemático")
st.write("Proyecto de Emprendimiento - Enfoque en Inteligencia Artificial")

st.markdown("---")

st.subheader("Análisis de Problemas Aplicados")
pregunta_usuario = st.text_input(
    "Introduzca cualquier problema matemático o caso industrial:",
    placeholder="Ej: Un tanque recibe agua a razón de..."
)

if st.button("Resolver y Graficar"):
    if pregunta_usuario:
        if API_KEY == "TU_API_KEY_AQUI":
            st.error("Por favor, coloca tu API Key de Gemini en el código.")
        else:
            with st.spinner("La IA está analizando y resolviendo el problema..."):
                try:
                    # Configurar el modelo de lenguaje de Google
                    model = genai.GenerativeModel('gemini-pro')
                    
                    # Instrucciones estrictas para que la IA responda de forma ordenada
                    prompt = f"""
                    Eres un profesor experto en cálculo y ecuaciones diferenciales. 
                    Resuelve el siguiente problema de forma detallada, clara y directa. 
                    Usa formato matemático LaTeX para las ecuaciones (ej: $$integral$$).
                    Divide tu respuesta estrictamente en:
                    1. Planteamiento de la Integral / Ecuación.
                    2. Paso a paso de la resolución analítica.
                    3. Resultado final destacado.
                    
                    Problema: {pregunta_usuario}
                    """
                    
                    respuesta = model.generate_content(prompt)
                    
                    # Mostrar la solución generada en vivo por la IA
                    st.subheader("Resolución Analítica de la IA")
                    st.write(respuesta.text)
                    
                    st.markdown("---")
                    
                    # Generar gráfica dinámica interactiva
                    st.subheader("Simulación Gráfica del Comportamiento")
                    factor = st.slider("Ajustar factor de escala del sistema (k)", min_value=0.5, max_value=1.5, value=1.0, step=0.1)
                    
                    t = np.linspace(0, 10, 100)
                    
                    # El gráfico cambia ligeramente según lo que el usuario pida
                    if "oscila" in pregunta_usuario.lower() or "onda" in pregunta_usuario.lower():
                        y = np.sin(t) * factor
                    else:
                        y = np.exp(-0.2 * factor * t) * 100
                    
                    fig, ax = plt.subplots(figsize=(8, 4))
                    ax.plot(t, y, color="#E63946", linewidth=2.5, label="Evolución temporal")
                    ax.set_xlabel("Tiempo (t)")
                    ax.set_ylabel("Magnitud (Y)")
                    ax.grid(True, linestyle=":", alpha=0.6)
                    ax.legend()
                    st.pyplot(fig)
                    
                except Exception as e:
                    st.error(f"Hubo un problema con la IA: {e}")
    else:
        st.warning("Por favor, introduzca un problema.")
