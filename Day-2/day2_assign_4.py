def is_prime(num):
    if num <= 1:
        return False # 0 & 1 are not prime numbers
    for i in range(2, num):
        if num % i == 0:
            return False # numbers having other factors are not prime
    return True

first = int(input("Enter first number: "))
last = int(input("Enter last number: "))

print("Prime numbers in given range:")
for i in range(first, last + 1): #range excludes last number so necessity of + 1
    if is_prime(i):
     print(i,end=" ")