import sympy
import matplotlib.pyplot as plt 
import  numpy as np
from numpy import *
from sympy import * 

interactive

def Costo(ancho):
    return (6*ancho + 2*(300/ancho))*3 + 4*(300/ancho)
anchos = np.arange(1, 15)
print(anchos)
costos = Costo(np.arange(1, 15))
print(Costo(np.arange(1, 15)))

import pandas as pd 

table = pd.DataFrame({'anchos':anchos, 'costos': costos })
print(table)  

plt.plot(anchos, costos)
plt.show() 
