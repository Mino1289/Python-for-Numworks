from mathsup import disc
from math import sqrt


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = disc(a, b, c)
if (d > 0):
    print("x1 = ", (-b-sqrt(d))/(2*a))
    print("x2 = ", (-b+sqrt(d))/(2*a))
elif d==0:
    print("x = ", -b/(2*a))
elif (d < 0):
    print("z1 = ", (-b-sqrt(-d))/(2*a))
    print("z2 = ", (-b+sqrt(-d))/(2*a))
