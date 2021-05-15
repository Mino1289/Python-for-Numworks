from mathsup import factor

print("Donner un nombre\na factoriser en produit\nde facteur premiers.")
tt = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
n = int(input("n = "))
f = factor(n)
fa = n
for k in range(len(f)):
    fa = int(fa / f[k])
    # nombre d'espace en + 
    lenn = len(list(str(n)))
    lenfa = len(list(str(fa)))
    es = lenn - lenfa
    e = tt[0:es]
    print(str(int(fa)) + "".join(e) + "  |" + str(f[k]))
