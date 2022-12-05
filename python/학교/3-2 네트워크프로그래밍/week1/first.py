done = False
while not done:
    try:
        n = int(input('message : '))
        done = True
    except ValueError:
        print('re-enter..')

print(n)

