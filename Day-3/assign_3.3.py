def vowels(str):
    vow = "aeiouAEIOU"
    count = 0
    for i in str:
        if i in vow :
            count = count + 1
    return count

def consonants(str):
    vow = "aeiouAEIOU"
    count = 0
    for i in str:
        if i not in vow :
            count = count + 1
    return count

def ratio(v,c):
    if c == 0 :
        print("The ratio is Zero!")
    else:
        r = v/c
    return r

ch = input("Enter string : ")
t = vowels(ch)
print("Number of vowels : ",t)

const = consonants(ch)
print("No consonants : ",const)

rat = ratio(t,const)
print("Ratio : ",rat)



