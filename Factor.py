number = int(input("Ingrese el numero: "))
acc = 1
while (number > 0 ):
    acc = number * acc
    number -= 1
print(acc)