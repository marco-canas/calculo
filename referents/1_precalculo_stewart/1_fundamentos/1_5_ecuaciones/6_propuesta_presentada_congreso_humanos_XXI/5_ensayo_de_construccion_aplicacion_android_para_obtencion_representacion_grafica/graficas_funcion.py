import matplotlib.pyplot as plt
import numpy as np

# Solicitar al usuario la función matemática
func_str = input("Ingrese la función matemática en términos de x (por ejemplo, np.sin(x)): ")

# Crear un rango de valores de x
x = np.linspace(-10, 10, 400)

try:
    # Evaluar la función ingresada por el usuario
    y = eval(func_str)

    # Graficar la función
    plt.plot(x, y)
    plt.title(f'Grafica de la función: {func_str}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error en la función ingresada: {e}")
