n = int(input("n: "))

def rozklad(n):
    k = 2
    czynniki = []

    while 1 < n and k < n**1/2:
        while n%k == 0:
            czynniki.append(int(k))
            n /= k
        k += 1

    if n > 1:
        czynniki.append(int(n))

    return czynniki


print(rozklad(n))
