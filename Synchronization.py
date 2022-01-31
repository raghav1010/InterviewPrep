import threading 
import time 

shared_resource = 8192 
lock = threading.Lock()

def double():
    global shared_resource, lock
    lock.acquire()
    while shared_resource<16384:
        shared_resource*=2
        print(shared_resource)
        time.sleep(1)
    print("Reached the maximum!!")
    lock.release()

def half():
    global shared_resource, lock
    lock.acquire()
    while shared_resource>1:
        shared_resource/=2 
        print(shared_resource)
        time.sleep(1)
    print("Reached the minimum!!")
    lock.release()
    

t1 = threading.Thread(target=half)
t2 = threading.Thread(target=double)

t1.start()
t2.start()


    