# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

class Ciudadano(): # Crea la clase padre
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
    
    @staticmethod # Se usa un método estatico para acceder a él sin instancias
    def mostrar_todos(lista):
        for p in lista:
            print('\n------------------------')
            print(p.mostrar())
            print('------------------------')

    def es_mayor_de_edad(self):
        return self.__edad >= 18

class Mecatronico(Ciudadano): # Primera clase hija
    def __init__(self, lista, campo1, campo2):
        super().__init__(lista)
        self.campo1 = campo1 # Arduinos quemados
        self.campo2 = campo2 # Horas en lol

    def metodo_unico_mecatronico(self):
        print(f'{self.getNombre()} es un gran Ingeniero a pesar de acumular {self.campo2} horas en lol.')

    def mostrar(self):
        info_base = super().mostrar()
        return f'{info_base}\nProfesión: Mecatronico\n' \
            f'Arduinos quemados: {self.campo1}\nTiempo jugando League of Legends: {self.campo2} horas'

class Piloto(Ciudadano): # Segunda clase hija
    def __init__(self, lista, campo1, campo2):
        super().__init__(lista)
        self.campo1 = campo1 # Vuelos realizados
        self.campo2 = campo2 # Record Personal

    def metodo_unico_piloto(self):
        print(f'{self.getNombre()} ha realizado {self.campo1()} vuelos a sus {self.getEdad()} años de edad.')

    def mostrar(self):
        info_base = super().mostrar()
        return f'{info_base}\nProfesión: Piloto\nVuelos realizados: {self.campo1}\nRecord personal: {self.campo2}km'

class Artista(Ciudadano): # Tercer clase hija
    def __init__(self, lista, campo1, campo2):
        super().__init__(lista)
        self.campo1 = campo1 # Técnica artistica
        self.campo2 = campo2 # Medio utilizado

    def metodo_unico_artista(self):
        print(f'Los cuadros que realiza {self.getNombre()} en {self.campo1()} son espectaculares.')

    def mostrar(self):
        info_base = super().mostrar()
        return f'{info_base}\nProfesión: Artista\nTécnica preferida: {self.campo1}\nArte: {self.campo2}'
    
def mostrar_mayores_menores(lista):
    for p in lista:
        print('\n------------------------')
        print(p.getNombre())
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

def seleccionar_profesion_y_metodo(lista):
    print('Profesiones disponibles:')
    profesiones = ['Mecatronico', 'Piloto', 'Artista']
    for i, profesion in enumerate(profesiones):
        print(f'{i+1}: {profesion}')
    indice_profesion = int(input('Seleccione una profesión: '))-1
    
    print('Lista de ciudadanos registrados:')
    # Se compara la clase de la instancia con la ingresada por el usuario.
    instancias = [p for p in lista if type(p).__name__ == profesiones[indice_profesion]]
    for i, instancia in enumerate(instancias):
        print(f'{i+1}: {instancia.getNombre()}')
    indice_instancia = int(input('Seleccione un ciudadano: '))-1
    
    if profesiones[indice_profesion] == 'Mecatronico':
        instancias[indice_instancia].metodo_unico_mecatronico()
    elif profesiones[indice_profesion] == 'Piloto':
        instancias[indice_instancia].metodo_unico_piloto()
    elif profesiones[indice_profesion] == 'Artista':
        instancias[indice_instancia].metodo_unico_artista()
    else:
        print('Ha seleccionado un valor inválido.')

def main():
    persona=[]
    opc=''
    # El comando lambda evita que se ejecuten las funciones antes de ser llamadas por el usuario.
    menu = {'1': lambda: agregar(persona), '2': lambda: Ciudadano.mostrar_todos(persona),
            '3': lambda: mostrar_mayores_menores(persona),
            '4': lambda: seleccionar_profesion_y_metodo(persona), '5': None}
    while True:
        print('\n','Clase Estudiantes'.center(26,'-'))
        print('1) Agregar un núevo ciudadano.\n2) Mostrar los datos guardados.\n3) Conocer si es mayor o menor.' \
              '\n4) Ejecutar un metodo único.\n5) Salir.')
        opc=input('Dígite la opción que desea ejecutar: ')
        if opc in menu:
            if menu[opc] is None:
                break
            else:
                menu[opc]()

if __name__ == "__main__":
    main()