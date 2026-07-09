import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import re

st.set_page_config(page_title="MathModel AI", layout="centered")

st.title("Asistente de Modelado Matemático")
st.write("Proyecto de Emprendimiento - Enfoque en Inteligencia Artificial")

st.markdown("---")

st.subheader("Análisis de Problemas Aplicados")
pregunta_usuario = st.text_input(
    "Introduzca cualquier problema matemático o caso industrial:",
    placeholder="Ej: dy/dx + P(x)y = Q(x)..."
)

if st.button("Resolver y Graficar"):
    if pregunta_usuario:
        texto = pregunta_usuario.lower()
        
        with st.spinner("Procesando variables algebraicas y ejecutando motor numérico..."):
            
            # --- MOTOR 1: ECUACIONES DIFERENCIALES LINEALES DE PRIMER ORDEN (Tu fórmula) ---
            if "dy/dx" in texto or "p(x)" in texto or "ecuacion diferencial" in texto:
                st.subheader("Resolución Analítica en Tiempo Real")
                st.write("### 1. Identificación del Modelo Matemático:")
                st.write("Se ha detectado una **Ecuación Diferencial Ordinaria (EDO) Lineal de Primer Orden** en su forma estándar:")
                st.latex(r"\frac{dy}{dx} + P(x)y = Q(x)")
                
                st.write("### 2. Planteamiento del Método de Solución:")
                st.write("Para resolver este sistema, utilizamos el método del **Factor Integrante**, denotado matemáticamente como $\mu(x)$:")
                st.latex(r"\mu(x) = e^{\int P(x) \, dx}")
                
                st.write("### 3. Desarrollo Analítico Paso a Paso:")
                st.write("**Paso A:** Multiplicamos toda la ecuación diferencial por el factor integrante hallado:")
                st.latex(r"e^{\int P(x)dx} \frac{dy}{dx} + P(x)e^{\int P(x)dx}y = Q(x)e^{\int P(x)dx}")
                
                st.write("**Paso B:** Aplicamos la regla del producto de derivadas en el miembro izquierdo de la igualdad:")
                st.latex(r"\frac{d}{dx} \left[ y \cdot e^{\int P(x)dx} \right] = Q(x)e^{\int P(x)dx}")
                
                st.write("**Paso C:** Integramos ambos lados de la ecuación respecto a la variable independiente $x$:")
                st.latex(r"y \cdot e^{\int P(x)dx} = \int \left( Q(x)e^{\int P(x)dx} \right) \, dx + C")
                
                st.write("### 4. Solución General Explícita:")
                st.write("Despejando la variable dependiente $y$, obtenemos el resultado analítico destacado:")
                st.success("La solución general del sistema está dada por:")
                st.latex(r"y(x) = e^{-\int P(x) \, dx} \left[ \int Q(x)e^{\int P(x) \, dx} \, dx + C \right]")
                
                # Gráfica Dinámica de la Familia de Soluciones (Campos de dirección simulados)
                x_vals = np.linspace(0.1, 5, 100)
                fig, ax = plt.subplots(figsize=(8, 3.5))
                # Graficar varias curvas para diferentes valores de la constante C
                for c in [-10, 0, 10, 20]:
                    y_vals = (1 / x_vals) * (5 + c)  # Simulación de curvas solución reales
                    ax.plot(x_vals, y_vals, label=f"C = {c}" if c==0 else "")
                
                ax.set_ylim(-20, 40)
                ax.set_xlabel("Variable Independiente (x)")
                ax.set_ylabel("Variable Dependiente (y)")
                ax.set_title("Familia de Curvas Solución del Sistema Diferencial")
                ax.grid(True, linestyle=":", alpha=0.6)
                st.pyplot(fig)

            # --- MOTOR 2: CANAL TRAPEZOIDAL ---
            elif "canal" in texto or "trapezoidal" in texto:
                st.subheader("Resolución Analítica en Tiempo Real")
                numeros = [float(n) for n in re.findall(r"\d+\.\d+|\d+", texto)]
                b = numeros[0] if len(numeros) > 0 else 3.0
                y_val = numeros[1] if len(numeros) > 1 else 1.5
                z = numeros[2] if len(numeros) > 2 else 1.0
                
                st.write("### 1. Datos extraídos:")
                st.write(f"- Base (b): {b} m | Tirante (y): {y_val} m | Talud (z): {z}")
                
                st.write("### 2. Ecuaciones e Integrales Geométricas:")
                st.latex(r"A = b \cdot y + z \cdot y^2 \quad \text{y} \quad P = b + 2y \sqrt{1 + z^2}")
                
                area_final = (b * y_val) + (z * (y_val ** 2))
                raiz = np.sqrt(1 + z**2)
                perimetro_final = b + (2 * y_val * raiz)
                
                st.write("### 3. Sustitución Paso a Paso:")
                st.latex(rf"A = ({b})({y_val}) + ({z})({y_val})^2 = {area_final:.2f} \text{{ m}}^2")
                st.latex(rf"P = {b} + 2({y_val})\sqrt{{1 + {z}^2}} = {perimetro_final:.2f} \text{{ m}}")
                
                st.success(f"Resultado: Área = **{area_final:.2f} m²** y Perímetro = **{perimetro_final:.2f} m**.")
                
                t = np.linspace(0, 10, 100)
                y_graf = np.ones(100) * y_val
                fig, ax = plt.subplots(figsize=(8, 3.5))
                ax.plot(t, y_graf, color="#1D3557", linewidth=3)
                ax.fill_between(t, 0, y_graf, color="#4EA8DE", alpha=0.4)
                st.pyplot(fig)

            # --- MOTOR 3: TANQUES ---
            elif "tanque" in texto or "litros" in texto:
                st.subheader("Resolución Analítica en Tiempo Real")
                numeros = [float(n) for n in re.findall(r"\d+\.\d+|\d+", texto)]
                v0 = numeros[0] if len(numeros) > 0 else 40.0
                qe = numeros[1] if len(numeros) > 1 else 25.0
                qs = numeros[2] if len(numeros) > 2 else 10.0
                tiempo = numeros[3] if len(numeros) > 3 else 15.0
                
                st.write("### 1. Balance de Masa (EDO):")
                st.latex(r"\frac{dV}{dt} = Q_e - Q_s")
                
                neto = qe - qs
                v_final = v0 + (neto * tiempo)
                
                st.write("### 2. Integración Definida Paso a Paso:")
                st.latex(rf"\int_{{{v0}}}^{{V}} dV = \int_{{0}}^{{{tiempo}}} {neto} \, dt \implies V({tiempo}) = {v_final:.2f}")
                st.success(f"Volumen final calculado: **{v_final:.2f} Litros**.")
                
                t = np.linspace(0, tiempo * 1.3, 100)
                fig, ax = plt.subplots(figsize=(8, 3.5))
                ax.plot(t, v0 + neto * t, color="#E63946")
                st.pyplot(fig)
                
            else:
                st.warning("Estructura matemática no reconocida por el motor local.")
    else:
        st.warning("Por favor, introduzca un problema.")
