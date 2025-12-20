num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. div")
choice = int(input("Enter your choice : "))

match choice:
    case 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    case 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    case 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    case 4:
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("invalid operation")