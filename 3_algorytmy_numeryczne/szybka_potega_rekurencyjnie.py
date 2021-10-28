def szybka_potega(a, n):
    if n == 0:
        return 1
    if n%2 == 1:
        return a * szybka_potega(a, n-1)

    w = szybka_potega(a, n/2)

    return w*w


print(szybka_potega(2, 10))
