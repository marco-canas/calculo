# El objetivo de cada recurso es que sea una función de usuario o clase de python 
# que para unos elementos datos por el usuario, le permita 
# Ya logré un recurso que se adapta para funciones constantes y funciones negativas 
#  
# recurso_teorema_valor_medio_integrales.py
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
from scipy.integrate import quad

def determine_punto_c(f, a, b):
    """
    Grafica el área bajo la curva de la función f en el intervalo [a, b] 
    y permite visualizar un punto c donde el rectángulo tiene la misma área que el  
    área bajo la curva de f en [a, b].

    Parámetros:
    f : function
        Función continua en el intervalo [a, b].
    a : float
        Límite inferior del intervalo.
    b : float
        Límite superior del intervalo.
    """
    def trazo_region_rectangular(c=a):
        plt.figure(figsize=(6, 4))
        plt.title('Trazo del rectángulo de área igual al área bajo la curva de f')
        plt.xlabel('x')
        plt.ylabel('y')

        # Trazo de la región bajo la función f
        paso = 0.01 * (b - a)
        dominio = np.arange(a, b + paso, paso)
        y = np.array([f(d) for d in dominio])
        plt.axis([a, b, 1.1 * np.min(y), 1.1 * np.max(y)])
        plt.plot(dominio, y, label="Curva de f(x)", color='blue')

        # Cálculo del área bajo la curva de f en [a, b]
        resultado, error = quad(f, a, b)
        plt.fill_between(dominio, y, color="skyblue", alpha=0.4, label=f'Área bajo f: {round(resultado, 2)}')

        # Trazo del rectángulo con área igual al área bajo la curva de f
        rectangulo_y = f(c) * np.ones_like(dominio)
        plt.fill_between(dominio, rectangulo_y, color="red", alpha=0.3, label=f'Área del rectángulo: {round(f(c) * (b - a), 2)}')

        plt.xticks(np.arange(a, b + paso, (b - a) / 5))
        plt.yticks(np.linspace(np.min(y), np.max(y), 5))
        plt.grid(alpha=0.3)
        plt.legend()
        plt.show()

    # Interactivo para el valor de c
    interact(trazo_region_rectangular, c=(a, b, 0.01))
