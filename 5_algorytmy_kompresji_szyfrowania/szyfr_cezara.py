klucz = 3
s = "AabcdefzZ"
d= []

for i in range(len(s)):
    if ord(s[i]) >= 97:
        d.append(chr((ord(s[i])-97 + klucz) % 26 + 97))
    else:
        d.append(chr((ord(s[i])-65 + klucz) % 26 + 65))


print("".join(d))
