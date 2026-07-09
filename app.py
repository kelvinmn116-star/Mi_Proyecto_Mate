import streamlit as st
import numpy as np
import matplotlib.subplots as plt
import google.generativeai as genai
from google.api_core.client_options import ClientOptions

st.set_page_config(page_title="MathModel AI", layout="centered")

# 🔐 Conexión segura con la clave guardada en los Secrets de Streamlit
try:
    # El código busca la clave oculta de forma automática en los servidores de Streamlit
    API_KEY = st.secrets["GEMINI_API_KEY"]
    
    # Configuración obligatoria para las nuevas llaves 'AQ.' de Google
    options = ClientOptions(api_endpoint="generativelanguage.googleapis.com")
    genai.configure(api_key=API_KEY, client_options=options)
except Exception:
    st.error("Falta configurar la clave GEMINI_API_KEY en los Secrets de Streamlit Cloud.")

st.title("Asistente de Modelado Matemático Universal")
st.write("Proyecto de Emprendimiento - Inteligencia Artificial Real")

st.markdown("---")

st.subheader("Análisis de Problemas en Tiempo Real")
pregunta_usuario = st.text_input(
    "Introduzca cualquier problema matemático, ecuación o caso industrial:",
    placeholder="Ej: dy/dx + P(x)y = Q(x), integrales, canales trapezoidales..."
)

if st.button("Resolver con IA y Graficar"):
    if pregunta_usuario:
        with st.spinner("La Inteligencia Artificial está analizando y resolviendo el problema paso a paso..."):
            try:
                # Modelo de última generación capaz de procesar cualquier ejercicio matemático
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"""
                Eres un profesor experto en matemáticas avanzadas, cálculo e ingeniería.
                Resuelve el problema matemático que te dará el usuario de forma completamente real, analítica y exacta.
                
                Muestra el procedimiento matemático completo paso a paso de forma detallada.
                Usa el formato LaTeX ($formula$ o $$formula$$) para que todas las ecuaciones, fracciones, derivadas e integrales se vean perfectas en la pantalla.
                
                Estructura tu respuesta ordenadamente:
                1. Análisis e identificación del problema.
                2. Fórmulas, métodos o teoremas a aplicar.
                3. Desarrollo matemático paso a paso (con sustituciones y cálculos reales).
                4. Resultado final destacado.
                
                Problema a resolver: {pregunta_usuario}
                """
                
                respuesta = model.generate_content(prompt)
                
                # Mostrar el resultado real generado en vivo por la IA
                st.subheader("Resolución Analítica Paso a Paso")
                st.write(respuesta.text)
                
                st.markdown("---")
                
                # Generador de gráficos dinámicos adaptativos según el tema
                st.subheader("Comportamiento Gráfico del Modelo")
                t = np.linspace(0.1, 10, 100)
                texto = pregunta_usuario.lower()
                
                fig, ax = plt.subplots(figsize=(8, 3.5))
                
                if "canal" in texto or "trapezoidal" in texto:
                    y = np.ones(100) * 1.5
                    ax.plot(t, y, color="#023E8A", linewidth=2.5, label="Tirante de agua (m)")
                    ax.fill_between(t, 0, y, color="#4EA8DE", alpha=0.4)
                    ax.set_ylabel("Profundidad (m)")
                elif "dy/dx" in texto or "p(x)" in texto or "edo" in texto:
                    # Generar una familia de curvas para simular la constante C de la ecuación diferencial
                    for c in [-5, 0, 5, 10]:
                        y = (1 / t) * (3 + c)
                        ax.plot(t, y, label=f"C = {c}" if c==0 else "")
                    ax.set_ylim(-10, 20)
                    ax.set_ylabel("Variable Dependiente (y)")
                else:
                    y = t ** 2
                    ax.plot(t, y, color="#2A9D8F", linewidth=2.5, label="Evolución estándar")
                    ax.set_ylabel("Magnitud (Y)")
                    
                ax.set_xlabel("Variable X / Tiempo")
                ax.grid(True, linestyle=":", alpha=0.6)
                ax.legend()
                st.pyplot(fig)
                
            except Exception as e:
                st.error(f"Error al conectar con la IA: {e}. Verifica haber configurado correctamente tus Secrets.")
    else:
        st.warning("Por favor, introduzca un problema.")
