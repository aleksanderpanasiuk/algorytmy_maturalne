tab = [12, 1, 0, 5, 21, 8, 2, 3, 21]
tab_m, tab_M = tab[0], tab[0]

for i in tab:
    tab_m = min(tab_m, i)
    tab_M = max(tab_M, i)


print(tab_m, tab_M)
