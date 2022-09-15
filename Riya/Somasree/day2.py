'''x = 3 + 2 * 2
print(x)

y = "Lizz"
print(y[0:2])

p = '01234567'
print(p[::2]

t = ('1'+'2')
print(t)'''

'''tuple=(1,2,'somasree')
#print(tuple[-1])
tuple1=tuple+(3,4,'Baba')
print(sorted (tuple1))
#tuple.update(6,7)
#print(sorted(tuple1))
#tuple1Sorted = sorted(tuple1)
#print(tuple1Sorted)'''

'''u=(1,'Baba','Malay Mazumder',(100,3000))
print(u[3])
print(u[3][1])'''

'''u = [1, 'Baba', 'Malay Mazumder', (100, 3000)]
#u.extend(["Shishu"])
u[0]='65'
print(u)
del(u[0])
print(u)'''
'''name = "SomasreeMazumder"
x = name.split("     ")
print(x)'''
'''txt = "welcome to the jungle"

x = txt.split()

print(x)'''
'''B=["a","b","c"]
print(B[1:])'''

'''a=[1,2,3,4,5]
b=a
print(b)
a.append(4)
print(a)
print(b)
a.append(100)
print(a)
print(b)
b.append(200)
print(b)
print(a)
name_list = ['Baba', 'Maa', 'Riya', 'Papai', 'Babai', 'Baba', 'Maa']
print(name_list)
name_set = set(name_list)
print(name_set)
name_set.add("Malay")
print(name_set)
print(("Malay")in name_set)
print(("Shishu")in name_set)'''
'''a = {'1', '2', '3', '4', '5', '6', '7', '8', '9', }
b = {'6', '7', '8', '9', '10', '11', '12', '13', '14', '15'}
q = a.intersection(b)
print(q)'''
'''a={1,2,3,4,5,6,7,8,9}
b={6,7,8,9,10,11,12,13,14,15}
q = a.intersection(b)
print(q)
e=a.union(b)
print(e)
r=a.difference(b)
print(r)
o=a.symmetric_difference(b)
print(o)
h=a.difference_update(b)
print(h)
g=a.symmetric_difference_update(b)
print(g)'''

'''u={1:'A','B':2,'C':3,'D':4}
print(type(u))
print(u.get(1))
print(3 in(u))
print(u.keys)'''

'''u = int(input("Enter a number1:"))
v = int(input("Enter a number2:"))
if u != v:
    print("False")
else:
    print("True")'''
"""age=int(input("Enter the age:"))
if(age>18):
    print("You can enter")
elif(age>16):
    print("You can only go to the meat shop")
else:
    print("Move on")"""

'''dob=int(input("enter the year:"))
if(dob>1998)and(dob==2000):
    print("abc")
else:(print("pqr"))
'''

'''u=["Red","Blue","White","Yellow"]

for i in range(0,1):
    u[0]="lal"
    u[1]="nil"
    u[2]="sada"
    u[3]="holud"
    print(u)'''

'''square=["orange","orange","purple","blue"]
Newsquares=[]
i=0
while(square[i]=="orange"):
    Newsquares.append(square[i])
    i=i+1
    print(Newsquares)'''
'''A=[3,4,5]

for a in A:
    print(a)

a= 12
b= 14
def function(a):
    b=a+1
    print(a,"+1=",b)
    return(b)'''

'''a=[1,2,4,5,67,4,100,90]
sorted_a=sorted(a)
print(sorted_a)
'''


def x(n):
    if (n <= 1):
        return n
    else:
        return x(n - 1) + x(n - 2)

x(6)