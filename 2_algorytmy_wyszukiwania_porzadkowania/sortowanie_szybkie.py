def quick_sort(tab, p, k):
    i, j, m = p, k, tab[int((p+k)/2)]

    while i <= j:
        while tab[i] < m:
            i += 1
        while tab[j] > m:
            j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1

    if p < j:
        quick_sort(tab, p, j)
    if i < k:
        quick_sort(tab, i, k)

    return tab


tab = [12, 1, 0, 5, 21, 8, 2, 3, 21]

print(quick_sort(tab, 0, len(tab)-1))




