import math

print("Calcula el LCM de 2 numeros")
a=int(input("Introduce el primer numero "))
b=int(input("Introduce el segundo numero "))

c = a*b // math.gcd(a,b)

print("El LCM de " + str(a) + " y " + str(b) + " es: " + str(c))
input("Presiona Enter...")