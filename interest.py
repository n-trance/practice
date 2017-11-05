# Q: starting at $1 how long will it take to reach $6.B, compounded anually


'''
@param start: init state
@param end: goal state
@param interest: [0,1] (percentage)
@return years (years to goal)
'''
def yearToGoal(start, end, interest):
    # edge cases that make it non-terminating
    if start <= 0 or interest <= 0:
        return 0

    year = 0
    while start < end:
        start *= (1+interest)
        year += 1

    return year

goal = 6000000000 # 6billion
start = 1
interest = 1
years = yearToGoal(start, goal, interest)
print("it will take {} years to reach {}").format(years, goal)
