import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print("Finish bg file write to "+self.out)

def Main():
    message = input("Enter a string: ")
    background = AsyncWrite(message, "out.txt")
    background.start()
    print("The prog can cont")

    # wait for thread to fin before continuing
    background.join()
    print("DonE!!")

if __name__ == "__main__":
    Main()
