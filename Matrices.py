import random

# Ejercicio 1: Crear una matriz 3D e imprimirla
def crear_e_imprimir_matriz_3d():
    matriz = [[[i * 12 + j * 4 + k + 1 for k in range(4)] for j in range(3)] for i in range(2)]
    for capa in matriz:
        for fila in capa:
            print(fila)
        print()
crear_e_imprimir_matriz_3d()