# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

from random import randint as r

def randlist(l):
    for i in range (0,15):
        num = r(0,100)
        l.append(num)
    return l.sort()

def festivos(m):
    if m.lower() == "enero":
        enero = ["Tiene 31 días", "Año Nuevo", "Reyes Magos"]
        return enero
    
    elif m.lower() == "febrero":
        febrero = ["Tiene 28 días", "No tiene festivos"]
        return febrero
    
    elif m.lower() == "marzo":
        marzo = ["Tiene 31 días", "Día de San José"]
        return marzo
    
    elif m.lower() == "abril":
        abril = ["Tiene 30 días", "Jueves Santo", "Viernes Santo"]
        return abril
    
    elif m.lower() == "mayo":
        mayo = ["Tiene 31 días", "Día del trabajo", "Ascención de Jesús"]
        return mayo
    
    elif m.lower() == "junio":
        junio = ["Tiene 30 días", "Corpus Christi", "Sagrado Corazón de Jesús"]
        return junio
    
    elif m.lower() == "julio":
        julio = ["Tiene 31 días", "San Pedro y San Pablo", "Día de la independencia"]
        return julio
    
    elif m.lower() == "agosto":
        agosto = ["Tiene 31 días", "Batalla de Boyacá", "Asunción de la Virgen"]
        return agosto
    
    elif m.lower() == "septiembre":
        septiembre = ["Tiene 30 días", "No tiene festivos"]
        return septiembre
    
    elif m.lower() == "octubre":
        octubre = ["Tiene 31 días", "Día de la raza"]
        return octubre
    
    elif m.lower() == "noviembre":
        noviembre = ["Tiene 30 días", "Todos los Santos", "Independencia de Cartagena"]
        return noviembre
    
    elif m.lower() == "diciembre":
        diciembre = ["Tiene 31 días", "Inmaculada Concepción", "Navidad"]
        return diciembre
    
    else:
        error = "El valor ingresado no es valído"
        return error

def listaAppend(l):
    n = 0
    print("El programa solicitará números para agregar a la lista hasta que ingrese un negativo.\n")
    while n > -1:
        n = int(input("Ingrese un número: "))
        l.append(n)
    print(l)
    l2 = list(set(l))
    return l2

def main():
    print('''
          Escoja entre las 3 opciones de programas que están disponibles:\n
          1). Lista de números aleatorios.\n
            Descripción: El programa generara una lista de 15 números aleatorios ordenados
          de menor a mayor.\n \n
          2) Días Festivos.\n
            Descripción: El usuario deberá ingresar un mes del año y el programa devolvera
          el número de días que tiene dicho mes junto con sus festivos.\n \n
          3) Lista númerica.\n
            Descripción: El usuario ingresará una secuencia de números a gusto y el programa
          devolvera dos listas, una como la ha ingresado el usuario y otra donde se eliminaran los
          números duplicados.\n \n
          ''')
    
    select = input("Por favor ingrese el número del programa que desea ejecutar: ")
    if select == "1":
        lista=[]
        randlist(lista)
        print(lista)

    elif select == "2":
        mes = input("Ingrese un mes del año: ")
        print(festivos(mes))

    elif select == "3":
        lista=[]
        
        print(listaAppend(lista))

    else:
        print("El valor ingresado no es valído")

if __name__ == "__main__":
    main()