def maxCont(arr):
	
	max_now = 0
	max_value = 0

	for i in arr:

		if max_now + i < 0:
			max_now = 0
		else:
			max_now += i

		if max_now > max_value:
			max_value = max_now

	return max_value

A = [1,2,3,4]			#10
B = [10,-20,4,5]		#10
C = [13, -12, 20]		#21

print maxCont(A)
print maxCont(B)
print maxCont(C)