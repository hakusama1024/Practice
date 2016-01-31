class DoubleLinkedList:
	def __init__(self, v):
		self.val = v
		self.next = None
		self.pre = None

class Toggle:
	def __init__(self):
		self.head = None
		self.tail = None
		self.dic = {}
	def toggle(self, c):
		if c not in self.dic:
			self.dic[c] = DoubleLinkedList(c)
			if self.head == None:
				self.head = self.dic[c]
				self.tail = self.dic[c]
				self.tail.next = self.head
				self.head.pre = self.tail
			else:
				self.tail.next = self.dic[c]
				self.tail = self.tail.next
				self.dic[c].next = self.head
				
		else:
			if self.head == self.dic[c]:
				self.head = self.dic[c].next
				del self.dic[c]
			elif self.tail == self.dic[c]:
				self.tail = self.dic[c].pre
				del self.dic[c]
			else:
				tmp = self.dic[c]
				pre = tmp.pre
				pre.next = tmp.next
				pre.next.pre = pre
				del self.dic[c]

		printlist = []
		size = len(self.dic)
		if size == 0:
			self.head = None
			self.tail = None
		head = self.head
		for i in range(size):
			printlist.append(head.val)
			head = head.next
		print printlist
			

t = Toggle()
t.toggle('c')
t.toggle('c')
t.toggle('c')
t.toggle('c')
t.toggle('c')
t.toggle('c')
t.toggle('c')
t.toggle('a')
t.toggle('b')
t.toggle('c')
t.toggle('d')
t.toggle('a')
			
		
		
