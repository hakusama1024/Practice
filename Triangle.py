def findTriangle(l):
	size = len(l)
	if size == 0 : return 0
	l.sort()
	count = 0
	for i in range(size-2):
		k = i+2
		for j in range(i+1, size):
			while k < size and l[i]+l[j] > l[k]:
				k+=1
			count += k-j-1	

	print count

l = [10, 21, 22, 100, 101, 200, 300]

findTriangle(l)
