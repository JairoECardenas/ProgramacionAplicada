# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def suma(n,m):
    n-=1
    m.append(2*n-1)
    suma(n,m)

if __name__=="__main__":
    n=int(input("Ingrese hasta que número desea sumar: "))
    m=[]
    suma(n,m)