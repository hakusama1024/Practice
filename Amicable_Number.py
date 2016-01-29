def IsAmicable(a, b):
	if a == 0 or b == 0 : return False
	numList_1 = []
	numList_2 = []
	for i in range(1, a/2+1):
		if a%i == 0:
			numList_1.append(i)
	sumNumber_1 = sum(numList_1)


	for i in range(1, b/2+1):
		if b%i == 0:
			numList_2.append(i)
	sumNumber_2 = sum(numList_2)
	print numList_1
	print numList_2
	return a == sumNumber_2 and b == sumNumber_1

	

print IsAmicable(220, 284)
