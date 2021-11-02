def rozszerzony_euklides(a, b):
    u = 1
    x = 0
    w = a
    z = b

    while w > 0:
        if w < z:
            q = u
            u = x
            x = q
            q = w
            w = z
            z = q
        q = w // z
        u -= q * x
        w -= q * z

    if z == 1:
        if x < 0:
            x += b
        return x

    return "nie ma"

print(rozszerzony_euklides(7, 120))
