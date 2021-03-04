from datetime import datetime

print(datetime.now())
print("\n\n\n")

currenttime = datetime.now()

print("현재시간은", end=" ")
print(
    str(currenttime.hour)
    + ":"
    + str(currenttime.minute)
    + ":"
    + str(currenttime.second),
    end=" ",
)
print("입니다.")

print("\n" * 50)

import time

i = 0
while i < 5:
    currenttime = datetime.now()
    print("지금 시간은 ", end="")
    print(
        str(currenttime.hour)
        + ":"
        + str(currenttime.minute)
        + ":"
        + str(currenttime.second),
        end=" ",
    )
    print("입니다.")
    time.sleep(1)

    i += 1
