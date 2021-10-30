def czy_trojkat(a, b, c):
    return a+b > c and a+c > b and b+c > a


print(czy_trojkat(3, 4, 5))
print(czy_trojkat(3, 4, 50))
