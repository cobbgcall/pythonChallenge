print("Buscar cat and dog en la misma frase")
a = input("Introduce una frase con la palabra cat y dog: ")
b = a.count("cat")
c = a.count("dog")
if b == c:
    print("True")
else:
    print("False")