# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def importarDatos():
    f=open("wcm.csv","r",encoding='utf8')
    baseDatos=f.read()
    f.close
    baseDatos=baseDatos.split('\n')
    lista=[]
    for i in baseDatos[1:]:
        b=i.split(',')
        lista.append(b)
    return lista

def main():
    datos=importarDatos()
    menu={'1':campeon_mundial,
        '2':subcampeon_mundial}
    opcion=input('Elija una opción: ')
    if opcion in menu:
        menu[opcion](datos)

if __name__=="__main__":
    main()