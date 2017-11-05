'''
circular linked list implementation
find
add
remove
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # return node of item else None
    def find(self, value):
        # case empty
        if not self.head:
            return None
        # case first item (and one item)
        if self.head.getData() == value:
            return self.head
        # go through c-linked list
        start = self.head
        curr = start.getNext()
        while curr != start:
            if curr.getData() == value:
                return curr
            curr = curr.getNext()

        return None

    def add(self, value):
        # create Node
        new_node = Node(value)
        # case empty c_list
        if not self.head:
            new_node.setNext(node)
            new_node.setPrev(node)
            self.head = new_node
        # go through list to add node
        
