def bubble_sort(tab):
    n = len(tab)

    for i in range(n):
        for j in range(1, n-i):
            if tab[j-1] > tab[j]:
                tab[j-1], tab[j] = tab[j], tab[j-1]

    return tab

tab = [12, 1, 0, 5, 21, 8, 2, 3, 21]

print(bubble_sort(tab))
