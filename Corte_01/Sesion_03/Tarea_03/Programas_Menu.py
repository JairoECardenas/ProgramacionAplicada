# Autor Jairo Esteban Cárdenas Fajardo

print("Los programas disponibles son los siguientes:\n" + \
      "1) Vocal o Consonante.\n2) Factura Parqueadero.\n3) Identificador de Triángulos.")

program = input("\nSeleccione el programa que desea ejecutar usando el número indicado: ")

if (program == "1"):
    letra = input("\nEscriba una letra para ser evualuada: ")
    if (letra.lower() == "a" or letra.lower() == "e" \
        or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u"):
        print("\nLa letra es una vocal.")
    else:
        print("\nLa letra es una consonante.")

elif (program == "2"):
    tiempo = int(input("\nIngrese el tiempo que duro parqueado en minutos: "))
    Subtotal = tiempo*139
    ValorIVA = Subtotal*0.19
    Total = Subtotal+ValorIVA
    roundTotal = round(Total/50)*50

    print("\n           PARQUEADERO USB\n \n", \
        f"     Tiempo de uso: {tiempo} min\n", \
        " Tarifa por minuto: $139\n", \
        f"          Subtotal: ${Subtotal}\n", \
        f"         IVA (19%): ${ValorIVA}\n \n", \
        "--------------------------------------\n \n", \
        f"        Total neto: ${Total}\n",\
        f"  Total aproximado: ${roundTotal}")
    
elif (program == "3"):
    print("\nIngrese 3 longitudes: ")
    l1 = int(input("\nLado 01: "))
    l2 = int(input("Lado 02: "))
    l3 = int(input("Lado 03: "))

    if (l1 < l2+l3 and l2 < l1+l3 and l3 < l2+l1):

        if (l1 == l2 and l2 == l3):
            print("\nLas tres longitudes pueden formar un triángulo equilatero.")
        elif (l1 != l2 and l1 != l3 and l2 != l3):
            print("\nLas tres longitudes pueden formar un triángulo escaleno.")
        else:
            print("\nLas tres longitudes pueden formar un triángulo isósceles.")

    else:
        print("\nLas longitudes ingresadas no pueden formar un triángulo.")

else: 
    print("Ha ingresado un valor inválido.")