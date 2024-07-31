import matplotlib.pyplot as plt
import numpy as np

# Solicitar al usuario la función matemática
func_str = input("""Ingrese la función diferencia 
                 de los lados de la ecuación 
                 en términos de x (por ejemplo, np.sin(x)): """)

# Crear el conjunto de puntos x
a,b = -10,10 # definir el dominio de graficación
x = np.arange(start = a, stop = b, step = 0.5)

try:
    # Evaluar la función ingresada por el usuario
    y = eval(func_str)

    # Graficar la función
    plt.plot(x, y, 'r--')
    plt.axhline(y = 0, xmin = a, xmax = b) 
    plt.title(f'Grafica de la función: {func_str}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error en la función ingresada: {e}")
