# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.
from MatrizRandom import crearMatriz, imprimir

def MinMax(matriz):
    menor = []
    mayor = []
    cont = 0
    for i in matriz:
        menor.append(min(i))
        mayor.append(max(i))
    menor = min(menor)
    mayor = max(mayor)
    print(f"\nEl menor número de la lista es {menor} y el mayor número es {mayor}")

def main():
    matriz = crearMatriz(5,10)
    imprimir(matriz)
    MinMax(matriz)

if __name__ == "__main__":
    main()