def szybka_potega(a, n):
    w = 1

    while n > 0:
        if n%2 == 1:
            w *= a

        a *= a
        n = n // 2

    return w


print(szybka_potega(2, 10))
