# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def busqueda(a, b, i=0):
    if len(a) < len(b):
        return []
    elif a[:len(b)] == b:
        return [i] + busqueda(a[1:], b, i+1)
        # Compará si desde la posición 0 hasta la longitud de b, a es igual a b.
    else:
        return busqueda(a[1:], b, i+1)

def main():
    a=input("Ingrese un texto: ")
    b=input("Ingrese elemento a buscar: ")
    print(busqueda(a,b))

if __name__=="__main__":
    main()