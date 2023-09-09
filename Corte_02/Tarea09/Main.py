# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

from Funciones.CrearMatriz import crear,crearLista,imprimir
from Funciones.stringsRecursiva import busqueda
from Funciones.MinMaxMatriz import MinMax
from MayorRecursiva import MayorRecursiva


def main():
    print("Bienvenido a la Tarea 09, para poder continuar, por favor escoja uno de los siguientes programas:\n",\
            "\n1) Organizador de matrices.\n","2) Mayor elemento en una lista.\n","3) Encontrar b en a.\n","4) Salir\n")
    opc=input("Escoja el programa que desea ejecutar: ")
    while opc.lower() != 'salir' or opc != '4':
        if opc=='1':
            crear(5,10)
            MinMax()
        elif opc=='2':
            n=int(input("Ingrese la longitud de la lista: "))
            lista=crearLista(n)
            m=MayorRecursiva(lista)
            print(f'El mayor elemento de la lista:\n{lista}\nEs {m}.')
        elif opc=='3':
            a=input('Ingrese un texto: ')
            b=input('Ingrese el elemento que desea encontrar del texto anterior: ')
            pos=busqueda(a,b)
            print(f'El elemento "{b}" del texto ingresado, se encuentra en las posiciones:\n{pos}')
        elif opc=='salir':
            break
        else:
            print('Selección Invalida')
        print("Bienvenido a la Tarea 09, para poder continuar, por favor escoja uno de los siguientes programas:\n",\
            "\n1) Organizador de matrices.\n","2) Mayor elemento en una lista.\n","3) Encontrar b en a.\n","4) Salir\n")
        opc=input("Escoja el programa que desea ejecutar: ")
        

if __name__ == "__main__":
    main()