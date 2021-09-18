from scripts.maths.mathsup import arran, combi, cong, congi, dioph, disc, dive, divint, fact, factor, iscong, pgcd, ppcm, prime, permut, r, q, tp, nprime, sdiv, gdiv, sprdiv, gprdiv, divcom, invmod, egcd, lstbin, max2int, based

# test de toutes les fonctions
e = 0
print("Test pour mathsup.py...")
if arran(10, 5) != 30240:
    e += 1
    print("Erreur dans arran(n,k)")
if combi(10, 5) != 252:
    e += 1
    print("Erreur dans combi(n,k)")
if cong(55, -3) != (1, -2):
    e += 1
    print("Erreur dans cong(a,n)")
if congi(55, -3) != 1:
    e += 1
    print("Erreur dans congi(a,n)")
if dioph(21, 32) != (-3, 2):
    e += 1
    print("Erreur dans dioph(a,b)")
if dioph(21, 32, 4) != (20, -13):
    e += 1
    print("Erreur dans dioph(a,b,c)")
if dioph(12, 19, 5, 1) != [(-17, 11), (2, -1), (21, -13)]:
    e += 1
    print("Erreur dans dioph(a,b,c,l)")
if disc(5, -2, 8) != -156 or disc(5, 6, -8) != 196:
    e += 1
    print("Erreur dans disc(a,b,c)")
if dive(51, 6) != (8, 3):
    e += 1
    print("Erreur dans dive(a,n)")
if divint(296) != [1, 2, 4, 8, 37, 74, 148, 296]:
    e += 1
    print("Erreur dans divint(n)")
if fact(10) != permut(10) or fact(10) != 3628800:
    e += 1
    print("Erreur dans fact(n) et ou permut(n)")
if factor(96) != [2, 2, 2, 2, 2, 3]:
    e += 1
    print("Erreur dans factor(n)")
if not iscong(25, 6, 1):
    e += 1
    print("Erreur dans iscong(a,b,n)")
if pgcd(15, 12) != 3:
    e += 1
    print("Erreur dans pgcd(a,b)")
if ppcm(12, 16) != 48:
    e += 1
    print("Erreur dans ppcm(a,b)")
if not prime(37):
    e += 1
    print("Erreur dans prime(n)")
if q(12, -5) != -2:
    e += 1
    print("Erreur dans q(a,n)")
if r(12, -5) != 2:
    e += 1
    print("Erreur dans r(a,b)")
if not tp(3, 4, 5):
    e += 1
    print("Erreur dans tp(x,y,z)")
if nprime(100) != [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
    e += 1
    print("Erreur dans nprime(n)")
if sdiv(10808) != 2:
    e += 1
    print("Erreur dans sdiv(n)")
if gdiv(10808) != 5404:
    e += 1
    print("Erreur dans gdiv(n)")
if sprdiv(10808) != 2:
    e += 1
    print("Erreur dans sprdiv(n)")
if gprdiv(10808) != 193:
    e += 1
    print("Erreur dans gprdiv(n)")
if divcom(18, 24) != [1, 2, 3, 6]:
    e += 1
    print("Erreur dans divcom(a,b)")
if invmod(91, 1487) != 719:
    e += 1
    print("Erreur dans invmod(a,b)")
if egcd(86, 977) != (1, -284, 25):
    e += 1
    print("Erreur dans egcd(a,b)")
if max2int(-32, 4) != max(-32, 4):
    e += 1
    print("Erreur dans max2int(a,b)")
if lstbin(456) != [256, 128, 64, 8]:
    e += 1
    print("Erreur dans lstbin(a,b)")
if based("654",7) != "333":
    e += 1
    print("Erreur dans based(n,base)")
print("Fin du test avec {} erreurs.".format(e))
