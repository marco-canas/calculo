# 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact

class RepresentacionesTabularesGraficasTendencia:

    # Constructor para inicializar los valores de f, a, y b
    def __init__(self, f, a, b):
        self.f = f  # Función a utilizar
        self.a = a  # Límite inferior
        self.b = b  # Límite superior

    # Método para generar una tabla del comportamiento de la función
    def elabore_tabla(self, a=None, b=None):
        a = a if a is not None else self.a
        b = b if b is not None else self.b
        tiempos = np.arange(start=a, stop=b + 1, step=1)  # progresiones aritméticas a_0, a_n, d
        valores_futuros = self.f(tiempos)
        diccionario = {'tiempo en años': tiempos, 'Valor futuro de la inversión': valores_futuros}
        tabla = pd.DataFrame(diccionario)
        tabla.to_csv('comportamiento_valor_futuro.csv', index=False)
        tabla.to_excel('comportamiento_valor_futuro.xlsx', index=False)
        return tabla

    # Método para dibujar un diagrama de dispersión del comportamiento de la función
    def dibujar_diagrama_dispersion(self, a=None, b=None):
        a = a if a is not None else self.a
        b = b if b is not None else self.b
        paso = 1
        tiempos = np.arange(start=a, stop=b + 1, step=paso)  # progresiones aritméticas a_0, a_n, d
        valores_futuros = self.f(tiempos)
        plt.figure(figsize=(6, 4))
        plt.title('Comportamiento o tendencia del valor del dinero invertido')
        plt.xticks(np.arange(a, b + 1, step=paso))  # Escalar eje x con progresión aritmética
        plt.yticks(np.linspace(self.f(a), self.f(b), num=10))  # Escalar eje y con partición regular
        plt.xlabel('tiempo')
        plt.ylabel('Valor futuro de la inversión en millones')
        plt.grid(alpha=0.3)
        plt.scatter(tiempos, valores_futuros, color='red', label=r'Valor futuro $A(t)$', marker='^')
        plt.legend()
        plt.savefig('tendencia_de_valor_futuro.jpg')
        plt.show()

    # Método para generar un gráfico dinámico del comportamiento de la función
    def comportamiento_animado(self, a=None, b=None):
        a = a if a is not None else self.a
        b = b if b is not None else self.b
        rastrox, rastroy = [], []

        def trazar_valor_presente(t=0):
            plt.figure(figsize=(6, 4))
            plt.title('Comportamiento del valor futuro a través del tiempo')
            plt.xlabel('Tiempo')
            plt.ylabel('Valor Futuro A(t)')
            min_rango = np.min(np.array([self.f(a), self.f(b)]))
            max_rango = np.max([self.f(a), self.f(b)])
            plt.axis([a - 1, b + 1, min_rango - 2, max_rango + 1])
            plt.grid(alpha=0.3)
            plt.xticks(np.arange(a, b))
            plt.axhline(y=0, xmin=a, xmax=b)
            plt.axvline(x=0, ymin=min_rango, ymax=max_rango)
            plt.scatter(t, self.f(t), label='valor futuro', marker='^')
            rastrox.append(t)
            rastroy.append(self.f(t))
            plt.scatter(rastrox, rastroy, color='red', marker='^')
            plt.scatter(np.zeros_like(rastroy), rastroy, color='red', alpha=0.4, marker='^')
            plt.scatter(rastrox, np.zeros_like(rastrox), color='red', alpha=0.4, marker='>')

        interact(trazar_valor_presente, t=(a, b))

# Esto permite que puedas ejecutar este archivo .py como un módulo independiente si lo deseas
# o simplemente importarlo en otros scripts o cuadernos Jupyter.
if __name__ == "__main__":
    # Ejemplo de uso de la clase cuando se ejecuta este archivo directamente
    # Define la función de ejemplo (por ejemplo, una exponencial)
    def f(t):
        return 1000 * (1 + 0.05) ** t
        
# Ejemplo de uso:
# Define la función de ejemplo (por ejemplo, una exponencial)
#def f(t):
#    return 1000 * (1 + 0.05) ** t

# Crea una instancia de la clase
#representacion = RepresentacionesTabularesGraficasTendencia(f, 0, 10)

# Llama a los métodos con la opción de actualizar 'a' y 'b' si es necesario
#representacion.elabore_tabla()  # Usa los valores iniciales a=0, b=10
#representacion.elabore_tabla(a=5, b=15)  # Usa nuevos valores a=5, b=15

#representacion.dibujar_diagrama_dispersion()  # Usa los valores iniciales a=0, b=10
#representacion.dibujar_diagrama_dispersion(a=3, b=8)  # Usa nuevos valores a=3, b=8

#representacion.comportamiento_animado()  # Usa los valores iniciales a=0, b=10
#representacion.comportamiento_animado(a=1, b=12)  # Usa nuevos valores a=1, b=12
