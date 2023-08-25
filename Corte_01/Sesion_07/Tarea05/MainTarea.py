# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.
import FuncionPerfecto as p
import FuncionVector as v
def main():
    print('Bienvenido al programa de tarea de la sesión #07\n'
          'Por favor seleccione cual de las siguientes funciones desea llamar.\n'
          '\n1) Función Vector.\n'
          'Descripción: El programa solicita las coordenadas de origen y final '
          'de un vector y este retornara el módulo de dicho vector.\n'
          '\n2) Función números perfectos.\n'
          'Descripción: El programa solicita un número del 1 al 4 para mostrar la secuencia '
          'de números perfectos conocidos hasta el momento.\n')
    n = int(input('\nDigite el número del programa a ejecutar: '))
    if n == 1:
        v.vector()
    elif n == 2:
        p.perfect()
    else:
        print("\nHa escogido un valor inválido.")
if __name__ == "__main__":
    print("\nInicio del programa.\n")
    main()
    print("\nFin del programa.")