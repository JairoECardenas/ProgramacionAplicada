# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def recursiva(l,n,mayor):
    if n<len(l):
        if mayor<=l[n]:
            mayor=l[n]
        n+=1
        recursiva(l,n,mayor)
    return mayor

def main():
    lista=[5,14,4,3,2,1]
    n=0
    mayor=0
    print(recursiva(lista,n,mayor))

if __name__ == "__main__":
    main()