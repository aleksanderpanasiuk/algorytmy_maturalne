def euklides(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


print(euklides(12, 18))
