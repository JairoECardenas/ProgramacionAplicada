# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

class Articulos():
    def __init__ (self, nombre:str, precio:float):
        self.__nombre=nombre
        self.__precio=precio

        #------------Setters------------
    def setNombre(self, nombre:str):
        self.__nombre=nombre

    def setPrecio(self, edad:int):
        self.__edad=edad

    #------------Getters------------
    def getNombre(self):
        return self.__nombre
    
    def getPrecio(self):
        return self.__precio
    
class IvaCero(Articulos):
    def __init__ (self, nombre:str, precio:float, iva:float):
        super().__init__(nombre,precio)
        self.__iva = 0.00

    def getIva(self):
        return self.__iva

class IvaCinco(Articulos):
    def __init__ (self, nombre:str, precio:float, iva:float):
        super().__init__(nombre,precio)
        self.__iva = 0.05

    def getIva(self):
        return self.__iva

class IvaDiecinueve(Articulos):
    def __init__ (self, nombre:str, precio:float, iva:float):
        super().__init__(nombre,precio)
        self.__iva = 0.19

    def getIva(self):
        return self.__iva
    
def importarDatos():
    f=open("Alimentos.txt","rt")
    listaAlimentos=f.read()
    f.close
    a=listaAlimentos.split('\n')
    datos={}
    for i in a[1:]:
        b=i.split(',')
        datos[b[0]]=[b[1],b[2]]
    return datos

def imprimir_menu():
    print("\n1) Mostrar la lista de productos disponibles.",\
        "\n2) Calcular el valor base de un producto.\n3) salir.")

def imprimir():
    f=open("Alimentos.txt","rt")
    listaAlimentos=f.readlines()
    f.close
    b=[]
    for a in listaAlimentos[1:]:
        b.append(a.split(','))
        b.sort(key=lambda x: x[2])
    print('\n-------------------------\n')
    for i, lista in enumerate(b):
        print(f'{i+1}. {lista[1]}')
    print('\n-------------------------\n')

def buscar_valor_base(datos):
    nombreAlimento=input('Ingrese el nombre del alimento tal y como aparece en la lista: ')
    for valor in datos.values():
        if valor[0]==nombreAlimento:
            valorNeto=int(input('Ingrese el valor neto del producto: '))
            valorBase=(valorNeto)/(1+float(valor[1]))
            print(f"\nEl valor base es: ${valorBase[0]}\nSu IVA es: {valor[1]*100}%")
            return round(valorBase,2),float(valor[1])
    print("\nHa ingresado un valor inválido, recuerte respetar las las mayusculas y minusculas.")
    return False

def main():
    datos=importarDatos()
    menu={'1': lambda:imprimir(),'2': lambda:buscar_valor_base(datos),'3': None}
    while True:
        imprimir_menu()
        opc=input("\nIngrese la opción que desea ejecutar: ")
        if opc in menu:
            if menu[opc] is None:
                break
            else:
                menu[opc]()

if __name__=="__main__":
    main()