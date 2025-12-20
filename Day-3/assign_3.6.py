x = float(input("Enter num1 : "))
y = float(input("Enter num2 : "))

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return float(a)*float(b)

def division(a,b):
    return a/b

def calculate(p,q,func):
    return func(p,q)

add = calculate(x,y,addition)
print("Addition : ",add)

sub = calculate(x,y,subtraction)
print("Subtraction : ",sub)

mul = calculate(x,y,multiplication)
print("Multiplication : ",mul)

div = calculate(x,y,division)
print("Division : ",div)



