def MCD(m, n):
    if m < n:
        (m, n) = (n, m)
    if (m%n) == 0:
        return n 
    else:
        return MCD(n, m%n)
Num1 = int(input("Ingrese primer valor: "))
Num2 = int(input("Ingrese segundo valor: "))
print(MCD(Num1, Num2))