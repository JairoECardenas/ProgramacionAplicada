# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def main(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num = int(input(f"Ingrese el número de la posición [{i},{j}]:"))
            matriz[i].append(num)
    for i in matriz:
        print(i)
        # Al no usar range sino poner una lista, el for conoce el tamaño y toma el valor de la lista.

if __name__=="__main__":
    filas=int(input("Ingrese el número de filas: "))
    columnas=int(input("Ingrese el número de columnas: "))
    main(filas,columnas)