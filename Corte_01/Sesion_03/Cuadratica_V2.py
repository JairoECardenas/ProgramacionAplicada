import math as m

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

raiz = b**2-4*a*c
if raiz > 0:
    x1 = (-b+m.sqrt(raiz))/(2*a)
    x2 = (-b-m.sqrt(raiz))/(2*a)
    print("Las soluciones son: \n", f"x1 = {x1}", "\n", f"x2 = {x2}")
else:
    raiz = m.fabs(raiz)
    x_r = -b/(2*a)
    x_i = (m.sqrt(raiz))/(2*a)
    print("Las souciones son: \n",\
          "x1 =", x_r, "+",f"{x_i}i\n", \
          "x2 =", x_r, "-",f"{x_i}i")