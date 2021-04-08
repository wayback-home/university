import random, time


def retry_with_backoff(fn, retries=5, backoff_in_seconds=1):
    x = 0
    while True:
        try:
            return fn()
        except:
            if x == retries - 1:
                raise
            else:
                sleep = backoff_in_seconds * 2 ** x + random.uniform(0, 1)
                time.sleep(sleep)
                x += 1


i = 0


def f() -> int:
    global i
    i = i + 1
    print("  i     :", i)
    if i < 4 or i % 2 != 0:
        raise Exception("Invalid number.")
    return i


# should  sleep 3 times
print("A:")
x = retry_with_backoff(f)
print(x, "\n\n")

# should sleep 1 time
print("B:")
x = retry_with_backoff(lambda: f())
print(x, "\n")

# should crash after 2 retries
print("C:")
i = 0
x = retry_with_backoff(lambda: f(), retries=2)
