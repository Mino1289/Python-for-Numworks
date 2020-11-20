from MathSup import disc
from math import sqrt


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = disc(a, b, c)
if (d > 0):
    print("x1 = (-" + str(b) + "-sqrt(" + str(d) + "))/(2*" + str(a) + ")\n= " + str((-b-sqrt(d))/(2*a)))
    print("x2 = (-" + str(b) + "+sqrt(" + str(d) + "))/(2*" + str(a) + ")\n= " + str((-b+sqrt(d))/(2*a)))
elif d==0:
    print("x = -" + str(b) + "/(2*" + str(a) + ")\n= " + str(-b/(2*a)))
elif (d < 0):
    print("z1 = (-" + str(b) + "-i*sqrt(-(" + str(d) + ")))/(2*" + str(a) + ")\n= " + str((-b-sqrt(-d))/(2*a)))
    print("z2 = (-" + str(b) + "-i*sqrt(-(" + str(d) + ")))/(2*" + str(a) + ")\n= " + str((-b+sqrt(-d))/(2*a)))
