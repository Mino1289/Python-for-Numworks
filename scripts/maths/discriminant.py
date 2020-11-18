from math import sqrt

def disc():
    print("Calcul du discriminant :\n Donnez a, b, c")
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))

    disc = b**2-4*a*c
    if disc == 0:
        x = -b/2*a
        print("Discriminant = " + str(disc) + "\n x =" + str(x))
    elif disc > 0:
        x1 = (-b + sqrt(disc))/2*a
        x2 = (-b - sqrt(disc))/2*a
        print("Discriminant > 0 (= " + str(disc) + ")\n x1 =" + str(x1) + "\n x2 =" + str(x2))
    else:
        print("Discriminant négatif (" + str(disc) + "), pas de valeur possible")
