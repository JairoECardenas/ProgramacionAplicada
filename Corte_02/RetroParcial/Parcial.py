# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

from random import uniform as u

def rates():
    comision=[]
    for i in range(5):
        comision.append(round(u(0.1,0.5),2))
    return comision

def ver_tasas(d,c,r):
    for i in range(5):
        print(f"Divisa: {d[i]}, Tasa: {c[i]}, Comisión:{r[i]}")

def conversion(r,d,c):
    divisa=input("A que divisa desea hacer el cambio: ").upper()
    if divisa in d:
        idx=d.index(divisa)
        divisa=d[idx]
        tasa=int(c[idx])
        comision=r[idx]
        Precio_venta=tasa+(tasa*comision)
        cambio=int(input("Que valor desea cambiar: "))
        total = cambio//Precio_venta
        vueltas = round((cambio - Precio_venta*total),2)
        print(f"Cambio: {total} {divisa}, Devolución: {vueltas} COP")
        return 1
    print("Ingrese un valor valido.")

def menu():
    comision=rates()
    divisas=['USD','EUR','CNY','JPY','PEN']
    cambio=[4108,4454,563,28,1106]
    print('Selecciones una de las siguientes opciones\n',\
        '1. Cambio de divisa.\n','2. Ver tasas de cambio.\n','3. Salir.\n')
    opc=input('Seleccione una opción: ')

    while opc!='salir':
        if opc=="1":
            conversion(comision,divisas,cambio)
        elif opc=="2":
            ver_tasas(divisas,cambio,comision)
        elif opc=="salir" or "3":
            break
        else:
            print("Selección Invalida")
        print('\nSelecciones una de las siguientes opciones\n',\
        '1. Cambio de divisa.\n','2. Ver tasas de cambio.\n','3. Salir.\n')
        opc=input("\nSeleccione una opción: ")

def inicio():
    comision=rates()
    divisas=['USD','EUR','CNY','JPY','PEN']
    cambio=[4108,4454,563,28,1106]
    menu()

if __name__ == "__main__":
    inicio()