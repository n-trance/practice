arr = [0, 0, 0, 1, 2, 5]

def can_zero_sum(arr):
    # arr needs min 3 numbers
    head = 0
    tail = len(arr) - 1
    arr = sorted(arr)

    # while the array length is greater than 3
    while (tail - head) >= 2:

        # search for number in arr
        diff = arr[tail] + arr[head]
        if bin_search(arr, head, tail, diff):
            return True

        # if the search fails increase range if -ve, decrease range if +ve
        if (arr[tail] + arr[head]) > 0:
            tail -= 1
        else:
            head += 1

    return False



# search for number between head and tail
def bin_search(arr, head, tail, diff):
    print("H: " + str(arr[head]))
    print("T: " + str(arr[tail]))
    print(diff)
    search_arr = arr[head+1 : tail]
    if diff in search_arr:
        print("F: " + str(diff))
        return True
    return False

print(can_zero_sum(arr))
