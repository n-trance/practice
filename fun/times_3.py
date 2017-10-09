'''
given a list, get the largest number by multiplying all numbers.
len(list) >= 3, integers
'''

'''
proposed solution:
1. sort list (nlogn)
2.  case: all values >= 0:
    - we pick last 3
    case: all values <= 0:
    - we pick last 3
    case: mix of numbers:
    - we pick last number
    - check if first list[0]*list[1] > list[n-2]*list[n-3]
    we pick the largest of the two

    ***
    solution is either:
    0,1,n-1 or n-1,n-2,n-3
'''

l1 = [1,2,3]            #6
l2 = [0,1,2,3,4]        #24
l3 = [-4,-5,-3,0,-1]    #0
l4 = [-4,-5,-3, -1]     #-12
l5 = [-10, 7, 5, 10, 0] #350
l6 = [-10,0,-10,1,1,1]  #100

def times_3(list):
    list = sorted(list) #nlogn
    n = len(list)
    first = list[0]*list[1]*list[n-1]       # 0*1*n
    second = list[n-1]*list[n-2]*list[n-3]  # n*n-1*n-2
    if (first > second):
        return first
    else:
        return second

print(times_3(l1))
print(times_3(l2))
print(times_3(l3))
print(times_3(l4))
print(times_3(l5))
print(times_3(l6))
