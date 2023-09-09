# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

festivo={
    'Enero':['1 - año nuevo','6 - Reyes magos'],
    'Febrero':['No tiene festivos'],
    'Marzo':['20 - Día de San Jose']}

def main():
    mes=input('Ingrese un mes: ')
    print(festivo[mes])

if __name__=='__main__':
    main()