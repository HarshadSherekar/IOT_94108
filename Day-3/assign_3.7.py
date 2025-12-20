def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num -1)
f = factorial(5)
print("Factorial : ",f)


def power(base , pow):
    if pow == 0:
        return 1
    return base * power(base,(pow -1))
p = power(2,4)
print("Power : ",p)