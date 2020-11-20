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
