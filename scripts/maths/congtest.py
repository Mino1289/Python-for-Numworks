from mathsup import cong,r

print("Donnez l'expression\nd'exposant n"+
"\nSans le n : 7 est 7^n"+
"\nEt 7^2n = 49^n soit 49")
exp = int(input("exp = "))
print("Donnez le modulo :")
mod = int(input("mod = "))
print("Résultats :")
for n in range(1,min(exp+1, mod+1)):
    print(str(exp) + "^" + str(n) + " est congru à : " + str(r(exp**n,mod)) + " [" + str(mod)+"]")
