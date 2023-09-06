# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.
from MatrizRandom import crearMatriz, imprimir

def MinMax(matriz):
    menor = 101
    mayor = -1
    posmin=[]
    posMax=[]
    for i in matriz:
        for j in range(len(i)):
            if min(i) == i[j] and menor >= i[j]:
                menor = i[j]
            elif max(i) == i[j] and mayor <= i[j]:
                mayor = i[j]
    for i in matriz:
        for j in range(len(i)):
            if menor==i[j]:
                posmin.append([matriz.index(i),i.index(i[j])])  
            elif mayor==i[j]:
                posMax.append([matriz.index(i),i.index(i[j])])
    print(f"\nEl menor número de la lista es {menor} en la posición {posmin} y el mayor número es {mayor} en la posición {posMax}.")

def main():
    matriz = crearMatriz(5,10)
    imprimir(matriz)
    MinMax(matriz)

if __name__ == "__main__":
    main()