import math as m

print("Figuras disponibles: \n",\
     "1. Circulo\n 2. Triangulo \n 3. Cuadrado")

fig = input("Seleccione una figura: ")
A = "invalida"

if (fig.lower() == "circulo") or (fig=="1"):
    r = eval(input("Ingrese el valor del radio: "))
    A = m.pi*r**2
    figura = "circulo"

elif (fig.lower() == "triangulo") or (fig == "2"):
    b = eval(input("Ingrese la base: "))
    h = eval(input("Ingrese la altura: "))
    A = (b*h)/2
    figura = "triangulo"

elif (fig.lower() == "rectangulo") or (fig=="3"):
    b = eval(input("Ingrese la base: "))
    h = eval(input("Ingrese la altura: "))
    A = b*h
    figura = "rectangulo"
else:
    print("Seleccione una figura valida")

print(f"Para un {figura}, el valor del área es {A}u²")