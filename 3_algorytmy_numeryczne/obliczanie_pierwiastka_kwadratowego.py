def pierwiastek(x):
    e = 0.000001
    a = 1.0
    b = x

    while abs(a - b) >= e:
        a = (a+b) / 2
        b = x / a

    return a


print(pierwiastek(3))
