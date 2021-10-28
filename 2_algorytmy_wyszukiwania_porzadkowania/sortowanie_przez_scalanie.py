def merge_sort(tab):
    if len(tab) > 1:
        s = len(tab) // 2
        l = tab[:s]
        p = tab[s:]
        merge_sort(l)
        merge_sort(p)

        i = j = k = 0

        while i < len(l) and j < len(p):
            if l[i] < p[j]:
                tab[k] = l[i]
                i += 1
            else:
                tab[k] = p[j]
                j += 1
            k += 1

        while i < len(l):
            tab[k] = l[i]
            i += 1
            k += 1

        while j < len(p):
            tab[k] = p[j]
            j += 1
            k += 1

    return tab



tab = [12, 1, 0, 5, 21, 8, 2, 3, 21]

print(merge_sort(tab))
