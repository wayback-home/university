import threading
import time

def thread_fn(*data):
    print('string thread')
    print(threading.currentThread().getName())
    print(data)
    time.sleep(3)
    print('end of thread')

th = threading.Thread(target=thread_fn,\
                      name='Testing',\
                      args=(1,2,3))
th.start()
th.join()
print('end of program')