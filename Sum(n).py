def Sum(n, acc = 0):
    if n == 0:
        return acc
    else:
        return Sum(n-1,acc + n)
limt = int(input("Ingrese el numero: "))
print(Sum(limt))