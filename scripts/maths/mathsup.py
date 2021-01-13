def fact(x):
    """
    x = int\n\nReturn x!
    """
    r = 1
    for i in range(x):
        r = r * (i + 1)
    return r


def combi(n, k):
    """
    n, k = int\n\nReturn k among n
    """
    x = fact(n) / (fact((n - k)) * fact(k))
    return int(x)


def arran(n, k):
    """
    n, k = int\n\nReturn arrangement of k objects among n
    """
    if k > n:
        return
    x = fact(n) / fact((n - k))
    return int(x)

def permut(n):
    """
    n = int\n\nReturn n!
    """
    x = fact(n)
    return int(x)

def disc(a, b, c):
    """
    a, b, c = int or float\n\nReturn b^2-4ac
    """
    d = (b**2)-(4*a*c)
    return int(d)

def dive(a,b):
    """
    a & b = int\n\nReturn q & r in a = b*q+r
    """
    q = a//b
    r = a%b
    if r > b or r < 0:
        r -= b
        q += 1
    return q, r

def iscong(a,b,n):
    """
    a, b, n = int\n\nReturn bool if a is congruent to b modulo n
    """
    return (a-b)%n == 0
