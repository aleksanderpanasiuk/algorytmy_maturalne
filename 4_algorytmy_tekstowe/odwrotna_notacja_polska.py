onp = input().split()
wynik = []

for i in range(len(onp)):
    if ord(onp[i]) >= 48 and ord(onp[i]) <= 58:
        onp[i] = int(onp[i])
        wynik.append(onp[i])
        
    elif ord(onp[i]) == 45:
        wynik.append(- wynik.pop(-1) + wynik.pop(-1))
        
    elif ord(onp[i]) == 43:
         wynik.append(wynik.pop(-1) + wynik.pop(-1))

    elif ord(onp[i]) == 42:
         wynik.append(wynik.pop(-1) * wynik.pop(-1))

    elif ord(onp[i]) == 47:
         wynik.append((1 / wynik.pop(-1)) * wynik.pop(-1))
        
    else:
        print(ord(onp[i]))


print(wynik[0])
