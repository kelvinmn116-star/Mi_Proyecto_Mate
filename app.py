import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import google.generativeai as genai
from google.api_core.client_options import ClientOptions

st.set_page_config(page_title="MathModel AI", layout="centered")

# 🔑 Tu clave de Google configurada de forma correcta
API_KEY = "AQ.Ab8RN6IAD7WUcw_9FcYvaVv_DiNAihRQ4sA11CGn0goPxilyzA"

# Forzar el endpoint correcto para evitar el error 401
options = ClientOptions(api_endpoint="generativelanguage.googleapis.com")
genai.configure(api_key=API_KEY, client_options=options)

st.title("Asistente de Modelado Matemático")
st.write("Proyecto de Emprendimiento - Enfoque en Inteligencia Artificial")

st.markdown("---")

st.subheader("Análisis de Problemas Aplicados")
pregunta_usuario = st.text_input(
    "Introduzca cualquier problema matemático o caso industrial:",
    placeholder="Ej: Un canal de concreto con base 3m y tirante 1.2m..."
)

if st.button("Resolver y Graficar"):
    if pregunta_usuario:
        with st.spinner("La IA está analizando, extrayendo los datos numéricos y resolviendo el problema paso a paso..."):
            try:
                # Usamos el modelo moderno que acepta tu tipo de clave
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"""
                Eres un profesor experto en cálculo, ingeniería y ecuaciones diferenciales.
                Resuelve el problema que el usuario te dará a continuación de manera estrictamente real y matemática.
                
                IMPORTANTE: Extrae los números exactos que el usuario te dé y haz los cálculos reales paso a paso.
                Usa código LaTeX para que las fórmulas se vean perfectas ($formula$ o $$formula$$).
                
                Estructura tu respuesta así:
                1. Datos extraídos del problema.
                2. Planteamiento de las ecuaciones o integrales correspondientes.
                3. Desarrollo matemático paso a paso con los cálculos reales.
                4. Resultado final destacado en negrita.
                
                Problema a resolver: {pregunta_usuario}
                """
                
                respuesta = model.generate_content(prompt)
                
                # Desplegar la respuesta real calculada por la IA
                st.subheader("Resolución Analítica en Tiempo Real")
                st.write(respuesta.text)
                
                st.markdown("---")
                
                # Gráfica interactiva de soporte
                st.subheader("Simulación Gráfica del Comportamiento")
                factor = st.slider("Ajustar factor de escala del sistema (k)", min_value=0.5, max_value=1.5, value=1.0, step=0.1)
                
                t = np.linspace(0, 10, 100)
                if "canal" in pregunta_usuario.lower():
                    y = np.ones(100) * (1.2 * factor)
                else:
                    y = np.exp(-0.2 * factor * t) * 100
                    
                fig, ax = plt.subplots(figsize=(8, 4))
                ax.plot(t, y, color="#E63946", linewidth=2.5, label="Comportamiento del modelo")
                ax.set_xlabel("Eje X (Tiempo / Espacio)")
                ax.set_ylabel("Eje Y (Magnitud / Nivel)")
                ax.grid(True, linestyle=":", alpha=0.6)
                ax.legend()
                st.pyplot(fig)
                
            except Exception as e:
                st.error(f"Hubo un problema de conexión con la IA: {e}")
    else:
        st.warning("Por favor, introduzca un problema.")
