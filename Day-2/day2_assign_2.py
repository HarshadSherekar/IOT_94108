
n1=int(input("enter the 5 digit number"))

d1=n1%10
d2=(n1//10)%10
d4=(n1//1000)%10
d5=n1//10000

if d1==d5 and d2==d4:
    print ("number is palindrome")
else:
    print("number is not palindrome")
