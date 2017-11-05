#!/usr/bin/python3

'''
Design a stack that has push, pop, and min, which runs in O(1) on these commands
'''
# single frame of the stack
class Frame:
    def __init__(self, item, min):
        self.item = item
        self.min = min

# holds array of frames
class Stack:
    def __init__(self):
        self.size = 0
        self.items = []

    def peek(self, value):
        return self.items[-1]

    def push(self, value):

        new_frame = Frame(value, value)
        # no items
        if (len(self.items) > 0):
            stack_min = self.items[-1].min
            if (value > stack_min):
                print("new min")
                new_frame = Frame(value, stack_min)
                print(new_frame.min)
        print("actu", new_frame.min)
        self.items.append(new_frame)
        return new_frame



    def pop(self, value):
        next

    def min(self):
        if (len(self.items) > 0):
            return self.items[-1].min
        else:
            return None

s = Stack()
print(s.min())
s.push(1)
print(s.min())
s.push(2)
print(s.min())
