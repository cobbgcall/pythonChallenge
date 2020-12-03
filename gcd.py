import math

print("Calcula el gcd de 2 numeros")
a=int(input("Introduce el primer numero "))
b=int(input("Introduce el segundo numero "))

c = math.gcd(a,b)

print("El gcd de " + str(a) + " y " + str(b) + " es: " + str(c));
