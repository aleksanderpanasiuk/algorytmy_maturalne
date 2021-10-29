klucz = 3
s = "AabcdefzZ"

def kodowanie(s, k):
    d = []

    for i in range(len(s)):
        if ord(s[i]) >= 97:
            d.append(chr((ord(s[i])-97 + k) % 26 + 97))
        else:
            d.append(chr((ord(s[i])-65 + k) % 26 + 65))

    return "".join(d)


def dekodowanie(s, k):
    d = []

    for i in range(len(s)):
        if ord(s[i]) >= 97:
            d.append(chr((ord(s[i])-97 - k) % 26 + 97))
        else:
            d.append(chr((ord(s[i])-65 - k) % 26 + 65))

    return "".join(d)


print(s)
print(kodowanie(s, klucz))
print(dekodowanie(kodowanie(s, klucz), klucz))
