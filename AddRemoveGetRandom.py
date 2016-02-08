import random
class My:
	def __init__(self):
		self.d = {}
		self.l = []
	def add(self, v):
		self.d[v] = len(self.l)
		self.l.append(v)
		print "after add d: ", self.d
		print "after add l: ", self.l
	def remove(self, v):
		if v in self.d:
			po = self.d[v]
			value = self.l[-1]
			self.d[value] = po
			del self.d[v]
			del self.l[-1]
		print "after remove d: ", self.d
		print "after remove l: ", self.l
	def getRandom(self):
		print random.choice(self.l)

my = My()
my.add(3)
my.add(4)
my.add(5)
my.add(6)
my.add(7)
my.add(9)
my.remove(9)
my.getRandom()
