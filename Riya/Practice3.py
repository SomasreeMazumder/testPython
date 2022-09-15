

p = int(input('The principle value'))
r = int(input('The interest rate'))
t = int(input('The time period'))
Amount = p * (pow((1 + r / 100), t))
si = (p * r * t) / 100
print("The simple interest is", si)
ci = Amount-p
print("The compound interest is",ci)



