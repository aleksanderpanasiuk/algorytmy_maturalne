def przecinanie_odcinkow(a, b, c, d):
    max_x_ab = max(a[0], b[0])
    max_x_cd = max(c[0], d[0])
    min_x_ab = min(a[0], b[0])
    min_x_cd = min(c[0], d[0])

    max_y_ab = max(a[1], b[1])
    max_y_cd = max(c[1], d[1])
    min_y_ab = min(a[1], b[1])
    min_y_cd = min(c[1], d[1])

    x_ok = (max_x_ab >= min_x_cd and min_x_ab <= max_x_cd) or (max_x_cd >= min_x_ab and min_x_cd <= max_x_ab)
    y_ok = (max_x_ab >= min_x_cd and min_x_ab <= max_x_cd) or (max_x_cd >= min_x_ab and min_x_cd <= max_x_ab)

    return x_ok and y_ok



a = [0, -2]
b = [2, 2]
c = [-1, 2]
d = [3, 1]

print(przecinanie_odcinkow(a, b, c, d))
