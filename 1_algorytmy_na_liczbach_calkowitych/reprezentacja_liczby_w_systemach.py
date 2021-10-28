n = int(input("n: "))
p = int(input("p: "))

def zamiana(n, p):
    szesc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    
    r = 0
    wynik = ""

    while n >= 1:
        r = n%p
        n = n // p
        wynik = str(szesc[r]) + wynik

    return wynik

print(zamiana(n, p))
