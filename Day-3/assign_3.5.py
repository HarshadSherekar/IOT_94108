def student_info(name, course="Python", duration="3 Months"):
    print("Name:", name)
    print("Course:", course)
    print("Duration:", duration)

student_info("Rahul")

def calculate(a, b):
    print("Sum:", a + b)

calculate(a=10, b=5)
calculate(b=20, a=5) 

def order(item, quantity=1, price=50):
    total = quantity * price
    print("Item:", item)
    print("Total Price:", total)

order("Pen")
order("Book", quantity=3)
order("Notebook", price=40, quantity=5)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def operate(func, x, y):
    return func(x, y)

result = operate(add, 10, 20)
print("Result:", result)

result = operate(sub, 20, 10)
print("Result:", result)