from cmath import cos, pi, e, sin, sqrt

j = sqrt(-1)
print("Donner la racine nième\nTel que Z^n = 1")
n = int(input("n = "))
print("Toutes les valeurs de solution de Z^" + str(n) + "= 1 sont :\n")
for k in range(0, n):
    alge = complex(cos((2*k*pi)/n), sin((2*k*pi)/n))
    print("z" + str(k+1) + " = cos(" + str(2*k) + "pi/" + str(n) + ") + i*sin(" + str(2*k) + "pi/" + str(n) + ")\n   = " + str(alge) + " \n")
    k += 1