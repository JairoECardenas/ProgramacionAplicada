# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.
from random import randint as r

def rates():
    comision = r(10,50)/100
    return comision

def selecMoneda(moneda):
    if moneda.upper() == "USD":
        comi = tasas[0]+tasas[0]*rates()
        return comi
    elif moneda.upper() == "EUR":
        comi = tasas[1]+tasas[1]*rates()
        return comi
    elif moneda.upper() == "CNY":
        comi = tasas[2]+tasas[2]*rates()
        return comi
    elif moneda.upper() == "JPY":
        comi = tasas[3]+tasas[3]*rates()
        return comi
    elif moneda.upper() == "PEN":
        comi = tasas[4]+tasas[4]*rates()
        return comi
    else:
        comi = "Selección invalida"
        print(comi)

def conversor(moneda,valor):
    precio = selecMoneda(moneda)
    cambio = valor//precio
    dev = valor-(precio*cambio)
    print(f"Cambio: {float(cambio)} {moneda}, Devolución: {round(dev,2)} COP")

def menu():
    print('''Programas disponibles:
          1) Consersión de COP a cualquier divisa seleccionada.
          2) Ver las tasas de cambio y la correspondiente comisión.\n''')
    menu = int(input("Dígite el número del programa: "))
    return menu

def main(tasas, monedas):
    
    m = menu()
    if m == 1:
        print("\n",monedas)
        m = input("A que divisa desea convertir: ")
        valor = int(input("Cuantos COP desea cambiar: "))
        conversor(m,valor)
    elif m == 2:
        for i in range(len(monedas)):
            print(f"divisa: {monedas[i]}, tasa: {tasas[i]}, Comisión: {rates()}")
    else:
        print("Selección Invalida.")

if __name__ == "__main__":
    tasas = [4108,4454,563,28,1106]
    monedas =["USD","EUR","CNY","JPY","PEN"]
    main(tasas, monedas)