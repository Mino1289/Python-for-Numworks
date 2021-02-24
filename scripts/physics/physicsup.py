def pvnrt(P, V, n, T):
    R = 8.31
    if type(P) == str:
        return (n*R*T)/V
    elif type(V) == str:
        return (n*R*T)/P
    elif type(n) == str:
        return(P*V)/(R*T)
    elif type(T) == str:
        return (P*V)/(n*R)
    else:
        return bool(P*V == n*R*T)


def rho(m, V, p):
    if type(m) == str:
        return p*V
    elif type(V) == str:
        return m/p
    elif type(p) == str:
        return m/V
    else:
        return bool(p == m/V)
