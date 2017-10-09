def get_max_profit(stock):
    min = stock[0]
    ret = stock[1] - stock[0]
    for i in range(1, len(stock)):
        curr = stock[i]
        if curr - min > ret:
            ret = curr - min
        if curr < min:
            min = curr
    return ret

stock = [10, 7, 5, 8, 11, 9]
stock = [3,0]
print(get_max_profit(stock))
