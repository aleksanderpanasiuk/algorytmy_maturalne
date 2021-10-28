n = int(input("n: "))

def pierwsza(n):
    if n < 2:
        return False

    for d in range(2, int((n**1/2)+1)):
        if n%d == 0:
            return False
    return True

print(pierwsza(n))
    
