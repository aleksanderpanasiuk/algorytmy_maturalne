def horner(wspolczynniki, stopien, x):
    if stopien == 0:
        return wspolczynniki[0]

    return x * horner(wspolczynniki, stopien-1, x) + wspolczynniki[stopien]


wspolczynniki = [1, -1, 1, 1]
stopien = 3
x = 2

print(horner(wspolczynniki, stopien, x))
