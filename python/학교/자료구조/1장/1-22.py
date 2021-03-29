def abc(n):
    r = n % 2
    print("*", end=" ")
    if n >= 2:
        abc(n // 2)
    print("%d" % r, end=" ")
    return


abc(78)