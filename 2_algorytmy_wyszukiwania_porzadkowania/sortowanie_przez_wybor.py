def selection_sort(tab):
    for i in range(len(tab)-1):
        min_poz = i
        
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min_poz]:
                min_poz = j
                
        tab[i], tab[min_poz] = tab[min_poz], tab[i]

    return tab


tab = [12, 1, 0, 5, 21, 8, 2, 3, 21]

print(selection_sort(tab))
