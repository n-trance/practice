
arr = input("type in array<int> separate by space: ")
arr = arr.split(' ')
arr = list(map(int, arr))

res = []
for i in arr:
    i += 1
    if (i > 9):
        i = 0
    res.append(i)

print(res)
