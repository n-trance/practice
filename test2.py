def checkIP4(ip):
    try:
        A,B,C,D = ip.split('.')
        num = [A,B,C,D]
        # check all digits
        for i in num:
            if not(i.isdigit()):
                return False
        # check range
        for i in num:
            val = int(i)
            if (val < 0 or val > 255):
                return False

        return True
    except:
        return False

# a = '111.222.111.100.11'
# if checkIP4(a):
#     print("yes")
# else:
#     print("no")

def checkIP6(ip):
    hx = '0123456789abcdef'
    try:
        val = ip.split(':')
        # check there are 8
        if len(val) != 8:
            return False
        # check values in hex
        print(val)
        for item in val:
            item = item.lower()
            for c in item:
                if c not in hx:
                    return False

        return True
    except:
        return False

b = '2001:0bd8:0000:0000:0000:ff00:0042:8329'
print(b)

if checkIP6(b):
    print('yea')
else:
    print('nah')
