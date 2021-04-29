from mathsup import r, q, pgcd

print("PGCD de :")
a, b = abs(int(input("a = "))), abs(int(input("b = ")))
A, B = a, b
while b > 0:
    re = r(a, b)
    print("{} = {} * {} + {}".format(a, b, q(a, b), r(a, b)))
    a, b = b, re

print("\nPGCD({},{}) = {}".format(A, B, pgcd(A, B)))
