'''1.print("Twinkle, twinkle, little star,\n    How I wonder what you are!
 \n                  Up above the world so high,"
      "\n                  Like a diamond in the sky. \nTwinkle, twinkle, little star,
      \n    How I wonder what you are ")'''

'''2.import sys
print("Python version")
print (sys.version)
#print("Version info")
#print (sys.version_info)'''
'''sys' module provides access to some variables
 used or maintained by the interpreter and to functions that interact strongly with the interpreter
 i.e. Information on the Python Interpreter. Like all the other modules, the sys module has to be imported with 
 the import statement,i.e. The sys module provides information about constants, functions and methods of 
 the Python interpreter'''

'''3.import datetime
now = datetime.datetime.now()
#print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))'''

'''4.from math import pi
r=float(input("Enter the radious of the circle:"))
#pi=3.144444
area=pi*r*r
print("Area of the circle is:",area)'''

'''u=input("Enter your name:")
print(u)
print(u[::-1])'''

'''5.fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ( lname + " " + fname)'''

'''6.values = (input("Input some comma seprated numbers : "))
x = values.split()
#tuple = tuple(list)
print('List : ',x)
#print('Tuple : ',tuple)
print(type(x))'''

'''7.filename = input("Input the Filename: ")
#x = filename.split(',')
x=filename
#print(x)
#print(repr(x))
print(repr(x[-1]))

#print ("The extension of the file is : " + repr(x[-1]))

'''

'''8.color_list =input('Enter the values:')
temp=color_list.split()
print(temp)
print(temp[0])'''

'''9.n = int(input('Enter the value of n:'))
# u=(n+(n*n)+(n*n*n))
# print(u)
n1 = int('%s' % n)
n2 = int('%s%s' % (n, n))
n3 = int('%s%s%s' % (n, n, n))
print(n1 + n2 + n3)'''

'''10.exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)'''

'''11.print(abs.__doc__)
u=round(3.999999)
print(u)
print(type(u))
print(round.__doc__)'''

'''12.import calendar

# date = '2021-05-21'
# datem = calendar.datetime(date, "%Y-%m-%d")
y = int(input("Input the year : "))
m = int(input("Input the month : "))
d = int(input("Input the day: "))
print(calendar.month(y, m))
print(calendar.month(m, d))
# print(calendar.date)'''

'''13.print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")'''

'''14.from  datetime import date
first_date=date(2022,2,3)
last_date=date(2022,8,8)
Baba=last_date-first_date
print(Baba.days)'''

'''15.from math import pi
r=float(input('Enter the value of radius:'))
volume=(4.0/3)*pi*r*r*r
print('The volume of the spehere is',volume)'''

'''16.u=int(input('Enter a value:'))
v=17
if u>v:
    print((u-v)**2)
else:
    print(abs(u-v))'''

'''u = int(input('Enter a number:'))
if u <= 100:
    print(False)
else:
    u <= 2000
    print(True)'''

'''ef f(n):
    if (n == 0 or n == 1 or n == 2):
        return 0
    if (n == 3):
        return 1
    else:
        return f(n - 1) + f(n - 2) + f(n - 3)'''

'''i=0
    sum=0
    while(i<100):
        sum=sum+i
        sum=i+sum
        i+=1
        #n-+2
    print(sum)'''


def x(n):
    if (n <= 1):
        return n
    else:
        return x(n - 1) + x(n - 2)

x(6)
'''for i in range(1, n):
        print(f(i))'''


