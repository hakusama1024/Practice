class MaxStack:
	def __init__(self):
		self.stack = []
		self.maxStack = []
	def push(self, v):
		self.stack.append(v)
		if self.maxStack:
			tmp = self.maxStack[-1]
			if tmp > v : self.maxStack.append(tmp)
			else : self.maxStack.append(v)
		else:
			self.maxStack.append(v)
	def peekMax(self):
		if self.maxStack:
			return self.maxStack[-1]
	def popMax(self):
		if self.stack:
			counter = 0
			curMax = self.maxStack
	
