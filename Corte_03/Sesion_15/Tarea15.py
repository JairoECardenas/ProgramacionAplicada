# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

class Ciudadano():
    def __init__(self,lista:list):
        self.__nombre=lista[0]
        self.__documento=lista[1]
        self.__edad=int(lista[2])
    
    #------------Setters------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    
    def setDocumento(self,documento:str):
        if 8 <= len(documento) <= 10:
            self.__documento=documento
        else:
            print('El documento ingresado no cuenta con la longitud correcta.')

    def setEdad(self,edad:int):
        if 0 < edad:
            self.__edad=edad
        else:
            print('Las edades no pueden ser menores a cero.')
    
    #------------Getters------------
    def getNombre(self):
        return self.__nombre
    
    def getDocumento(self):
        return self.__documento
    
    def getEdad(self):
        return self.__edad
    
    #------------Métodos------------
    def mostrar(self):
        return f'Nombre: {self.getNombre()}\nCédula: {self.getDocumento()}\nEdad: {self.getEdad()}'
    
    @staticmethod
    def mostrar_todos(lista):
        for p in lista:
            print('\n------------------------')
            print(p.mostrar())
            print('------------------------')

    def es_mayor_de_edad(self):
        return self.__edad >= 18

class Mecatronico(Ciudadano):
    def __init__(self, lista, campo1, campo2):
        super().__init__(lista)
        self.campo1 = campo1
        self.campo2 = campo2

    def metodo_unico(self):
        pass

    def mostrar(self):
        info_base = super().mostrar()
        return f'{info_base}\nProfesión: Mecatronico\n' \
            f'Arduinos quemados: {self.campo1}\nTiempo jugando League of Legends: {self.campo2} horas'

class Piloto(Ciudadano):
    def __init__(self, lista, campo1, campo2):
        super().__init__(lista)
        self.campo1 = campo1
        self.campo2 = campo2

    def metodo_unico(self):
        pass

    def mostrar(self):
        info_base = super().mostrar()
        return f'{info_base}\nProfesión: Piloto\nVuelos realizados: {self.campo1}\nRecord personal: {self.campo2}km'

class Artista(Ciudadano):
    def __init__(self, lista, campo1, campo2):
        super().__init__(lista)
        self.campo1 = campo1
        self.campo2 = campo2

    def metodo_unico(self):
        pass

    def mostrar(self):
        info_base = super().mostrar()
        return f'{info_base}\nProfesión: Artista\nTécnica preferida: {self.campo1}\nArte: {self.campo2}'
    
def mostrar_mayores_menores(lista):
    for p in lista:
        print('\n------------------------')
        print(p.mostrar())
        if p.es_mayor_de_edad():
            print('Es mayor de edad.')
        else:
            print('Es menor de edad.')
        print('------------------------')

def agregar(lista):
    print('\n------------------------')
    print('Dígite el nombre, cédula, la edad y la profesión (Mecatronico, Piloto, Artista o Ninguna) separados por comas.')
    datos=input('Datos: ').split(',')
    profesion = datos.pop().strip(' ')
    if profesion == 'Mecatronico':
        campo1 = input('Ingrese número de arduinos quemados: ')
        campo2 = input('Ingrese horas jugando lol: ')
        lista.append(Mecatronico(datos, campo1, campo2))
    elif profesion == 'Piloto':
        campo1 = input('Conteo de vuelos realizados: ')
        campo2 = input('Ingrese record de altura personal en kilometros: ')
        lista.append(Piloto(datos, campo1, campo2))
    elif profesion == 'Artista':
        campo1 = input('Ingrese técnica preferida: ')
        campo2 = input('Especifique si su arte es digital o análogo: ')
        lista.append(Artista(datos, campo1, campo2))
    else:
        lista.append(Ciudadano(datos))
    print('Ciudadano registrado con éxito.')
    print('------------------------')

def main():
    persona=[]
    opc=''
    menu = {'1': lambda: agregar(persona), '2': lambda: Ciudadano.mostrar_todos(persona),
            '3': lambda: mostrar_mayores_menores(persona), '4': None}
    while True:
        print('\n','Clase Estudiantes'.center(26,'-'))
        print('1) Agregar un núevo ciudadano.\n2) Mostrar los datos guardados.\n3) Conocer si es mayor o menor.\n4) Salir.')
        opc=input('Dígite la opción que desea ejecutar: ')
        if opc in menu:
            if menu[opc] is None:
                break
            else:
                menu[opc]()

if __name__ == "__main__":
    main()