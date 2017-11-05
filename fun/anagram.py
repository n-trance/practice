#!/usr/bin/python3

'''
checks if a string is an anagram
'''

user_input = input("string: ")

# we just need to check that word[0] == end[-0]
string_size = len(user_input)//2

isAnagram = True
for i in range(0, string_size):
    if user_input[i] != user_input[(-1) - i]:
        isAnagram = False
        break

if (isAnagram):
    print("Yes")
else:
    print("No")
