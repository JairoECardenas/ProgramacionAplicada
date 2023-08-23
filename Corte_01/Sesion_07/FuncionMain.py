# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

import FuncionExterna as Fcn_ext
import Funcion03 as F3
# Importando una funcion de código dentro de la misma carpeta

def main():
    nombre = input("Ingrese su nombre: ")
    surname = input("Ingrese su apellido: ")
    print("------------------------")
    Fcn_ext.matrix(nombre,surname)
    print("------------------------")
    F3.suma()
    print("------------------------")
    print(f"Ejecutado desde {__name__}")

if __name__ == "__main__": 
    #Está condición permite que el código solo se ejecute cuando la función sea la principal
    main()