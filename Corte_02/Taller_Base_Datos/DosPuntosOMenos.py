# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def campeon_mundial(listado):
    campeones={}
    for partidos in listado:
        if partidos[12]=='Final':
            if (partidos[2]>partidos[4])or(partidos[3]>partidos[5]):
                if partidos[0] not in campeones:
                    campeones[partidos[0]]=[partidos[16]]
                else:
                    list_year=campeones[partidos[0]]
                    list_year.append(partidos[16])
                    campeones[partidos[0]]=list_year                
            else:
                if partidos[1] not in campeones:
                    campeones[partidos[1]]=[partidos[16]]
                else:
                    list_year=campeones[partidos[1]]
                    list_year.append(partidos[16])
                    campeones[partidos[1]]=list_year
    campeones=dict(sorted(campeones.items()))
    print('\n---------------Listado de Campeones mundiales ----------------\n')
    for pais,year in campeones.items():
        print(f'{pais}: campeón en {year}')
    
    pais=input('Ingrese un pais: ')
    
    if pais in campeones:
        year=campeones[pais]
        print(f'fue campeon en los años {year}')
    else:
        print(f'{pais} no ha sido campeon del mundo')

def subcampeon_mundial(listado):
    subcampeones={}
    for partidos in listado:
        if partidos[12]=='Final':
            if (partidos[2]>partidos[4])or(partidos[3]>partidos[5]):
                if partidos[1] not in subcampeones:
                    subcampeones[partidos[1]]=[partidos[16]]
                else:
                    list_year=subcampeones[partidos[1]]
                    list_year.append(partidos[16])
                    subcampeones[partidos[1]]=list_year                
            else:
                if partidos[0] not in subcampeones:
                    subcampeones[partidos[0]]=[partidos[16]]
                else:
                    list_year=subcampeones[partidos[0]]
                    list_year.append(partidos[16])
                    subcampeones[partidos[0]]=list_year
    print(subcampeones)

def main():
    pass

if __name__=='__main__':
    main()