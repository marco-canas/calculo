# Primer recurso para la solución de ecuaciones con python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class FuncionDiferenciaLadosEcuacion:
    def __init__(self, f, a, b):
        """
        Inicializa la clase con la función lambda f y los extremos del dominio a y b.
        """
        self.f = f
        self.a = a
        self.b = b
    
    def crear_tabla_de_la_funcion(self):
        """
        Crea una tabla con los puntos del dominio de la función y sus valores correspondientes.
        """
        paso = 1
        puntos_dominio = np.arange(self.a, self.b + paso, paso)  # Crea una progresión aritmética de puntos del dominio
        valores_funcion = self.f(puntos_dominio)  # Evalúa la función en esos puntos
        
        # Crear DataFrame
        diccionario = {'numeros x': puntos_dominio, r'valores $y$ o $f(x)$': valores_funcion}
        return pd.DataFrame(diccionario)

    def crear_grafico_funcion_diferencia(self):
        """
        Crea un gráfico de la función diferencia de los lados de la ecuación.
        """
        # Configuración básica del gráfico
        plt.figure(figsize=(6, 4))
        plt.title('Función diferencia de los lados de la ecuación a resolver')
        plt.xlabel('Puntos x')
        plt.ylabel('Valores y o f(x)')
        plt.grid(alpha=0.3)
        
        # Obtener los datos de la tabla de la función
        df = self.crear_tabla_de_la_funcion()
        
        # Graficar los datos
        plt.plot(df.iloc[:, 0].values, df.iloc[:, 1].values, color='red', label=r'$f(x)$')  # Graficar los puntos
        plt.axhline(y=0, xmin=self.a, xmax=self.b, color='green', linestyle='--', label='y = 0')  # Línea horizontal en y=0
        
        # Añadir leyenda y mostrar gráfico
        plt.legend()
        plt.show()

# Ejemplo de uso:
f = lambda x: 2 * x - x**2  # Función ejemplo
a = -4
b = 4

# Crear una instancia de la clase
funcion = FuncionDiferenciaLadosEcuacion(f, a, b)

# Crear la tabla y mostrarla
tabla = funcion.crear_tabla_de_la_funcion()
print(tabla)

# Crear el gráfico
funcion.crear_grafico_funcion_diferencia()
