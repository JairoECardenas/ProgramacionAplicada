# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def numero_enfrentamientos(listado): # Está función tiene un valor de 5 pts
    eq1=input('Digite el primer equipo: ')
    eq2=input('Digite el segundo equipo: ')
    historial={}
    vic1=0
    der1=0
    vic2=0
    der2=0
    emp=0
    for partidos in listado:
        if partidos[0]==eq1 and partidos[1]==eq2 or partidos[0]==eq2 and partidos[1]==eq1:
            listaTemp=[partidos[16],partidos[12],partidos[0],partidos[2],partidos[1],partidos[4]]
            historial[partidos[15]]=listaTemp
            if partidos[2] != partidos[4]:
                if eq1==partidos[0] and partidos[2]>partidos[4] or eq1==partidos[1] and partidos[4]>partidos[2]:
                    vic1+=1
                    der2+=1
                else:
                    vic2+=1
                    der1+=1
            else:
                emp+=1
    print(f'Cantidad de partidos: {len(historial)}')
    print(f'Historial: {eq1} => {vic1} victorias, {emp} empates, {der1} derrotas.')
    print(f'           {eq2} => {vic2} victorias, {emp} empates, {der2} derrotas.\n')
    for host,value in historial.items():
        print('-----------------------------------------------------------')
        print(f'-({host}-{value[0]})-\n'.center(60))
        print(f'{value[2]} |{value[3]} vs {value[5]}| {value[4]} - Ronda: {value[1]}'.center(60))
        print('-----------------------------------------------------------')

def mayores_goleadas(listado):# Está función tiene un valor de 5 pts
    goleadas={}
    goleada_ord={}
    num=int(input('Desea conocer hasta cuantos partidos por mundial (max. 10): '))
    if num <= 10:
        print('a. Ver la lista completa de mayores goleadas en mundiales.\n'
            'b. Busqueda por mundial.')
        select=input('----> ')
        print('Listado de mayores goleadas'.center(60,'-'))
        print('\n')
        if select=='a':
            for partidos in listado:
                goles=abs(int(partidos[2])-int(partidos[4]))
                if partidos[16] not in goleadas:
                    goleadas[partidos[16]]=[[goles,partidos[15],partidos[0],partidos[2],partidos[4],partidos[1],partidos[12]]]
                else:
                    list_gol=goleadas[partidos[16]]
                    list_gol.append([goles,partidos[15],partidos[0],partidos[2],partidos[4],partidos[1],partidos[12]])
                    goleadas[partidos[16]]=list_gol
            for year, value in goleadas.items():      
                goleada_ord[year]=sorted(value,reverse=True)
            for year,value in goleada_ord.items():
                print(f'{value[0][1]} - {year}'.center(60,'-'))
                for i in range(num):
                    print(f'{i+1}. Por {value[i][0]} goles: {value[i][2]} | {value[i][3]} vs',\
                        f'{value[i][4]} | {value[i][5]} (Ronda: {value[i][6]})')
        elif select=='b':
            mundial_year=input('Escriba el año del mundial que desea consultar --> ')
            for partidos in listado:
                goles=abs(int(partidos[2])-int(partidos[4]))
                if mundial_year == partidos[16] and partidos[16] not in goleadas:
                    goleadas[partidos[16]]=[[goles,partidos[15],partidos[0],partidos[2],partidos[4],partidos[1],partidos[12]]]
                elif mundial_year == partidos[16] and mundial_year in goleadas:
                    list_gol=goleadas[partidos[16]]
                    list_gol.append([goles,partidos[15],partidos[0],partidos[2],partidos[4],partidos[1],partidos[12]])
                    goleadas[partidos[16]]=list_gol
            for year, value in goleadas.items():      
                goleada_ord[year]=sorted(value,reverse=True)
            for year,value in goleada_ord.items():
                print(f'{value[0][1]} - {year}'.center(60,'-'))
                for i in range(num):
                    print(f'{i+1}. Por {value[i][0]} goles: {value[i][2]} | {value[i][3]} vs',\
                        f'{value[i][4]} | {value[i][5]} (Ronda: {value[i][6]})')
        else:
            print('El valor ingresado no está entre las opciones.')
    else:
        print('Ha ingresado un valor superior a 10, volviendo al menu.')

def main():
    pass

if __name__=='__main__':
    main()