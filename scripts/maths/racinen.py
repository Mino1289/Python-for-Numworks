from cmath import cos, pi, sin, sqrt

j = sqrt(-1)
print("Donner la racine nième\nTel que Z^n = 1")
n = int(input("n = "))
print("Toutes les valeurs de solution de\nZ^" + str(n) + " = 1 sont :\n")
for k in range(0, n):
    z = complex(cos((2*k*pi)/n),(sin((2*k*pi)/n)))
    alge = round(z.real, 1) + round(z.imag, 1) * 1j
    print("z" + str(k+1) + "= cos(" + str(2*k) + "pi/" + str(n) + ")+i*sin(" + str(2*k) + "pi/" + str(n) + ")\n   = " + str(alge).replace("j", "i") + " \n")
    k += 1
