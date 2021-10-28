def f(x):
    return (x**2) + x + 2

def calki(a, b, n):
    x = (b-a)/n
    s = 0.0
    srodek = a+(b-a)/(2.0*n)

    for i in range(n):
        s += f(srodek)
        srodek += x

    return s * x

print(calki(0, 10, 20))
