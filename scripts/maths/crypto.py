from mathsup import r

def code(L,j):
    Lettres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    C = []
    def f_y(x,j):
        return r(11*x+j,26)
    for k in L:
        C.append(Lettres[f_y(Lettres.index(k.upper()),j)])
    return "".join(C)

def decode(L,j):
    Lettres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    D = []
    def f_x(y,j):
        return r(19*y+(26-r(19*j,26)),26)
    for k in L:
        D.append(Lettres[f_x(Lettres.index(k.upper()),j)])
    return "".join(D)
    
def l(n):
    return list(n)

print("Coder un message : 1")
print("Décoder un message : 2")
t = int(input("Codage ou Décodage ?\n"))

if t == 1:
    # codage
    j = int(input("Quel jour sommes nous ?\n"))
    print("Donnez votre message :")
    mot = list(input("").upper())
    co = code(mot,j)
    print(co)
elif t ==2:
    # décodage
    j = int(input("Quel jour sommes nous ?\n"))
    print("Donnez votre message :")
    mot = list(input("").upper())
    dco = decode(mot,j)
    print(dco)

else:
    print("t con")
