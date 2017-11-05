
'''
stack implementation
which includes:
* O(1) - min lookup
* O(1) - size lookup
'''

# frame will hold the min at the time
class Frame:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.min = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        new_frame = Frame(val)
        # if empty, no prev min
        if self.head:
            if self.head.min < val:
                new_frame.min = self.head.min
            else:
                new_frame.min = val
        else:
            new_frame.min = val
        # new frame now head
        new_frame.next = self.head
        self.head = new_frame
        self.size += 1

    def pop(self):
        # handle empty
        if not self.head:
            return None
        ret_frame = self.head
        self.head = ret_frame.next
        self.size -= 1
        return ret_frame.val

    def peek(self):
        if not self.head:
            return None
        return self.head.val

    def show(self):
        curr = self.head
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print("None")

    def min(self):
        if not self.head:
            return None
        return self.head.min

S = Stack()
for i in 'lkjhgfdsa':
    S.push(i)
    print("min: {0}, size: {1} ".format(S.min(), S.size))
S.show()
print(S.peek())
S.show()
print(S.pop())
S.show()
while S.peek():
    S.pop()
    print("min: {0}, size: {1} ".format(S.min(), S.size))

S.show()
