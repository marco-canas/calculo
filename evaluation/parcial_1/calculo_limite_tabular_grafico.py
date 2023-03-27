import numpy as np 
import pandas as pd 

    

def tabla_izquierda(f, c = 0):
    epsilon = 0.001
    X = np.linspace(c-1, c-epsilon, 10)
    Y = f(X)
    tabla_izq = pd.DataFrame({'x':X, 'y':Y})
    return tabla_izq


def tabla_derecha(f, c = 0):
    epsilon = 0.001
    X = np.linspace(c+epsilon, c+1-epsilon, 10)
    Y = f(X)
    tabla_der = pd.DataFrame({'x':X, 'y':Y})
    return tabla_der


def trazar_flecha(punto_inicial = [0,0], delta_x = 3, delta_y = 4, **opcions):
    return plt.arrow()

def plot_tendencia_funcion(c = 2):
    punto_final_flechas = [c, f(c)]
    epsilon = 0.000001
    derivada_en_c = (f(c+epsilon) - f(c-epsilon))/(2*epsilon)
    # flecha superior
    plt.arrow(c + 1.2,c + 6.4, -1, -derivada_en_c, head_width=0.1)
    
    # flecha inferior
    plt.arrow(c-1, c-2, 1, derivada_en_c, head_width=0.1) 
    #plt.arrow()
plot_tendencia_funcion()