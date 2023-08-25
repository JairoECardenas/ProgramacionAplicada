# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.
from Factorial import factorial as f
def main():
    n = int(input("Por favor ingrese el número de elementos: "))
    m = int(input("Por favor ingrese en número de muestras: "))
    nm = (f(n))/(f(m)*f(n-m))
    print(f"\nLa cantidad de combinaciones que puede realizar para {n} elementos en {m} muestras es: {int(nm)}")
if __name__ == "__main__":
    print("Inicio del programa.\n")
    main()
    print("\nFinal del programa.\n")