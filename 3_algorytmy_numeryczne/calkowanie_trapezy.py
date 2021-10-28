def f(x):
    return (x**2) + x + 2

def calki(a, b, n):
    h = (b-a)/n
    s = 0.0
    pod_a = f(a)

    for i in range(1, n+1):
        pod_b = f(a+h*i)
        s += pod_a + pod_b
        pod_a = pod_b

    return s * 1/2 * h

print(calki(0, 10, 20))
