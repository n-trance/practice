def min_coins(values, n):
	minCoins = n

	arr  = [0] * (n + 1)
	last = [1] * (n + 1) # 0 coins = 1, for the sake of program.

	count = 1

	while count <= n:
		fill_arr(arr, values, count, last)
		count += 1
	
	print last

	return  arr[n]

def fill_arr(arr, values, n, last):
	if n in values:
		arr[n] = 1
		last[n] = n
	else:
		arr[n] = n
		for i in values:
			if (n - i) > 0:					# check n - lowest, valid
				if (arr[n - i] + 1) < arr[n]:
					arr[n] = arr[n - i] + 1
					last[n] = last[n - i]

A = [1,5,10,12]

print(min_coins(A, 2))
print(min_coins(A, 3))
print(min_coins(A, 16))
print(min_coins(A, 4))
print(min_coins(A, 5))


