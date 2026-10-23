import pandas as pd
import numpy as np
#Iram Jimenez NC = 0079 Fecha 23/10/2026
n_filas = 5
n_columnas = 5
tag_columna = tuple('ABCDE') #Etiquetas para la columnas de un tupla
print(tag_columna)
matriz = np.random.randint(1, 10, size = (n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendido entre 1 y 10")
print(matriz)
#La variable df es DataFrame
df = pd.DataFrame(matriz, columns = tag_columna)
print("--- La tabla o DataFrame ---  NC = 0079")
print(df)
print("---Iram Jimenez NC = 0079 Fecha 23/10/2026---")