def insert_sort(tab):
    for i in range(len(tab)):
        pom = tab[i]
        j = i-1

        while j >= 0 and tab[j] > pom:
            tab[j+1] = tab[j]
            j -= 1

        tab[j+1] = pom

    return tab


tab = [12, 1, 0, 5, 21, 8, 2, 3, 21]

print(insert_sort(tab))
