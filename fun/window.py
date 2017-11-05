'''
given arr A, and int k, return index [x,y] where min len
and has k unique elements
'''

# n**2 solution, for i in arr, find, end stop

def window_n2(A, k):
    min_len = None
    min_start = None
    min_end = None
    # for each item in array find get ra
    for i in range(0,len(A)):
        curr_start = i
        curr_end = None
        curr_len = None
        items = set({A[i]})
        count = k - 1
        for j in range(i, len(A)):
            if A[j] not in items:
                items.add(A[j])
                count -= 1
                if count == 0:
                    curr_end = j
                    curr_len = curr_end - curr_start
                    break
        print(curr_len, curr_start, curr_end)
        if not curr_len:
            continue
        if not min_len or curr_len < min_len:
            min_len = curr_len
            min_start = curr_start
            min_end = curr_end
    return (min_start, min_end)

def window_n(A, k):


A1 = [1, 1, 2, 2, 3, 3, 4, 5]
k1 = 3
A2 = [1, 2, 2, 3]
k2 = 2

print(window_n2(A1, k1))
print(window_n2(A2, k2))
