# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.
def perfect():
    n=int(input("Ingrese la cantidad de números perfectos que desea conocer: "))
    cont=1
    x=7
    numero="6"
    if 0 < n < 5:
        while cont<n:
            suma=0
            for i in range (1,x+1):
                div = x%i
                if div==0:
                    suma+=i
            if suma-x==x:
                numero += str(f", {x}")
                cont+=1
            x+=1
        print('\n'+numero)
    else:
        print('\nEl número indicado es muy alto y no puede ser mostrado.')
if __name__ == "__main__":
    perfect()