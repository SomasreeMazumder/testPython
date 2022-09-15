'''import numpy


def s():

    x = numpy.sqrt(9)
    y=9**(1/2)
    print(x,y)

s()'''
#  00000(700)

'''fo = open("foo.txt", "rw+")
print
"Name of the file:", fo.name

for index in range(5):
    line = fo.next()
    print
    "Line No %d-$s" % (index, line)
fo.close()'''

'''def u(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False

print(u([1, 2, 3, 4, 5]))
print(u([2, 2, 5, 9, 3, 7, 8]))
'''

'''import random
list = ['a','e','i','o','u']
random.shuffle(list)
print(''.join(list))'''

'''import random

number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
print("Original list : ", number_list)
random.shuffle(number_list)
print("List after shuffle : ", number_list)
'''


def remove_nums(int_list):
    position = 2
    idx = 0
    len_list = (len(int_list))
    # print(len_list)
    while len_list > 0:
        idx = (position + idx) % len_list
        y=int_list[idx]
        print(int_list,"lenghth",len_list,"index",idx)
        print("*******")
        int_list.pop(idx)
        print(int_list,y,"idx",idx)
        len_list -= 1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

remove_nums(nums)
xx=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(xx))
x=4%8
print("xxxx",x)
