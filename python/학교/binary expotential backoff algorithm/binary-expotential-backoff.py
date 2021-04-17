import random
import time

## BEB 알고리즘
def backoff(fuction, attempts):
    times = 0
    while True:
        try:
            return fuction()
        except:
            if times == attempts - 1:
                raise
            else:
                cw = 2 ** times - 1
                delay_ms = random.uniform(0, cw) / 1000
                backoff = 52.6 * delay_ms
                time.sleep(backoff)
                print(f"delay time = {backoff}초\n")
                times += 1


# 출력, 반복
def printBEB() -> int:
    global attempsNumber
    attempsNumber += 1
    time.sleep(1)
    print(f"attemps = {attempsNumber}")
    if attempsNumber < attemps:
        raise Exception()

    return attempsNumber


# 메인함수
print("Binary Expotential Backoff Program Test")
while True:
    attemps = int(input("시도 횟수를 입력해주세요 : "))
    attempsNumber = 0
    print(backoff(printBEB, attemps))