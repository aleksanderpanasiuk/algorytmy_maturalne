def fib(n):
    if n < 3:
        return 1

    return fib(n-2) + fib(n-1)


n = int(input("n: "))
print(fib(n))
