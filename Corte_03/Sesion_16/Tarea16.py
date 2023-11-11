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

    def setPrecio(self, precio:int):
        self.__precio=precio

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
    datos=[]
    for i in a[1:]:
        b=i.split(',')
        if b[2] == '0':
            datos.append(IvaCero(b[1], None, b[2]))
        elif b[2] == '0.05':
            datos.append(IvaCinco(b[1], None, b[2]))
        elif b[2] == '0.19':
            datos.append(IvaDiecinueve(b[1], None, b[2]))
    return datos

def imprimir_menu():
    print("\n1) Mostrar la lista de productos disponibles.",\
        "\n2) Calcular el valor base de un producto.",\
        "\n3) Productos con precio registrado.\n4) salir.")

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
    for producto in datos:
        if producto.getNombre()==nombreAlimento:
            valorNeto=int(input('Ingrese el valor neto del producto: '))
            valorBase=round((valorNeto)/(1+producto.getIva()),2)
            print(f"\nEl valor base es: ${valorBase}\nSu IVA es: {producto.getIva()*100}%")
            producto.setPrecio(valorBase) # Establece el precio del producto
            return producto
    print("\nHa ingresado un valor inválido, recuerte respetar las las mayusculas y minusculas.")
    return None

def imprimir_productos_con_precio(datos):
    print("\n-------------------------")
    for producto in datos:
        if producto.getPrecio() is not None:
            print(f"Nombre del producto: {producto.getNombre()}")
            print(f"Precio base: {producto.getPrecio()}")
            print(f"IVA: {producto.getIva()*100}%")
            print("-------------------------")

def main():
    datos=importarDatos()
    menu={'1': lambda:imprimir(),'2': lambda:buscar_valor_base(datos),
          '3': lambda:imprimir_productos_con_precio(datos), '4': None}
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