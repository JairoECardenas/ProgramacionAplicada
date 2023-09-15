# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.
def imprimir():
    f=open("Alimentos.txt","rt")
    listaAlimentos=f.read()
    f.close
    print(listaAlimentos)

def importarDatos():
    f=open("Alimentos.txt","rt")
    listaAlimentos=f.read()
    f.close
    a=listaAlimentos.split('\n')
    datos={}
    for i in a[1:]:
        b=i.split(',')
        datos[b[0]]=[b[1],b[2]]
    return datos

def buscar_valor_base(datos, nombreAlimento, valorNeto):
    for llave,valor in datos.items():
        if valor[0]==nombreAlimento:
            valorBase=(valorNeto)/(1+float(valor[1]))
            return round(valorBase,2)
    return None

def main():
    imprimir()
    datos=importarDatos()
    alimento=input('Ingrese el nombre del alimento tal y como aparece en la lista: ')
    valor=int(input('Ingrese el valor neto del producto: '))
    valorBase=buscar_valor_base(datos, alimento, valor)
    print(f"El valor base es: ${valorBase}")

if __name__=="__main__":
    main()