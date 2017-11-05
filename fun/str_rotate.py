'''
check if a string is rotated
'''

S1 = input("Enter Str1: ")
S2 = input("Enter Str2: ")

def isSubstring(s1, s2):
    return s1 in s2

# str_a < str_b for length
str_a = len(S1) < len(S2) ? S1 : S2
str_b = len(S1) < len(S2) ? S2 : S1

for i in len(str_b):
    
