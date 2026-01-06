import random
import os
os.system("")

# ===== COLORES =====
RESET = "\033[0m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[34m"
BLANCO = "\033[37m"

# ===== ENTRADA =====
filas = int(input("Filas (impar): "))
columnas = int(input("Columnas (impar): "))

if filas % 2 == 0: filas += 1
if columnas % 2 == 0: columnas += 1

# ===== LABERINTO BASE =====
laberinto = [['#' for _ in range(columnas)] for _ in range(filas)]

# ===== DFS GENERADOR =====
def dfs_generar(x, y):
    direcciones = [(0,2),(2,0),(0,-2),(-2,0)]
    random.shuffle(direcciones)

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 1 <= nx < filas-1 and 1 <= ny < columnas-1:
            if laberinto[nx][ny] == '#':
                laberinto[x + dx//2][y + dy//2] = '.'
                laberinto[nx][ny] = '.'
                dfs_generar(nx, ny)

laberinto[1][1] = '.'
dfs_generar(1, 1)

laberinto[1][1] = 'S'
laberinto[filas-2][columnas-2] = 'E'

# ===== IMPRIMIR =====
def imprimir_laberinto(lab):
    for fila in lab:
        for celda in fila:
            if celda == '#':
                print(ROJO + "█" + RESET, end=" ")
            elif celda == 'S':
                print(VERDE + "S" + RESET, end=" ")
            elif celda == 'E':
                print(AZUL + "E" + RESET, end=" ")
            else:
                print(BLANCO + "·" + RESET, end=" ")
        print()

# ===== MOSTRAR LABERINTO =====
print("\nLaberinto generado:\n")
imprimir_laberinto(laberinto)

# ===== AGREGAR MUROS EXTRA =====
while True:
    opcion = input("\n¿Agregar muro? (enter = sí | letra = salir): ")

    if opcion.isalpha():
        break

    try:
        x = int(input("Fila: "))
        y = int(input("Columna: "))

        if laberinto[x][y] == '.':
            laberinto[x][y] = '#'
            print("\nMuro agregado:\n")
            imprimir_laberinto(laberinto)
        else:
            print("No se puede colocar un muro ahí.")

    except:
        print("Entrada inválida.")

print("\nFinalizado.")
