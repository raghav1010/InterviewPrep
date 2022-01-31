import threading 

event = threading.Event()

def angry_bird():
    print("Waiting for angry bird to get triggered... \n")
    event.wait()
    print("Angry Bird is performing action now...")

t1 = threading.Thread(target=angry_bird)
t1.start()

x = input("Do you want to trigger angry bird? (y/n) \n")
if x=="y":
    event.set()