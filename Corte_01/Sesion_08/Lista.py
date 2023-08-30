# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def agregar(milista):
    num = int(input("Que desea agregar?: "))
    milista.append(num)
    print(milista)

def insertar(milista):
    idx=int(input("Indique el indice: "))
    val=int(input("Cual es el valor que insertará: "))
    milista.insert(idx,val)
    # Inserta un valor en la lista en un índice específico.
    print(milista)

def formateo(milista):
    milista.clear()
    # Clear eliminará todos los valores de la lista.
    print(milista)

def remover(milista):
    print(milista)
    n=int(input("Que valor desea remover: "))
    milista.remove(n)
    # Remove eliminará el primer elemento que encuentre que coincida con el valor.
    print(milista)

def index(milista):
    print(milista)
    n=int(input("Indique la ubicación de la lista: "))
    p=milista.index(n)
    # Index revisará cúal es el elemento que se ubica en la posición de la lista.
    print(f"El elemento en la posición es {n} es {p}")

def extraer(milista):
    print(milista)
    n=int(input("Indique la posición a eliminar: "))
    milista.pop(n)
    # Pop eliminará el valor que se encuentre en la posición especificada.
    print(milista)

def main(milista):
    opc=''
    while opc!="exit":
        if opc == "1":
            agregar(milista)
        elif opc=="2":
            insertar(milista)
        
        elif opc=="3":
            formateo(milista)
        
        elif opc=="4":
            remover(milista)

        elif opc=="5":
            index(milista)
        elif opc=="6":
            extraer(milista)

        print("Seleccione una opción: \n",\
            "1. Append\n2. Insert\n3. Formatear\n",\
                "4. Remover\n5. Valor elemento\n6. Extraer")    
        opc=input("Selección: ") 

if __name__=="__main__":
    milista=[2,3,4]
    main(milista)