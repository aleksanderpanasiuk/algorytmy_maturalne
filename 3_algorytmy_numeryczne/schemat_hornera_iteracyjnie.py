def horner(wspolczynniki, stopien, x):
    wynik = wspolczynniki[0]

    for i in range(1, stopien+1):
        wynik = wynik*x + wspolczynniki[i]

    return wynik
    
wspolczynniki = [1, -1, 1, 1]
stopien = 3
x = 2

print(horner(wspolczynniki, stopien, x))
