# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

class IndMasCor:

    def __init__(self):
        self.__nombre=None
        self.__estatura=None
        self.__peso=None

    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre

    def setEstatura(self,estatura:float):
        self.__estatura=estatura

    def getEstatura(self):
        return self.__estatura

    def setPeso(self,peso:int):
        self.__peso=peso

    def getPeso(self):
        return self.__peso

def calcularIMC(peso,estatura):
    imc=(peso/(estatura/100)**2)
    if imc < 18.5:
        estado='Por debajo'
    elif 18.5 <= imc <= 24.9:
        estado='Saludable'
    elif 25 <= imc <= 29.9:
        estado='Sobrepeso'
    elif 30 <= imc <= 34.9:
        estado='Obesidad I'
    elif 35 <= imc <= 39.9:
        estado='Obesidad II'
    elif 40 <= imc:
        estado='Obesidad III'
    else:
        estado='Error, valor fuera de la escala'
    return round(imc,2),estado

def listaDefecto():

    lista_nombres=['Pedro Caceres','Maria Pérez','Julian Dominguez','Jessica Fuentes']
    lista_estatura=[188, 160,158,170]
    lista_peso=[97,47,58,73]
    listaDef=[]
    for i in range(len(lista_nombres)):
        persona=IndMasCor()
        persona.setNombre(lista_nombres[i])
        persona.setEstatura(lista_estatura[i])
        persona.setPeso(lista_peso[i])
        listaDef.append(persona)
    return listaDef

def listaUsuario():
    
    continuar='Y'
    listaUser=[]
    while True:
        if continuar.upper() == 'Y':
            persona=IndMasCor()
            persona.setNombre(input('\nIngrese el nombre de la persona: '))
            persona.setEstatura(float(input('Ingrese la altura de la persona en cm: ')))
            persona.setPeso(int(input('Ingrese el peso de la persona en kg: ')))
            listaUser.append(persona)
        elif continuar.upper() == 'N':
            break
        else:
            print('Valor inválido')
        continuar=input('¿Desea agregar más personas a la lista? (Y/N): ')
    return listaUser

def main():
    while True:
        print('\nBienvenido, para iniciar seleccione uno de los siguientes códigos.',\
            '\n1) Conocer el valor de IMC de una lista creada por defecto.',\
            '\n2) Crear su propia lista de personas para calcular su IMC.',\
            '\n3) Salir del programa.')

        menu={'1':listaDefecto,'2':listaUsuario}
        opcion=input('\nIngrese una opción: ')
        if opcion in menu and opcion != '3':
            a=menu[opcion]()
            for i in a:
                b=calcularIMC(i.getPeso(),i.getEstatura())[0] # b es el valor del IMC
                c=calcularIMC(i.getPeso(),i.getEstatura())[1] # c es el estado según la tabla del obesidad
                print(f'\nEl IMC de {i.getNombre()} es de: {b}.',\
                    f'\nSu estado de salud es {c}.\n')
        
        elif opcion == '3':
            break
        else:
            print('No ha seleccionado un item de la lista')
        
if __name__=='__main__':
    main()