''''numbers = []
for num in range(100):
    num=str(num).zfill(3)
print(num)
numbers.append(num)
'''

'''n=int(input('enter a number'))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print('reverse of the number',reverse)'''

'''n = int(input('enter a number: '))
temp=n
reverse = 0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if reverse==temp:
    print('the number is palindron number')

else: print('The number is not palindron number')
'''
'''u='riya'
v='india'
#riinydaia

def merge(s1,s2):
    result=[]
    for i in range(len(s1)) and range(len(s2)):
            if(i< len(s1)):
               result.append(s1[i])
            if(i<len(s2)):
                result.append(s2[i])
    print(result)
    print(''.join(result))
merge(u,v)'''

'''import collections
import pprint

file_input = input('File Name: ')
with open(file_input, 'r') as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)
print(value)'''

'''import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)
for m in installed_packages_list:
    print(m)
    print(pkg_resources)'''

