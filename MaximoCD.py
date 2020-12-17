number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

a = max(number1, number2)
b = min(number1, number2)

while (b != 0):
    acc = b
    b = a%b
    a = acc
print(acc)