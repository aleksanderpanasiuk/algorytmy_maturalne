tab = [12, 1, 0, 5, 21, 8, 2, 3, 21]
zbior_m = []
zbior_M = []
tab_m, tab_M = tab[0], tab[0]

if len(tab) % 2 == 0:
    for i in range(0, len(tab), 2):
        if tab[i] < tab[i+1]:
            zbior_m.append(tab[i])
            zbior_M.append(tab[i+1])
        else:
            zbior_m.append(tab[i+1])
            zbior_M.append(tab[i])
else:
    for i in range(0, len(tab)-1, 2):
        if tab[i] < tab[i+1]:
            zbior_m.append(tab[i])
            zbior_M.append(tab[i+1])
        else:
            zbior_m.append(tab[i+1])
            zbior_M.append(tab[i])
            
    zbior_m.append(tab[-1])
    zbior_M.append(tab[-1])


for i in zbior_m:
    tab_m = min(tab_m, i)
for i in zbior_M:
    tab_M = max(tab_M, i)


print(tab_m, tab_M)
