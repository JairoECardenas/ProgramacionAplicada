# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

from DosPuntosOMenos import *
from TresPuntosOMas import *

def imprimir():
    f=open("Menu.txt","rt", encoding='utf-8')
    menu=f.readlines()
    f.close
    for i in menu:
        print(i.strip('\n'))

def importarDatos():
    f=open("wcm.csv","r",encoding='utf8')
    baseDatos=f.readlines()
    f.close
    lista=[]
    for i in baseDatos[1:]:
        lista.append(i.strip('\n').split(','))
    return lista

def main():
    while True:
        imprimir()
        datos=importarDatos()
        menu={'1':campeon_mundial, '2':subcampeon_mundial,'3':participaciones_mundial,
            '11':numero_enfrentamientos,'14':mayores_goleadas}
        opcion=input('Opción: ')
        if opcion.lower() == 'salir':
            break
        elif opcion in menu:
            menu[opcion](datos)
        else:
            print('Selección inválida, vuelva a intentar')

if __name__=="__main__":
    main()