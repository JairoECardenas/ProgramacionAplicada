# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

from random import randint as r

def crear(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num = r(0,100)
            matriz[i].append(num)
    return matriz

def crearLista(columnas):
    lista = []
    for i in range(columnas):
        lista.append(r(0,100))
    return lista

def imprimir(matriz):
    for fila in matriz:
        for valor in fila:
            print(f"{valor:^4}", end=" ") # Este comando va a centrar los elementos y les dará 4 espacios de relleno.
        print() # Este print fuerza una nueva línea al salir del for.
        # Al no usar range sino poner una lista, el for conoce el tamaño y toma el valor de la lista.

def main():
    filas=int(input("Ingrese el número de filas: "))
    columnas=int(input("Ingrese el número de columnas: "))
    m = crear(filas,columnas)
    imprimir(m)

if __name__=="__main__":
    main()