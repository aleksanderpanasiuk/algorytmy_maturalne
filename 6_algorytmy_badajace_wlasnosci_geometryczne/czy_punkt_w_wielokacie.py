def iloczyn_wektorowy(a, b, c):
    x1 = c[0] - a[0]
    y1 = c[1] - a[1]
    x2 = b[0] - a[0]
    y2 = b[1] - a[1]

    return x1*y2 - x2*y1


def punkt_odcinek(a, b, c):
    x_ok = c[0] >= min(a[0], b[0]) and c[0] <= max(a[0], b[0])
    y_ok = c[1] >= min(a[1], b[1]) and c[1] <= max(a[1], b[1])
    return x_ok and y_ok


def przecinanie_odcinkow(a, b, c, d):
    v1 = iloczyn_wektorowy(c, d, a)
    v2 = iloczyn_wektorowy(c, d, b)
    v3 = iloczyn_wektorowy(a, b, c)
    v4 = iloczyn_wektorowy(a, b, d)

    if ((v1>0 and v2<0) or (v1<0 and v2>0)) and ((v3>0 and v4<0) or (v3<0 and v4>0)):
        return True, False

    if v1 == 0 and punkt_odcinek(c, d, a):
        return True, True
    if v2 == 0 and punkt_odcinek(c, d, b):
        return True, True
    if v3 == 0 and punkt_odcinek(a, b, c):
        return True, True
    if v4 == 0 and punkt_odcinek(a, b, d):
        return True, True

    return False, False


def punkt_wielokacie(wielokat, p):
    max_odl = 0
    
    for punkt in wielokat:
        max_odl = (((p[0]-punkt[0])**2)+((p[1]-punkt[1])**2))**(1/2)

    max_odl *= 2
    max_odl = int(max_odl)+1
    p2 = [p[0], p[1]+max_odl]
    punkty = [False] * len(wielokat)
    liczba_przeciec = 0

    for i in range(len(wielokat)):
        przeciecie = przecinanie_odcinkow(p, p2, wielokat[i], wielokat[(i+1)%len(wielokat)])

        if przeciecie[0] and (punkty[i] == False and punkty[(i+1)%len(wielokat)] == False):
            liczba_przeciec += 1

        if przeciecie[1]:
            if wielokat[i][0] == p[0]:
                punkty[i] = True
            else:
                punkty[(i+1)%len(wielokat)] = True

    if liczba_przeciec%2 == 1:
        return True
    else:
        return False

    return 0


a = [-2, -2]
b = [-5, -4]
c = [-5, 2]
d = [2, 2]
e = [2, -5]

wielokat = [a, b, c, d, e]
p = [-2, -1]
r = [-2, -3]

print(punkt_wielokacie(wielokat, p))
print(punkt_wielokacie(wielokat, r))
