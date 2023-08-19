nota = float(input("Ingrese su nota: "))

if(0 <= nota <= 5):
    if nota >= 3:
        print("Aprobó")
    else:
        print("Reprobó")
else:
    print("La nota ingresada es invalida")