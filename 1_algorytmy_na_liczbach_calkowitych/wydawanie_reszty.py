NOMINALY = [500, 200, 100, 50, 20, 10, 5, 2, 1]
NOMINALY = sorted(NOMINALY, reverse=True)
monety = []
reszta = 2137
k = 0
max_nominal = NOMINALY[0]

while reszta:
    if max_nominal <= reszta:
        reszta -= max_nominal
        monety.append(max_nominal)
    else:
        k += 1
        max_nominal = NOMINALY[k]

print(monety)
