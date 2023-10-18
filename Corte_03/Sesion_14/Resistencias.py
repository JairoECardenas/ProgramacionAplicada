# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

def resistencia(banda):
    dic_color = {'negro':'0', 'cafe':'1', 'rojo':'2', 'naranja':'3', 'amarillo':'4',
                'verde':'5', 'azul':'6', 'morado':'7', 'gris':'8', 'blanco':'9'}
    num = dic_color[banda[0]] + dic_color[banda[1]]
    dic_pref = {'Kilo':3, 'Mega':6, 'Giga':9}

    print('-'.center(26,'-'))
    if int(dic_color[banda[2]]) <= 2:
        expo = int(dic_color[banda[2]])
        print(f'respuesta:{int(num)*(10**expo)} ohms')
    elif int(dic_color[banda[2]]) <= 4:
        expo = (dic_pref['Kilo'] - int(dic_color[banda[2]]))*-1
        print(f'respuesta:{int(num)*(10**expo)} Kilo-ohms')
    elif int(dic_color[banda[2]]) <= 7:
        expo = (dic_pref['Mega'] - int(dic_color[banda[2]]))*-1
        print(f'respuesta:{int(num)*(10**expo):.1f} Mega-ohms')
    else:
        expo = (dic_pref['Giga'] - int(dic_color[banda[2]]))*-1
        print(f'respuesta:{int(num)*(10**expo)} Giga-ohms')

def main():
    print('Bandas'.center(30,'-'))
    colores = []
    for i in range (3):
        banda = input(f'Color banda {i}: ')
        colores.append(banda)
    resistencia(colores)

if __name__ == '__main__':
    main()