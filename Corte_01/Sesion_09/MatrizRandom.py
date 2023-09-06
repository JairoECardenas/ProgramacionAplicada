# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.
from random import randint as r

def crearMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num = r(0,100)
            matriz[i].append(num)
    return matriz

def imprimir(matriz):
    print("\nLa matriz es la siguiente:\n")
    for fila in matriz:
        for valor in fila:
            print(f"{valor:^4}", end=" ") # Este comando va a centrar los elementos y les dará 4 espacios de relleno.
        print() # Este print fuerza una nueva línea al salir del for.
        # Al no usar range sino poner una lista, el for conoce el tamaño y toma el valor de la lista.

def escalar(matriz):
    esc=int(input("Ingrese un escalar: "))
    for i in matriz:
        for j in range(len(i)):
            i[j]*=esc
    imprimir(matriz)

def main():
    filas=int(input("Ingrese el número de filas: "))
    columnas=int(input("Ingrese el número de columnas: "))
    m = crearMatriz(filas,columnas)
    imprimir(m)
    escalar(m)

if __name__=="__main__":
    main()