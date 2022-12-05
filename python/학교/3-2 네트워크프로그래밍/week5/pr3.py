import threading
import time

done = False


def counter_th():
    counter = 0
    while not done:
        print("counter : ", counter)
        time.sleep(2)
        counter += 1


def userinput_th():
    global done
    while not done:
        n = input("input message : \n")
        if n == "exit":
            done = True
        else:
            print(n)


if __name__ == "__main__":
    c_th = threading.Thread(target=counter_th)
    u_th = threading.Thread(target=userinput_th)

    c_th.start()
    u_th.start()

    c_th.join()
    u_th.join()

    print("end of program")
