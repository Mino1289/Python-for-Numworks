
from random import random, uniform
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
    d = (b**2) - (4*a*c)
    return d


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
    return r(a - b, n) == 0


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


def congi(a, n):
    (b, c) = cong(a, n)
    if abs(b) >= abs(c):
        return c
    else:
        return b


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
    if n == 1:
        return False
    if n % 2 == 0:
        if n == 2:
            return True
        return False
    for i in range(3, round(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def factor(n):
    div, L = 2, []
    if prime(n):
        return [n]
    while n > 1:
        if n % div == 0:
            L.append(div)
            n /= div
        else:
            div += 1
    return L


def divint(n):
    n, L = abs(n), []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            L.append(i)
            L.append(n//i)

    return sorted(k for k in L if not(L.count(k) > 1))


def nbdiv(n):
    f, nbr, L = factor(n), 1, []
    for k in range(len(f)):
        if L.count(f[k]) == 0:
            L.append(f[k])

    for k in L:
        nbr *= len(divint(k**f.count(k)))
    return nbr


def nprime(n):
    return [k for k in range(n) if prime(k)]


def sdiv(n):
    return divint(n)[1]


def gdiv(n):
    d = divint(n)
    return d[len(d)-2]


def sprdiv(n):
    return factor(n)[1]


def gprdiv(n):
    f = factor(n)
    return f[len(f)-1]


def pi(n):
    c, t = 0, 0
    for _ in range(0, n + 1):
        x, y = random(), random()
        if x**2 + y**2 <= 1:
            c += 1
        t += 1
    return 4*(c/t)


def rng(x):
    r = uniform(0.75, 1.25)
    return x*r


def dioph(a, b, c=1, l=0):
    if c % pgcd(a, b) != 0:
        return None
    L = []
    r = abs(a) + abs(b)
    for u in range(-r, r):
        for v in range(-r, r):
            if (a*u) + (b*v) == c:
                L.append((u, v))
    if l:
        return L
    else:
        return L[int(len(L)/2)]


def tp(x, y, z):
    return (x*x) + (y*y) == z*z and x < y < z


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
        if isinstance(L, int):
            L = splitter(L)
    n = 0
    for i in range(len(L)):
        if L[i] == 1:
            n += 2**(len(L)-i)
    return int(n/2)


def joiner(L):
    if not isinstance(L, list):
        return None
    return int("".join(str(L[i]) for i in range(len(L))))


def splitter(s):
    p = 0
    if not isinstance(s, str) and isinstance(s, int):
        p = 1
        s = str(s)
    L = [c for c in s]

    if p == 1:
        for k in range(len(L)):
            L[k] = int(L[k])
    return L
