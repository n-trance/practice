#!/user/bin/python3

'''
given 3 strings, where each character represents a unique number 0-9
determine if strings (a + b = c) e.g. ONE + ONE = TWO, given mapping:
['O':2, 'N':3, 'E':1, 'W':6, 'T':4]
'''
def mapString(string, mapping):
    result = ''
    for i in string:
        result += str(mapping[i])
    return int(result)

def checkMap(a, b, c, mapping):
    a_value = mapString(a, mapping)
    b_
    # b_list = list(b)
    # c_list = list(c)
    print(a_total)


A = "ONE"
B = "ONE"
C = "TWO"
m = {"O":2, "N":3, "E":1, "W":6, "T":4}
checkMap(A, "", "", m)
