import threading

total = 0
locker = threading.Lock()


def th_code(*data):
    global total

    for v in range(data[0], data[1]):
        locker.acquire()
        tmp = total
        for _ in range(1000):
            pass
        tmp += v

        total = tmp
        locker.release()


def run(nofthreads=20, limit=100000):
    length = limit // nofthreads
    for i in range(nofthreads - 1):
        th = threading.Thread(target=th_code, args=(i * length + 1, (i + 1) * length + 1))
        th.start()

    th = threading.Thread(target=th_code, args=((nofthreads - 1) * length + 1, nofthreads * length + 1))
    th.start()

    for t in threading.enumerate():
        if t != threading.currentThread():
            t.join()


if __name__ == "__main__":
    run()
    print("total = ", total)
