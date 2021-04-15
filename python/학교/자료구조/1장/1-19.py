def g(n):
    if n > 0:
        g(n - 1)
    print(n, end=" ")


g(4)