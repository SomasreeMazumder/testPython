'''input_string1 = input("enter a string")

resultf = ""
for i in input_string1:
    if i == 'i' or i == 's':
        pass
    else:
        resultf += i
print("input string : ", input_string1)
print("resultant string : ", resultf)'''

s1 = input("enter a string")
s2 = input("enter a diff String")
res = ""

for i in s1:
    for j in s2:
        if i == j:
            continue
        else:
            res += i
print("resultant string :", res)
