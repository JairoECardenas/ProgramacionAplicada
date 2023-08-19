# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

print("""\nBienvenid@, estos son los programas disponibles:\n \n
    1) Divisores de un número.\n
        Descripción: El usuario proporcionará un número y el programa
        retornara todos los divisores positivos de dicho número.\n \n
    2) Producto entre dos números.\n
        Descripción: El usuarío proporcionará dos números de los cuales
        desea conocer su producto.\n \n
    3) Serie de Fibbonacci.\n
        Descripción: El usuario proporcionará el número de valores de
        la serie de Fibbonacci que desea conocer.\n
    """)
program=int(input("\nPor favor, ingrese el dígito del programa que desea ejecutar: "))

if program == 1:
    print("\nUsted ha seleccionado el primer programa\n")
    n=int(input("Ingrese el número del que desea conocer los divisores: "))
    cont=2
    div="1"
    if n > 0:
        while cont < n+1:
            x=n%cont
            if x==0:
                div+=str(f", {cont}")
            cont+=1
        print(f"\nLos divisores de {n} son:\n{div}")
    elif n == 0:
        print("\nNingún número es divisible entre cero")

elif program == 2:
    print("\nUsted ha seleccionado el segundo programa\n")
    x=int(input("Ingrese el primer número: "))
    y=int(input("Ingrese el segundo número: "))
    produc=0
    for i in range(abs(x)):
        produc+=y
    if x<0 and y<0:
        produc=abs(produc)
    elif x<0:
        produc*=-1
    print(f"\nEl producto de {x} y {y} es: {produc}")

elif program == 3:
    print("\nUsted ha seleccionado el tercer programa\n")
    n=int(input("Ingrese la cantidad de dígitos que desea conocer"
                "de la serie de Fibbonacci: "))
    x=0
    y=1
    numero="0"
    for i in range (n-1):
        suma=x+y
        y=x
        x=suma
        numero+=str(f", {x}")
    print(f"\nLos primeros {n} dígitos de Fibbonacci son:\n{numero}")

else:
    print("\nHa ingresado un valor inválido.")