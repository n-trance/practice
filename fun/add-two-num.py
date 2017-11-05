'''
given a singly-linked list of nums
sum them and save a linked list,
note lists are in reverse order
'''

'''
this solution is incorrect as it can't sum different lenght numbers correctly
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    ret_node = None
    curr_node = ret_node
    a = l1
    b = l2
    carry = False
    while a or b or carry:
        # get total
        total = 0
        total += a.val if a else 0
        total += b.val if b else 0
        total += 1 if carry else 0
        # check if carry is required
        if total >= 10:
            carry = True
            total //= 10
        else:
            carry = False
        # create new node and append
        new_node = ListNode(total)
        if (curr_node):
            curr_node.next = new_node
            curr_node = curr_node.next
        else:
            ret_node = new_node
            curr_node = new_node
        # go to next if a,b exists
        a = a.next if a else None
        b = b.next if a else None
    # done
    return ret_node


# populate
l1 = ListNode(2)
curr = l1
for i in [4,3]:
    tmp = ListNode(i)
    curr.next = tmp
    curr = curr.next

l2 = ListNode(5)
curr = l2
for i in [6,4]:
    tmp = ListNode(i)
    curr.next = tmp
    curr = curr.next

x = addTwoNumbers(l1, l2)
curr = x
while curr:
    print(curr.val, end='')
    curr = curr.next
print('')


l1 = ListNode(9)
curr = l1
for i in [9]:
    tmp = ListNode(i)
    curr.next = tmp
    curr = curr.next

l2 = ListNode(1)

x = addTwoNumbers(l1, l2)
curr = x
while curr:
    print(curr.val, end='')
    curr = curr.next
print('')
