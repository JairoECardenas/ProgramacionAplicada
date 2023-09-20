# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.

a=[1,2,3,4]
b=['Uno','Dos','Tres','Cuatro']
x=zip(a,b)
# El zip combina dos listas o tuplas en una sola.
m=list(x)
# print(m)

for idx,valor in enumerate(m):
    print(idx)
    print(valor)