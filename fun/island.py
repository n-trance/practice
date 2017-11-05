i1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

i2 = [[0,0,0,0,0,0,0,0]]



def max_area(I):
    # helper function for getting area
    def area(x, y):
        # base case
        if not (0 <= x < width and
                0 <= y < height and
                (x, y) not in seen and
                I[y][x] == 1):
            return 0
        # case island
        seen.add((x, y))
        # get N S E W
        return (1
                + area(x, y + 1)
                + area(x, y - 1)
                + area(x + 1, y)
                + area(x - 1, y))

    height = len(I)
    width = len(I[0])
    seen = set()
    max_i = 0
    # go  through all island
    for x in range(width):
        for y in range(height):
            max_i = max(max_i, area(x, y))
    return max_i

print(max_area(i1))
print(max_area(i2))
