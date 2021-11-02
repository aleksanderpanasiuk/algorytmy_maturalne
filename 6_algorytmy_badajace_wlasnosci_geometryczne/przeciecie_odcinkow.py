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
        return True

    if v1 == 0 and sprawdz(C, D, A):
        return True
    if v2 == 0 and sprawdz(C, D, B):
        return True
    if v3 == 0 and sprawdz(A, B, C):
        return True
    if v4 == 0 and sprawdz(A, B, D):
        return True

    return False



a = [-5, -4]
b = [-2, -3]
c = [-2, -2]
d = [2, -5]

print(przecinanie_odcinkow(a, b, c, d))
