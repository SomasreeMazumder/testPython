

'''H = set("Hacker")
R = set("Rank")
u=R.symmetric_difference_update(H)
print (u)'''


'''A={1,2,3,4,5,6}
B={4,5,6,2,7,8}
x=A.symmetric_difference_update(B)
#x=A.symmetric_difference(B)
print(x)'''
A={1,2,3,4,5,6}
B={3,4,5,6,7,8}
#x=A.difference_update(B)
y=A.symmetric_difference_update(B)
print(y)

'''A={'r','g','b'}
B={'y','r','o'}
y=A.symmetric_difference(B)
u=A.symmetric_difference_update(B)
print(y)
print(u)'''
