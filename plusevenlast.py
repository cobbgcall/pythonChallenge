print("Welcome to Even last Challenge!!!")
even = list(input("Introduce numbers: "))
input("Press enter...")

def evenlast(numbers):
    result = 0
    
    for n in numbers:
        even = numbers.index(n) % 2
        if even == 1:
            result += int(n)
            continue
    evenlast = result * int(numbers[numbers.index(n)])

    return evenlast  

last = evenlast(even)
print(last)