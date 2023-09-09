# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

from CrearMatriz import crearLista
from random import randint as r

def mayorRecursiva(l):
    if len(l)==1:
        return l[0]
    else:
        mayor = mayormayorRecursiva(l[1:])
        # La condición "l[1:]" toma la lista original pero sin el primer elemento de la lista.
        return mayor if mayor > l[0] else l[0]
        # Las condicionales se pueden escribir en la misma línea.

def main():
    lista=crearLista(r(1,10))
    print(lista)
    print(mayorRecursiva(lista))

if __name__ == "__main__":
    main()