# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def cuenta_atras(num):
    num -=1
    if num>0:
        print(num)
        cuenta_atras(num)
    else:
        print("BOOOOOOM!")
    print("Fin de la función",num)

if __name__=="__main__":
    cuenta_atras(5)
    # Una función recursiva es aquella que puede llamarse a si misma.