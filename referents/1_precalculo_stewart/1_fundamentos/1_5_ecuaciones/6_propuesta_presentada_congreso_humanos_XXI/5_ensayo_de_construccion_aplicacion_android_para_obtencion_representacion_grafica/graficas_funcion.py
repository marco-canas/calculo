import matplotlib.pyplot as plt
import numpy as np

# Solicitar al usuario la función matemática
func_str = input("Ingrese la función matemática en términos de x (por ejemplo, np.sin(x)): ")

# Crear el conjunto de puntos x
x = np.arange(start = -10, stop = 10, step = 0.5)

try:
    # Evaluar la función ingresada por el usuario
    y = eval(func_str)

    # Graficar la función
    plt.plot(x, y, 'r--')
    plt.title(f'Grafica de la función: {func_str}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error en la función ingresada: {e}")
