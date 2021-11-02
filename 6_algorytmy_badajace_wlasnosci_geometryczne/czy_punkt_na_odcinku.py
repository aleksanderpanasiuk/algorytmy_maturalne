def punkt_odcinek(a, b, c):
    x_ok = c[0] >= min(a[0], b[0]) and c[0] <= max(a[0], b[0])
    y_ok = c[1] >= min(a[1], b[1]) and c[1] <= max(a[1], b[1])
    return x_ok and y_ok


a = [-5, -5]
b = [5, 5]
c = [0, 0]

print(punkt_odcinek(a, b, c))
