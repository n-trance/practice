from threading import Thread
from threading import Lock
import time

tLock = Lock()

def timer(name, delay, repeat):
    print("Timer: ", name, " started")
    tLock.acquire()
    print("lock acquired")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print("lock released")
    tLock.release()
    print("Timer: ", name, " complete")

def Main():
    t1 = Thread(target=timer, args=("timer1", 1, 5))
    t2 = Thread(target=timer, args=("timer2", 2, 5))
    t1.start()
    t2.start()

    print("Main complete")

if __name__ == "__main__":
    Main()
