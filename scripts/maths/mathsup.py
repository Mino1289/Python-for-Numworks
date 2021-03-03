from random import uniform, random
from math import log2


def fact(x):
    r = 1
    for i in range(x):
        r *= (i + 1)
    return int(r)


def combi(n, k):
    if k > n:
        return None
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
    q, r = a//b, a % b
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
    qu, re = q(a, b), r(a, b)
    return qu, re


def iscong(a, b, n):
    return bool(r(a-b, n) == 0)


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
    a, b = abs(a), abs(b)
    while b > 0:
        re = r(a, b)
        a, b = b, re
    return a


def ppcm(a, b):
    a, b = abs(a), abs(b)
    return q(a*b, pgcd(a, b))


def prime(n):
    n = abs(n)
    for i in range(2, int(n**0.5)+1):
        if r(n, i) == 0:
            return False
    return True


def factor(n):
    div, L = 2, []
    while n > 1:
        if r(n, div) == 0:
            L.append(div)
            n /= div
        else:
            div += 1
    return L


def divint(n):
    n, L = abs(n), []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            L.append(i)
            L.append(n//i)
    return sorted(L)


def pi(n):
    c, t = 0, 0
    for _ in range(0, n+1):
        x, y = random(), random()
        if x**2 + y**2 <= 1:
            c += 1
        t += 1
    return 4*(c/t)


def rng(x):
    r = uniform(0.75, 1.25)
    return x*r


def coefb(a, b):
    if pgcd(a, b) != 1:
        return None
    L = []
    for u in range(-10, 10):
        for v in range(-10, 10):
            if a*u + b*v == 1:
                c = [u, v]
                L.append(c)
    return L


def tp(x, y, z):
    if (x*x) + (y*y) == z*z and x < y < z:
        return True
    else:
        return False


def int_bin(n):
    L = []
    for i in range(round(log2(n)), -1, -1):
        if (2**i) - n <= 0:
            L.append(1)
            n -= 2**i
        else:
            L.append(0)
    if L[0] == 0:
        L = L[1:]
    return joiner(L)


def bin_int(L):
    if type(L) != list:
        if type(L) == int:
            L = splitter(L)
    n = 0
    for i in range(len(L)):
        if L[i] == 1:
            n += 2**(len(L)-i)
    return int(n/2)


def joiner(L):
    if type(L) != list:
        return None
    s = str()
    for i in range(len(L)):
        s += str(L[i])
    return int(s)


def splitter(s):
    p = 0
    if type(s) != str and type(s) == int:
        p = 1
        s = str(s)
    L = []
    for c in s:
        L.append(c)
    if p == 1:
        for k in range(len(L)):
            L[k] = int(L[k])
    return L
