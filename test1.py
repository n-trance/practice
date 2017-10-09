r = {1:'I',
     4:'IV',
     5:'V',
     9:'IX',
     10:'X',
     40:'XL',
     50:'L',
     90:'XC',
     100:'C',
     400:'CD',
     500:'D',
     900:'MC',
     1000:'M'}
# print(r)

ri = {'I':1,
     'IV':4,
     'V':5,
     'IX':9,
     'X':10,
     'XL':40,
     'L':50,
     'XC':90,
     'C':100,
     'CD':400,
     'D':500,
     'MC':900,
     'M':1000}


def convert(n):
    curr = n

    M = curr//1000
    curr = curr%1000

    CM = curr//900
    curr = curr%900

    D = curr//500
    curr = curr%500

    CD = curr//400
    curr = curr%400

    C = curr//100
    curr = curr%100

    XC = curr//90
    curr = curr%90

    L = curr//50
    curr = curr%50

    XL = curr//40
    curr = curr%40

    X = curr//10
    curr = curr%10

    IX = curr//9
    curr = curr%9

    V = curr//5
    curr = curr%5

    IV = curr//4
    curr = curr%4

    I = curr

    val = [M,CM,D,CD,C,XC,L,XL,X,IX,V,IV,I]
    rom = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    ret = ''
    for i in range(len(rom)):
        ret += val[i]*rom[i]

    print(ret)

convert(999)

print(ri)

b = {'x':3}
def con(n):
    for key in ri.keys():
        print(key)
