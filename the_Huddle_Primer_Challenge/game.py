from collections import deque
import random


N = int(input('filas (inpar):'))
M = int(input('columnas (inpar):'))



'''
dividiremos de esta manera mientras
    -   camino va ser igual a 0
    -   columna va ser igual a 1

'''
MAPA = [[1]*M for _ in range(N)]
MOV = [(0,1),(1,0),(0,-1),(-1,0)]


#para crear el mapa usaremos DFS

def generar_mapa()

