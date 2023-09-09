# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def lectura():
    f=open("matrizAsignacion.txt","rt")
    # Para poder llamar un archivo, hace falta poner el nombre exacto con su extensión.
    # También se debe aclarar la ruta en caso de no estar en la misma carpeta.
    line=f.readlines()
    f.close() # Luego de leer el documento y guardarlo, se puede cerrar para ahorra recursos.
    for i in line:
        a=i.rstrip("\n").split(",")
        print(f"{a} => {int(a[0])+int(a[1])}")

def lectura2():
    f=open("matrizAsignacion.txt","rt")
    line=f.readline()
    while line != '':
        print(line)
        opc=input("Presione Enter")
        line=f.readline()
    f.close()
    print('Finalizo la lectura.')

def lectura3():
    f=open("matrizAsignacion.txt","rt")
    line=f.read()
    f.close()
    print(line,len(line))
    print('-------------')
    a=line.split('\n')
    for i in a:
        b=i.split(',')
        print(b)

if __name__ == "__main__":
    #lectura()
    #lectura2()
    lectura3()