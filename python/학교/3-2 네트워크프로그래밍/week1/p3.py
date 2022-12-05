while 1:
    try:
        n = int(input())
        break
    except ValueError as err:
        print(err)

print(n)
