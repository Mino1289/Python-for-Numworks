def fact(x):
    """
    x = int\n\nReturn x!
    """
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


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
