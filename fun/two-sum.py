
# design improvements
'''
if needed in seen.keys():

can be replaced by:

if needed in seen:
'''

def twoSum(nums, target):
    seen = {} # dictionary of arrays
    for i in range(0, len(nums)):
        curr = nums[i]
        needed = target - curr
        if needed in seen.keys():
            # pair exists
            print("pair exists")
            return [i, seen[needed]]
        else:
            # add current key to dict, and sum
            seen[curr] = i
    print("doesn't exit")
    return []


arr = [1,2,3,4,5]
print(twoSum(arr, 1)) # no
print(twoSum(arr, 3)) # yes
print(twoSum(arr, 9)) # yes
print(twoSum(arr, 2)) # no

arr = [1,2,3,4,5,5]
## need to handle a case where the sum is the same number, it works for this as well how about that
print(twoSum(arr, 10))
