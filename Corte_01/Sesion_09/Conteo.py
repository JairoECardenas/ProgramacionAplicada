# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def conteo(num):
    if num > 0:
        num-=1
        conteo(num)
    print(num)

if __name__=="__main__":
    n=int(input("Hasta que número desea contar: "))
    conteo(n)