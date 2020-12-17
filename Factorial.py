def Factor(n, acc = 1):
    if n == 0:
        return acc
    else:
        return Factor(n-1, acc * n)
fac = int(input("Ingrese el numero: "))
print(Factor(fac))