def split_list(items: list) -> list:
    # your code here
    
    a = len(items)
    b = a % 2
    tupleA = []
    tupleB = []
    tupleT = []
    c = a // 2
    
    if b > 0:
        d = c + 1
        for x in range(0,d):
            tupleA.append(items[x]) 
        for y in range(d,a):
            tupleB.append(items[y]) 
    else:
        for x in range(0,c):
            tupleA.append(items[x])
        for y in range(c,a):
            tupleB.append(items[y])

    tupleT.append(tupleA)
    tupleT.append(tupleB)

    return tupleT

if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3]))
