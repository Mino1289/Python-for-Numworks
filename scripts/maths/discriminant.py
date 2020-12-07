from mathsup import disc
from cmath import sqrt


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = disc(a, b, c)
print(f"\n d = {d}")
if (d > 0):
    print("x1 = (" + str(-b) + "-sqrt(" + str(d) + "))/(2*" + str(a) + ")\n= " + str((-b-sqrt(d))/(2*a)))
    print("x2 = (" + str(-b) + "+sqrt(" + str(d) + "))/(2*" + str(a) + ")\n= " + str((-b+sqrt(d))/(2*a)))
elif d==0:
    print("x = " + str(-b) + "/(2*" + str(a) + ")\n= " + str(-b/(2*a)))
elif (d < 0):
    z1 = complex((-b/(2*a)), -(sqrt(-d))/(2*a))
    alge1 = round(z1.real, 1) + round(z1.imag, 1) * 1j
    print("z1 = (" + str(-b) + "-i*sqrt(" + str(-d) + "))/(2*" + str(a) + ")\n= " + str(alge1).replace("j", "i"))
    z2 = complex((-b/(2*a)), -(sqrt(-d))/(2*a))
    alge2 = round(z2.real, 1) + round(z2.imag, 1) * 1j
    print("z2 = (" + str(-b) + "+i*sqrt(" + str(-d) + "))/(2*" + str(a) + ")\n= " + str(alge2).replace("j", "i"))
