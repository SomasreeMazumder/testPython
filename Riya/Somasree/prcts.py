'''#m = 10 ** 9 + 7
m=20

k = int(input("Enter a number of different colors (K): "))
n = int(input("Enter a number of balloons (N): "))

c = k
for i in range(1, n):
    c = (c * (k - 1)) % m
    #c = (c * (k - 1))
    print(c)

print(f"The number of ways to arrange {n} ballons of {k} colors is {c} (in modulo 10^9+7)")'''
def x(n):
    if n<1:
        return 0
    coins=[5,1,10,25]
    sum=0
    for i in coins:
        print("latest value of n before", n)
        print("latest value of i before", i)

        sum+=n//i
        print("number of coins",sum)

        print("***************************************")
        n=n%i
        print("Modulas remainder",n)

        if n==0:
          break
        print("latest value of n after", n)
        print("latest value of i after", i)
        print("#########################################")
    return sum
print(x(31))
u=31//25
#print(u)
