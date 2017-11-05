'''
given a string of brackets check if they are valid
if not remove brackets until valid
'''

def valid(S):
    stack = []
    for i in S:
        if i == '(':
            stack += ['(']
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

# if false remove find where it's false

def removal(S):
    stack = []
    to_remove = []
    for idx, item in enumerate(S):
        if item == '(':
            stack += [(idx, item)]
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                to_remove += [idx]
    if len(stack) > 0:
        for (x,y) in stack:
            to_remove += [x]
    return to_remove
# TFTTF

S1 = '()'
S2 = '('
S3 = '(())'
S4 = '()()'
S5 = '(()'
S6 = ')))'
print(valid(S1))
print(valid(S2))
print(valid(S3))
print(valid(S4))
print(valid(S5))

print(removal(S2))
print(removal(S5))
print(removal(S6))
