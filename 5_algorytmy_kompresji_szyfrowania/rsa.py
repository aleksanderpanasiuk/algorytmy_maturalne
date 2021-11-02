def euklides(a, b):
    if b != 0:
        return euklides(b, a%b)
    return a


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


def generowanie_kluczy(p, q):
    fi = (p-1) * (q-1)
    n = p * q
    e = 2

    while euklides(fi, e) != 1 or rozszerzony_euklides(e, fi) == "nie ma":
        e += 1

    d = rozszerzony_euklides(e, fi)

    return [[e, n], [d, n]]


def szyfrowanie(klucz_publiczny, waidomosc):
    return (wiadomosc ** klucz_publiczny[0]) % klucz_publiczny[1]


def deszyfrowanie(klucz_prywatny, wiadomosc):
    return (wiadomosc ** klucz_prywatny[0]) % klucz_prywatny[1]

    
klucze = generowanie_kluczy(13, 11) # klucze[0] - publiczny, klucze[1] - prywatny
wiadomosc = 123
zaszyfrowana_wiadomosc = szyfrowanie(klucze[0], wiadomosc)
odszyfrowana_wiadomosc = deszyfrowanie(klucze[1], zaszyfrowana_wiadomosc)

print("klucz publiczny:", klucze[0])
print("klucz prywatny:", klucze[1])
print("wiadomosc:", wiadomosc)
print("zaszyfrowana wiadomosc:", zaszyfrowana_wiadomosc)
print("odszyfrowana wiadomosc:", odszyfrowana_wiadomosc)
