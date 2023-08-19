r = int(input('Ingrese el radio del recipiente: '))
                
v = (4/3)*3.1416*(r**3)
v = v*1000

print('El volumen de un recipiente de radio', r, 'm, es de', round(v,2), 'litros.')