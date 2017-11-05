#!/usr/bin/python3
'''
program replaces ' ' with %20
'''
user_input = input("String: ")

out = ''
for i in user_input:
    if i == ' ':
        out += "%20"
    else:
        out += i

print(out)
