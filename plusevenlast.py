print("Welcome to Even last Challenge!!!")
even = list(input("Introduce numbers: "))
input("Press enter...")

def evenlast(numbers):
    result = 0
    print(len(numbers))
    for n in numbers:
        even = numbers.index(n) % 2
        if even == 0:
            result += int(n)
        
evenlast(even)