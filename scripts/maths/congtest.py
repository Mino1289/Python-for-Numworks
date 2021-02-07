from mathsup import cong

print("Donnez l'expression d'exposant n"+
"\nSans le n : 7 est 7^n"+
"\nEt 7^2n = 49^n soit 49")
exp = int(input(""))
print("Donnez le modulo :")
mod = int(input(""))
print("Résultats :")
for n in range(1, mod):
    print(str(exp) + "^" + str(n) + " iscong : " + str(cong(exp**n,mod)))
