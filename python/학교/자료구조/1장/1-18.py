def f(n):
    print(n, end=" ")
    if n > 0:
        f(n - 1)


f(4)