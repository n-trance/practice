'''
check if all items in string is uniq
'''

S = input("string: ")

# hashmap method
h = {}
isUnique = True
for i in S:
    if i in h.keys():
        isUnique = False
        break
    h[i] = True
print(isUnique)

# set method a set is a data structure that contains only unique elements
print("Set method")
print(len(set(S)) == len(list(S)))

# O(N**2) method requires N space
n2unique = True
for i in range(0, len(S) - 1):
    for j in range(i+1, len(S)):
        if S[i] == S[j]:
            n2unique = False
            break
print(n2unique)
