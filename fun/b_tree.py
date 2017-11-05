'''
binary tree implemenation (not a search tree)
note: use @property and @x.setter, @x.deleter
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BTree:
    def __init__(self):
        self.root = None

    # L _ R
    def showInOrder(self):

        def get(node):
            S = ''
            if node.left:
                S += get(node.left)
            S += str(node.val) + "->"
            if node.right:
                S += get(node.right)
            return str(S)

        print(get(self.root))

    # _ L R
    def showPreOrder(self):
        # queue
        q = [self.root]
        ret = ''
        while (len(q) > 0):
            # get first item in q
            curr = q.pop(0)
            # line up children
            if curr.left:
                q += [curr.left]
            if curr.right:
                q += [curr.right]
            # create ret_string
            ret += str(curr.val) + "->"
        ret += "end"
        print(ret)


    # L R _
    def showPostOrder(self):
        # inline function
        def get(node):
            S = ''
            if node.left:
                S += get(node.left)
            if node.right:
                S += get(node.right)
            S += str(node.val) + "->"
            return str(S)
        print(get(self.root))

    def add(self, val):
        # create node to add
        new_node = Node(val)
        # case empty Tree
        if not self.root:
            self.root = new_node
            print("added: {}".format(val))
        # find space to add
        else:
            curr = self.root
            while curr:
                if val < curr.val:
                    # attempt to add left, then make curr None
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = new_node
                        curr = None
                else:
                    # attemp to add right, then make curr None
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = new_node
                        curr = None
            print("added: {}".format(val))

T = BTree()
nums = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
for i in nums:
    T.add(i)
T.showPreOrder()
T.showInOrder()
T.showPostOrder()
