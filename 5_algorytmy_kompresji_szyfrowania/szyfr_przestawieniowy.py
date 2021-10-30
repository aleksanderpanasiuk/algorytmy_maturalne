def kodowanie(s):
    d = []

    if len(s)% 2 == 0:
        for i in range(0, len(s), 2):
            d.append(s[i+1])
            d.append(s[i])

    else:
        for i in range(0, len(s)-1, 2):
            d.append(s[i+1])
            d.append(s[i])
        d.append(s[-1])

    return "".join(d)

def dekodowanie(s):
    d = []

    if len(s)% 2 == 0:
        for i in range(0, len(s), 2):
            d.append(s[i+1])
            d.append(s[i])

    else:
        for i in range(0, len(s)-1, 2):
            d.append(s[i+1])
            d.append(s[i])
        d.append(s[-1])

    return "".join(d)

s = "abcdefg"

print(s)
print(kodowanie(s))
print(dekodowanie(kodowanie(s)))
