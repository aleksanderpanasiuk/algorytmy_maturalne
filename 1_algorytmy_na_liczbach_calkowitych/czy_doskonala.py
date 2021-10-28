n = int(input("n: "))

def doskonala(n):
    dzielniki = []
    suma = 0
    
    for d in range(1, int((n/2)+1)):
        if n%d == 0:
            dzielniki.append(d)

    for l in dzielniki:
        suma += l

    return n == suma
    

print(doskonala(n))
    
