# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def imprimir_menu():
    print("\n1) Mostrar la lista de productos disponibles.",\
        "\n2) Calcular el valor base de un producto.\n3) salir.")

def imprimir():
    f=open("Alimentos.txt","rt")
    listaAlimentos=f.read()
    f.close
    print('\n-------------------------\n')
    print(listaAlimentos)
    print('\n-------------------------\n')

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

def buscar_valor_base(datos, nombreAlimento):
    for valor in datos.values():
        if valor[0]==nombreAlimento:
            valorNeto=int(input('Ingrese el valor neto del producto: '))
            valorBase=(valorNeto)/(1+float(valor[1]))
            return round(valorBase,2)
    print("\nHa ingresado un valor inválido, recuerte respetar las las mayusculas y minusculas.")
    return False

def main():
    datos=importarDatos()
    while True:
        imprimir_menu()
        opc=input("\nIngrese la opción que desea ejecutar: ")
        if opc=='1':
            imprimir()
        elif opc=='2':    
            alimento=input('Ingrese el nombre del alimento tal y como aparece en la lista: ')
            valorBase=buscar_valor_base(datos, alimento)
            if valorBase!=False:
                print(f"El valor base es: ${valorBase}")
        elif opc=='3' or opc.lower()=='salir':
            break
        else:
            print("Error, selección inválida.")

if __name__=="__main__":
    main()