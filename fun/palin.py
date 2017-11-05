#!/user/bin/python3

'''
check if a string is a palindrome
'''

string = input("string: ")

# boolean
def isPalindrome(string):
    ret_val = True
    for i in range(0, len(string)//2):
        if string[i] != string[(-1)-i]:
            ret_val = False
            break
    return ret_val

words = [
"a",    # True
"aa",   # True
"aab",  # False
"ab",   # False
"aba",  # False
""      # True
]

for i in words:
    print(isPalindrome(i))
