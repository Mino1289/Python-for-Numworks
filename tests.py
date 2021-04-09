from scripts.maths.mathsup import arran, bin_int, combi, cong, congi, dioph, disc, dive, divint, fact, factor, int_bin, iscong, pgcd, ppcm, prime, permut, r, q, tp

# test de toutes les fonctions
if arran(10, 5) != 30240:
    print("Erreur dans arran(n,k)")
if bin_int(11101111001100000) != 122464:
    print("Erreur dans bin_int(n)")
if combi(10, 5) != 252:
    print("Erreur dans combi(n,k)")
if cong(55, -3) != (1, -2):
    print("Erreur dans cong(a,n)")
if congi(55, -3) != 1:
    print("Erreur dans congi(a,n)")
if dioph(21, 32) != (-3, 2):
    print("Erreur dans dioph(a,b)")
if dioph(21, 32, 4) != (20, -13):
    print("Erreur dans dioph(a,b,c)")
if dioph(12, 19, 5, 1) != [(-17, 11), (2, -1), (21, -13)]:
    print("Erreur dans dioph(a,b,c,l)")
if disc(5, -2, 8) != -156 or disc(5, 6, -8) != 196:
    print("Erreur dans disc(a,b,c)")
if dive(51, 6) != (8, 3):
    print("Erreur dans dive(a,n)")
if divint(296) != [1, 2, 4, 8, 37, 74, 148, 296]:
    print("Erreur dans divint(n)")
if fact(10) != permut(10) or fact(10) != 3628800:
    print("Erreur dans fact(n) et ou permut(n)")
if factor(96) != [2, 2, 2, 2, 2, 3]:
    print("Erreur dans factor(n)")
if int_bin(122464) != 11101111001100000:
    print("Erreur dans int_bin(n)")
if not iscong(25, 6, 1):
    print("Erreur dans iscong(a,b,n)")
if pgcd(15, 12) != 3:
    print("Erreur dans pgcd(a,b)")
if ppcm(12, 16) != 48:
    print("Erreur dans ppcm(a,b)")
if not prime(37):
    print("Erreur dans prime(n)")
if q(12, -5) != -2:
    print("Erreur dans q(a,n)")
if r(12, -5) != 2:
    print("Erreur dans r(a,b)")
if not tp(3, 4, 5):
    print("Erreur dans tp(x,y,z)")
print("Fin du test, si il y a des erreurs, elles sont au dessus")
