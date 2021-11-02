def punkt_prosta(a, b, punkt):
    return punkt[1] == a * punkt[0] + b 


punkt = [0, 0] # [x, y]
a = 20
b = 2

print(punkt_prosta(a, b, punkt))
