'''
produce a serialized tree from an array

e.g.
A = [1,2,3,null,null,4,5]
means root = 1
1 -> 2,3
2 -> null, null
3 -> 4, 5
'''

''' edge cases
* no items -> empty tree
* 1 item -> single node in tree
* 2 items -> single node with left
'''

''' Plan for ialize
1. loop through all the items
2. put each item in a Queue
3. if pop item
4. next 2 items belong to curr item that's been popped
'''

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    # changes tree to serialize
    def serializer(self):
        ret_arr = []
        Q = [self.root]
        while len(Q) > 0:
            curr = Q.pop(0)
            if curr:
                ret_arr += [curr.val]
                Q += [curr.left]
                Q += [curr.right]
            else:
                ret_arr += [None]
        # return serialized
        return ret_arr
    # changes data to tree
    def deserialize(self, x):
        data = x.copy()
        # no tree
        if len(data) == 0:
            return None
        # at least 1 element
        root = Node(data.pop(0))
        # next item to add children
        node_queue = [root]
        while len(node_queue) > 0 and len(data) > 0:
            # curr node to add children
            curr = node_queue.pop(0)
            # left node
            if len(data) > 0:
                left = data.pop(0)
                if (left):
                    l_node =  Node(left)
                    curr.left = l_node
                    node_queue += [l_node]
            # right node
            if len(data) > 0:
                right = data.pop(0)
                if (right):
                    r_node = Node(right)
                    curr.right = r_node
                    node_queue += [r_node]
        # return tree
        self.root = root

    def showTree(self, root):
        # helper func
        def show(node):
            if node:
                print(node.val, end="->")
                show(node.left)
                show(node.right)
            else:
                return
        show(root)


A = [1,2,3,None,None,4,5]

t = Tree()
t.deserialize(A)
t.showTree(t.root)
print("\nserializer: ")
B = t.serializer()
print(B)

t.deserialize(B)
t.showTree(t.root)

# check that A wasn't augmented
print("\ncheck A wasn't augmented")
print(A)

print("\nserializer the :")
t.deserialize(t.serializer())
t.showTree(t.root)
