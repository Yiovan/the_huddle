import random
import os
import sys

# Aumentar límite de recursión para mapas grandes
sys.setrecursionlimit(5000)
os.system('cls' if os.name == 'nt' else 'clear')

# ===== COLORES =====
RESET = "\033[0m"
ROJO = "\033[31m"    # Muros
VERDE = "\033[32m"   # Inicio
AZUL = "\033[34m"    # Fin
BLANCO = "\033[37m"  # Pasillos
AMARILLO = "\033[33m" # Ruta

# ===== CONFIGURACIÓN DINÁMICA =====
print(f"{AMARILLO}--- THE HUDDLE: GENERADOR Y CALCULADORA ---{RESET}")
filas = int(input("Filas (impar): "))
columnas = int(input("Columnas (impar): "))

# El README pide que el mapa sea configurable
if filas % 2 == 0: filas += 1
if columnas % 2 == 0: columnas += 1

# Inicializamos el mapa lleno de muros (1/Edificio según el reto)
laberinto = [['#' for _ in range(columnas)] for _ in range(filas)]

# ===== 1. DFS GENERADOR (Crea el laberinto no vacío) =====
def dfs_generar(x, y):
    direcciones = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(direcciones)

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 1 <= nx < filas-1 and 1 <= ny < columnas-1:
            if laberinto[nx][ny] == '#':
                # "Tallamos" el camino (0/Libre según el reto)
                laberinto[x + dx//2][y + dy//2] = '.'
                laberinto[nx][ny] = '.'
                dfs_generar(nx, ny)

# Ejecutamos la generación desde el punto de inicio
laberinto[1][1] = '.'
dfs_generar(1, 1)

# Definimos puntos S y E
inicio = (1, 1)
fin = (filas - 2, columnas - 2)
laberinto[inicio[0]][inicio[1]] = 'S'
laberinto[fin[0]][fin[1]] = 'E'

# ===== 2. DFS DE BÚSQUEDA (Encuentra la ruta en el laberinto generado) =====
def buscar_ruta(x, y, visitados):
    if (x, y) == fin:
        return [(x, y)]
    
    visitados.add((x, y))
    
    # Movimientos simples: arriba, abajo, izquierda, derecha
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < filas and 0 <= ny < columnas:
            # Solo pasamos por donde no hay muros '#'
            if laberinto[nx][ny] != '#' and (nx, ny) not in visitados:
                resultado = buscar_ruta(nx, ny, visitados)
                if resultado:
                    return [(x, y)] + resultado
    return None

# ===== 3. VISUALIZACIÓN EN CONSOLA =====
def imprimir(lab, ruta=[]):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{AMARILLO}Ruta calculada con DFS:{RESET}\n")
    for r in range(len(lab)):
        for c in range(len(lab[0])):
            pos = (r, c)
            if pos == inicio:
                print(f"{VERDE}S{RESET}", end=" ")
            elif pos == fin:
                print(f"{AZUL}E{RESET}", end=" ")
            elif ruta and pos in ruta:
                print(f"{AMARILLO}*{RESET}", end=" ")
            elif lab[r][c] == '#':
                print(f"{ROJO}█{RESET}", end=" ")
            else:
                print(f"{BLANCO}·{RESET}", end=" ")
        print()

# ===== FLUJO FINAL =====
# Buscamos la ruta justo después de generar el laberinto
ruta_encontrada = buscar_ruta(inicio[0], inicio[1], set())
imprimir(laberinto, ruta_encontrada)

print(f"\n{VERDE}¡Mapa listo!{RESET} Se ha generado un laberinto y se ha trazado la ruta con {AMARILLO}*{RESET}.")

# Opción de agregar obstáculos extra como pide el README
while True:
    opcion = input("\n¿Añadir obstáculo manual? (Enter para sí / 'q' para salir): ")
    if opcion.lower() == 'q': break
    
    try:
        f = int(input("Fila: "))
        c = int(input("Columna: "))
        if laberinto[f][c] in ['.']:
            laberinto[f][c] = '#'
            nueva_ruta = buscar_ruta(inicio[0], inicio[1], set())
            imprimir(laberinto, nueva_ruta)
        else:
            print("No se puede colocar ahí.")
    except:
        print("Coordenada fuera de rango.")