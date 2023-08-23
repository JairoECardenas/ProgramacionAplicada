# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

# Una tupla es una seríe ordenada de datos
def app(*args,**kwargs):
    print(args)
    print(kwargs)

if __name__ == "__main__":
    p = input("Ingrese un texto de prueba: ")
    app(3,4,56,67,78,a=1,i=2,d=p)