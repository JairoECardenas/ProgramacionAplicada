# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def numero_enfrentamientos(listado): # Está función tiene un valor de 5 pts
    eq1=input('Digite el primer equipo: ')
    eq2=input('Digite el segundo equipo: ')
    historial={}
    for partidos in listado:
        if partidos[0]==eq1 and partidos[1]==eq2 or partidos[0]==eq2 and partidos[1]==eq1:
            listaTemp=[partidos[16],partidos[12],partidos[0],partidos[2],partidos[1],partidos[4]]
            historial[partidos[15]]=listaTemp
    for host,value in historial.items():
        print('-----------------------------------------------------------')
        print(f'-({host}-{value[0]})-\n'.center(60))
        print(f'{value[2]} |{value[3]} vs {value[5]}| {value[4]} - Ronda: {value[1]}'.center(60))
        print('-----------------------------------------------------------')

def main():
    numero_enfrentamientos()

if __name__=='__main__':
    main()