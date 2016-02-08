def findCloseSqrt(n):
	if n < 0 : return -1
	if n == 0 : return 0
	l = 0
	r = n/2+1
	while l <= r:
		m = (l+r)/2
		if m**2 == n:return m
		if m**2 < n : l = m+1
		if m**2 > n : r = m-1
	return r

def findSqrt(n):
	res = findCloseSqrt(n)
	if res**2 == n:
		print True
	else:
		print False

findSqrt(10)
findSqrt(100)
findSqrt(1000)
findSqrt(10000)
findSqrt(100000)

