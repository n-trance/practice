#!user/bin/python3

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
        self.prev

class linkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1

    def find(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if (current.getData() == item):
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        prev = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext)
