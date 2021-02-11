def fact(x):
    """
    x = int\n\nReturn x!
    """
    r = 1
    for i in range(x):
        r *= (i + 1)
    return int(r)


def combi(n, k):
    """
    n, k = int\n\nReturn k among n.
    """
    x = fact(n) / (fact((n - k)) * fact(k))
    return int(x)


def arran(n, k):
    """
    n, k = int\n\nReturn arrangement of k objects among n.
    """
    if k > n:
        return None
    x = fact(n) / fact((n - k))
    return int(x)


def permut(n):
    """
    n = int\n\nReturn n!
    """
    return int(fact(n))


def disc(a, b, c):
    """
    a, b, c = int or float\n\nReturn b^2-4ac.
    """
    d = (b**2)-(4*a*c)
    return int(d)


def q(a, b):
    """
    a & b = int\n\nReturn q in a = b*q+r.
    """
    q = a//b
    r = a % b
    if r > b or r < 0:
        r -= b
        q += 1
    return int(q)


def r(a, b):
    """
    a & b = int\n\nReturn r in a = b*q+r.
    """
    r = a % b
    if r > b:
        r -= b
    elif r < 0:
        r += b
    return int(r)


def dive(a, b):
    """
    a & b = int\n\nReturn q & r in a = b*q+r.
    """
    qu = q(a, b)
    re = r(a, b)
    return qu, re


def iscong(a, b, n):
    """
    a, b, n = int\n\nReturn bool if a is congruent to b modulo n.
    """
    return bool(r(a-b,n) == 0)


def cong(a, n):
    """
    a, n = int\n\nReturn b & c the two closer to 0. Where a is congruent to b modulo n, and a is congruent to c modulo n.
    """
    b = r(a, n)
    if b == 0:
        return int(b)
    else:
        if b < 0 or n < 0:
            c = b+n
        else:
            c = b-n
    return b, c


def pgcd(a, b):
    """
    a, b = int\n\nReturn int, the greatest common divisor of a and b.
    """
    while (b > 0):
        re = r(a, b)
        a, b = b, re
    return a


def ppcm(a, b):
    """
    a, b = int\n\nReturn int, the least common divisor of a and b.
    """
    return q(a*b, pgcd(a, b))


def prime(n):
    """
    n = int\n\nReturn bool if n is a prime number.
    """
    for i in range(2, int(n**0.5)+1):
        if r(n,i) == 0:
            return False
    return True

def factor(n):
    """
    n = int\n\nReturn the prime factorization of n.
    """
    L = []
    div = 2
    while n > 1:
        if r(n,div) == 0:
            L.append(div)
            n /= div 
        else:
            div += 1
    return L
