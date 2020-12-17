limit = int(input("Ingresar un numero: "))

acc = 1
counter = 2

while(counter<=limit):
    acc = counter + acc
    counter += 1
print(acc)