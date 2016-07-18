# given an array print longest increasing subseq

def LIC(arr):
	n = len(arr)

	if n == 1:
		return A

	A = [1] * n
	B = [-1] * n

	i = 1
	j = 0


	while i < n:
		if j == i:
			j = 0
			i += 1

		else:
			if (arr[j] < arr[i]):
				A[i] = A[j] + 1
				B[i] = j

		j += 1

	print A
	print B


X = ['a','c', 'd' ,'b', 'a']

LIC(X)