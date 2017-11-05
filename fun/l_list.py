'''
Linked list implementation
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        curr = self.head
        while curr:
            print(curr.data,end="->")
            curr = curr.next
        print("None")

    def add(self, data):
        # create Node
        n = Node(data)
        # case empty LinkedList
        if not self.head:
            self.head = n
        else:
            curr = self.head
            # go to end of LinkedList
            while curr.next != None:
                curr = curr.next
            curr.next = n

    def delete(self, data):
        if not self.head:
            raise Exception("cannot delete from empty list")
        # check if we remove first item
        if self.head.data == data:
            self.head = self.head.next
        else:
            # remove item from LinkedList
            curr = self.head
            while curr.next:
                # next item is to be removed
                if curr.next.data == data:
                    # skips next data
                    curr.next = curr.next.next
                    break
                curr = curr.next


l = LinkedList()
for i in 'asdfghjkwertyuio':
    l.add(i)

l.show()
print("del a")
l.delete('a')
l.show()
print("del f")
l.delete('f')
l.show()
print("del o")
l.delete('o')
l.show()
print("del 0")
l.delete('0')
l.show()

l = LinkedList()
l.delete('hello')
l.show()
