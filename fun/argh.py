

def get_r(string):

    r_flag = False
    score = 0
    r_count = 0
    # go through each string
    for char in string:
        # if A, start the R flag
        if r_flag == True:

            if char == 'R':
                r_count += 1
            else:
                r_flag = False
                score += 10 ** r_count
                r_count = 0


        if char == 'A':
            r_flag = True

    score += 10 ** r_count

    return score

    # if not R stop R flag and count how many R's

string = "ARHERLLOARR"
print(get_r(string))
