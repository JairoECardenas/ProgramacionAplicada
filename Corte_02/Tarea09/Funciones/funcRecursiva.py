# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def recursiva(l):
    n=0
    mayor=0
    if len(l)>n:
        if mayor<=l[n]:
            mayor=l[n]
        n+=1
        recursiva(l)
    return mayor

def main():
    lista=[5,14,4,3,2,1]
    print(recursiva(lista))

if __name__ == "__main__":
    main()