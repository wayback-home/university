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
                prevent_ms = random.uniform(0, 1)
                backoff = 2 ** times + prevent_ms
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
        raise Exception("시간초과")
    return attempsNumber


# 메인함수
print("Binary Expotential Backoff Program Test")
while True:
    attemps = int(input("시도 횟수를 입력해주세요 : "))
    attempsNumber = 0
    print(backoff(printBEB, attemps))
