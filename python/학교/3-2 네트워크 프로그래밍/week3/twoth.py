import threading
import time

done = False

def counter_th():
    count = 0
    while not done:
        count += 1
        print('Count = ', count)
        time.sleep(2)

def userinput_th():
    global done
    while not done:
        n = input('Input your messsage : ')
        if n == 'exit':
            done = True
        else:
            print(n)

if __name__ == '__main__':
    c_th = threading.Thread(target=counter_th)
    u_th = threading.Thread(target=userinput_th)
    c_th.start()
    u_th.start()

    c_th.join()
    u_th.join()
    print('end of program')