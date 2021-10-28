a = int(input("a: "))
b = int(input("b: "))

def euklides(a, b):
    if b != 0:
        return euklides(b, a%b)
    return a


print(euklides(a,b))
