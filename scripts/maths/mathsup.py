from random import uniform, random

def fact(x):
    r = 1
    for i in range(x):
        r *= (i + 1)
    return int(r)


def combi(n, k):
    x = fact(n) / (fact((n - k)) * fact(k))
    return int(x)


def arran(n, k):
    if k > n:
        return None
    x = fact(n) / fact((n - k))
    return int(x)


def permut(n):
    return int(fact(n))


def disc(a, b, c):
    d = (b**2)-(4*a*c)
    return int(d)


def q(a, b):
    q = a//b
    r = a % b
    if r > b or r < 0:
        r -= b
        q += 1
    return int(q)


def r(a, b):
    r = a % b
    if r > b:
        r -= b
    elif r < 0:
        r += b
    return int(r)


def dive(a, b):
    qu = q(a, b)
    re = r(a, b)
    return qu, re


def iscong(a, b, n):
    return bool(r(a-b,n) == 0)


def cong(a, n):
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
    while (b > 0):
        re = r(a, b)
        a, b = b, re
    return a


def ppcm(a, b):
    return q(a*b, pgcd(a, b))


def prime(n):
    for i in range(2, int(n**0.5)+1):
        if r(n,i) == 0:
            return False
    return True

def factor(n):
    L = []
    div = 2
    while n > 1:
        if r(n,div) == 0:
            L.append(div)
            n /= div 
        else:
            div += 1
    return L

def divint(n):
    n, L, x = abs(n), [], 1
    while x <= n:
        if r(n,x) == 0:
            L.append(x)
        x += 1
    return L

def pi(n):
    pts_c, pts_tt = 0, 0

    for _ in range(0, n+1):
        x, y = uniform(0, 1), uniform(0, 1)
        if x**2 + y**2 <= 1:
            pts_c += 1
        pts_tt += 1
    return 4*(pts_c/pts_tt)


def rng(x):
    r = random()
    r /= 2
    r += 0.75

    return x*r
