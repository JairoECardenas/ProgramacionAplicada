# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

from CrearMatriz import crear, imprimir

def MinMax(matriz):
    print("La matriz es la siguiente:")
    imprimir(matriz)
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
    print(f"\nEl menor número de la lista es {menor} en la posición {','.join(str(i) for i in posmin)} y",\
        f"el mayor número es {mayor} en la posición {','.join(str(i) for i in posMax)}.")
    lista=[]
    for i in matriz:
        for j in range(len(i)):
            lista.append(i[j])
    lista.sort(reverse=True)
    cont=0
    for i in matriz:
        for j in range(len(i)):
            a=matriz.index(i)
            b=i.index(i[j])
            matriz[a][b] = lista[cont]
            cont+=1
    print("\nLa matriz ordenada de mayor a menor es:")
    imprimir(matriz)

def main():
    matriz = crear(5,10)
    MinMax(matriz)

if __name__ == "__main__":
    main()