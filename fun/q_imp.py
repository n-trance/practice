'''
queue implementation with a linked list
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def show(self):
        curr = self.start
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print("None")

    # add val
    def enq(self, val):
        # create Node
        n = Node(val)
        # empty
        if not self.start and not self.end:
            self.start = n
            self.end = n
        else:
            # add to end
            self.end.next = n
            self.end = n
        # increment size
        self.size += 1
    # ret val
    def deq(self):
        # empty case
        if not self.start:
            return None
        # return front item
        node = self.start
        # one item in Q
        if self.start == self.end:
            self.start = None
            self.end = None
        # >1 item in Q
        else:
            self.start = self.start.next
        # decr size and return item
        self.size -= 1
        return node.val

Q = Queue()
Q.show()
for i in 'asdfghjkl':
    Q.enq(i)
    print("size: {0}".format(Q.size))
    Q.show()

while(Q.size > 0):
    print("removing: {0}".format(Q.deq()))
    print("size: {0}".format(Q.size))
    Q.show()
