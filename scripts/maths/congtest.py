from mathsup import cong,r


print("1: x en facteur\n2: n en exposant\n")
s = int(input(""))

if s == 1:
    #x en facteur
    print("Donnez l'expression\nde facteur x"+
    "\nSans le x : 7 est 7x")
    exp = int(input("= "))
    print("Donnez le modulo :")
    mod = int(input("mod = "))
    print("Résultats :")
    for x in range(1, max(exp+1,mod+1)):
        print(str(exp)+"*"+str(x)+ "="+ str(exp*x) +" est congru à : "+ str(r(exp*x, mod)) + " [" + str(mod)+"]")

elif s == 2:
    #n en exposant
    print("Donnez l'expression\nd'exposant n"+
    "\nSans le n : 7 est 7^n"+
    "\nEt 7^2n = 49^n soit 49")
    exp = int(input("= "))
    print("Donnez le modulo :")
    mod = int(input("mod = "))
    print("Résultats :")
    for n in range(1,max(exp+1, mod+1)):
        print(str(exp) + "^" + str(n) + " est congru à : " + str(r(exp**n,mod)) + " [" + str(mod)+"]")
else:
    print("t'es con ou quoi ?")
