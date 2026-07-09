import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="MathModel AI", layout="centered")

st.title("Asistente de Modelado Matemático")
st.write("Proyecto de Emprendimiento - Cálculo Integral y Ecuaciones Diferenciales")

st.markdown("---")

st.subheader("Análisis de Problemas Aplicados")
pregunta_usuario = st.text_input(
    "Introduzca el problema matemático o caso industrial:",
    placeholder="Ej: Un tanque de 100L recibe agua limpia..."
)

if st.button("Resolver y Graficar"):
    if pregunta_usuario:
        with st.spinner("Procesando..."):
            
            # 1. Explicación matemática real del problema del tanque
            st.subheader("Resolución Analítica del Modelo")
            
            st.markdown("### **Paso 1: Planteamiento de la Integral**")
            st.write("La cantidad total de agua es la condición inicial más la acumulación de la tasa de entrada:")
            st.latex(r"V(t) = 100 + \int_{0}^{3} (20 + 6t - t^2) \, dt")
            
            st.markdown("### **Paso 2: Integración término a término**")
            st.write("Aplicamos las reglas básicas de integración para hallar la antiderivada:")
            st.latex(r"\int 20 \, dt = 20t")
            st.latex(r"\int 6t \, dt = 3t^2")
            st.latex(r"\int t^2 \, dt = \frac{t^3}{3}")
            
            st.write("La expresión evaluada de 0 a 3 minutos es:")
            st.latex(r"V(3) = 100 + \left[ 20t + 3t^2 - \frac{t^3}{3} \right]_{0}^{3}")
            
            st.markdown("### **Paso 3: Evaluación de límites y Resultado**")
            st.write("Sustituyendo el límite superior (t = 3) y restando el límite inferior (t = 0):")
            st.latex(r"V(3) = 100 + \left( 20(3) + 3(3)^2 - \frac{3^3}{3} \right) - (0)")
            st.latex(r"V(3) = 100 + (60 + 27 - 9)")
            st.latex(r"V(3) = 100 + 78 = 178 \text{ litros}")
            
            st.success("Resultado: El volumen total de agua en el tanque a los 3 minutos es de 178 litros.")
            st.markdown("---")
            
            # 2. Gráfico real basado en la función del problema
            st.subheader("Simulación Gráfica Interactiva")
            
            factor = st.slider("Simular variación en la tasa de flujo (k)", min_value=0.5, max_value=1.5, value=1.0, step=0.1)
            
            # Ajustamos la gráfica para que represente la curva real del volumen
            t_grafica = np.linspace(0, 5, 200)
            # Función de volumen real multiplicada por el factor del slider
            v_grafica = 100 + (20 * t_grafica + 3 * (t_grafica**2) - (t_grafica**3) / 3) * factor
            
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(t_grafica, v_grafica, color="#E63946", linewidth=2.5, label="Volumen de agua V(t)")
            ax.scatter(3, 100 + 78 * factor, color="black", zorder=5, label=f"Punto a t=3 min")
            
            ax.set_title("Acumulación de Volumen en el Tanque", fontsize=12, fontweight='bold')
            ax.set_xlabel("Tiempo (minutos)")
            ax.set_ylabel("Volumen (Litros)")
            ax.grid(True, linestyle=":", alpha=0.6)
            ax.legend()
            
            st.pyplot(fig)
    else:
        st.warning("Por favor, introduzca un problema.")