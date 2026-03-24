number = int(input("Insert a number... "))
number2 = int(input("Insert a multiple... "))

for multiple in range(1, number2 + 1):
    multiplication = number * multiple
    print(number, "x", multiple, "=", multiplication)
