# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.
from math import sqrt as s
def vector():
    x1 = float(input("Ingrese el origen en x: "))
    y1 = float(input("Ingrese el origen en y: "))
    x2 = float(input("Ingrese el final en x: "))
    y2 = float(input("Ingrese el final en y: "))

    compx = x2-x1
    compy = y2-y1
    modulo = s(compx**2+compy**2)
    print(f'\nMódulo del vector: {modulo}\n'
        f'Componente en el eje x: {compx}\n'
        f'Componente en el eje y: {compy}\n')

if __name__ == "__main__":
    vector()