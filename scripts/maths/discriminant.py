from mathsup import disc
from math import *


a = float(eval(input("a = ")))
b = float(eval(input("b = ")))
c = float(eval(input("c = ")))

d = disc(a, b, c)
print("\nd = " + str(d))
if (d > 0):
    print("x1 = (" + str(-round(b, 2)) + "-sqrt(" + str(round(d, 2)) + "))/(2*" +
          str(round(a, 2)) + ")\n= " + str(round((-b-sqrt(d))/(2*a), 2)))
    print("x2 = (" + str(-round(b, 2)) + "+sqrt(" + str(round(d, 2)) + "))/(2*" +
          str(round(a, 2)) + ")\n= " + str(round((-b+sqrt(d))/(2*a), 2)))
elif d == 0:
    print("x = " + str(-round(b, 2)) +
          "/(2*" + str(round(a, 2)) + ")\n= " + str(-b/(2*a)))
elif (d < 0):
    z1 = complex((-b/(2*a)), -(sqrt(-d))/(2*a))
    alge1 = round(z1.real, 2) + round(z1.imag, 2) * 1j
    print("z1 = (" + str(-round(b, 2)) + "-i*sqrt(" + str(-round(d, 2)) +
          "))/(2*" + str(round(a, 2)) + ")\n= " + str(alge1).replace("j", "i"))
    z2 = complex((-b/(2*a)), -(sqrt(-d))/(2*a))
    alge2 = round(z2.real, 2) + round(z2.imag, 2) * 1j
    print("z2 = (" + str(-round(b, 2)) + "+i*sqrt(" + str(-round(d, 2)) +
          "))/(2*" + str(round(a, 2)) + ")\n= " + str(alge2).replace("j", "i"))
