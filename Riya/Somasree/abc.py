'''def x(n,m):
    if (m == 0):
        return n

    else:
        return (x(m,n%m))
a=x(100,2000)
print(a)'''

'''height = 100

bounce = 1

while (bounce <= 3):

    height = height * (3 / 5)

    bounce += 1

newheight = height

print(newheight)
'''

class P:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.h=100
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
    def damage(self,pts):
        self.health-=pts


