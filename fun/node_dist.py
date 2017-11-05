'''
distance between two nodes in a binary tree
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

# not a balanced binary tree
# doesn't auto balance
class BinaryTree:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def add(self, value):
        # create node
        new_node = Node(value)
        # empty tree case
        if not self.head:
            self.head = new_node
        else:
            # find where to add new_node
            curr = self.head
            added_node = False
            while (not added_node):
                if (value < curr.getData()):
                    # go or add to left
                    if (curr.getLeft()):
                        curr = curr.getLeft()
                    else:
                        curr.setLeft(new_node)
                        added_node = True
                elif (value > curr.getData()):
                    # go of add to right
                    if (curr.getRight()):
                        curr = curr.getRight()
                    else:
                        curr.setRight(new_node)
                        added_node = True
        # fin
        print("node added: ", value)

# assume head exists
def distToNode(n, head):
    count = 0
    curr = head
    while (curr.getData() != n):
        if n < curr.getData():
            curr = curr.getLeft()
        else:
            curr = curr.getRight()
        count += 1
    return count

# gets distance from a and b
def getDist(a, b, tree):
    # case same number
    if a == b:
        return 0
    # have x < y
    x = 0
    y = 0
    if a < b:
        x = a
        y = b
    else:
        x = b
        y = a
    # find common branch
    curr = tree.head
    while not(x <= curr.getData() <= y):
        if curr.getData() > x and curr.getData() > y:
            curr = curr.left
        else:
            curr = curr.right
    # we are now on a common branch
    # get dist to a and b from curr
    x_dist = distToNode(x, curr)
    y_dist = distToNode(y, curr)
    return (x_dist + y_dist)

# make simple binary tree
nums = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
b_tree = BinaryTree()

for i in nums:
    b_tree.add(i)

assert(getDist(8,8,b_tree) == 0)
# print(getDist(1,15, b_tree))
assert(getDist(1,15,b_tree) == 6)
assert(getDist(14,6,b_tree) == 4)
assert(getDist(2,6,b_tree) == 2)

print("all tests passed")
