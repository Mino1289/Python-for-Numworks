def fact(x):
    """
    x = int\n\nReturn x!
    """
    r = 1
    for i in range(1, x + 1):
        r = r * i
    return int(r)


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
