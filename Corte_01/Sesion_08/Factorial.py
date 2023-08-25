# …
# .===</PYTHON>===.
# .===</JAIROCKF>===.
# …
# This code was created by Jairo Cárdenas, a mechatronic engineering student.
def factorial(a):
    fact = 1
    for i in range (a):
        fact*=(i+1)
    return fact
if __name__ == "__main__":
    n = int(input("Ingrese un número para realizar el factorial: "))
    print(factorial(n))