class BigInteger:
	def __init__(self, num):
		self.bigInteger = []
		self.sign = False
		if num < 0:
			self.sign = True
		num = abs(num)
		while num:
			self.bigInteger.insert(0, num%10)
			num /= 10
		if self.sign:
			self.bigInteger.insert(0, '-')	
	def add(self, n):
		sign = False
		if n < 0:
			sign = True
			n = -n
		nlist = []
		while n:
			nlist.insert(0, n%10)
			n/=10
		if self.bigInteger[0] == '-' and sign:
			self.bigInteger = self.addTwoList(self.bigInteger[1:], nlist)
			self.bigInteger.insert(0, '-')
		elif self.bigInteger[0] == '-' and not sign:
			self.bigInteger = self.minusTwoList(nlist, self.bigInteger[1:])
		elif self.bigInteger[0] != '-' and sign:
			self.bigInteger = self.minusTwoList(self.bigInteger[1:], nlist)
		elif self.bigInteger[0] != '-' and not sign:
			self.bigInteger = self.addTwoList(self.bigInteger, nlist)
		return self.bigInteger

	def addTwoList(self, list1, list2):
		print list1
		print list2
		list1 = list1[::-1]
		list2 = list2[::-1]
		l = []
		s = []
		if len(list1) < len(list2):
			l = list2
			s = list1	
		else:
			l = list1
			s = list2
		acc = 0
		
		for i in range(len(s)):
			tmp = (l[i] + acc + s[i])/10
			l[i] = (l[i]+s[i]+acc)%10
			acc = tmp
		print l
		if acc:
			for i in range(len(s), len(l)):
				tmp = (l[i]+acc)/10
				l[i] = (l[i]+acc)%10
				acc = tmp
		if acc:
			l.append(1)
		return l[::-1]
			
		

	def minusTwoList(self, list1, list2):
		return list1
				
				

a = BigInteger(9999999)
			
print a.add(21341)
		
