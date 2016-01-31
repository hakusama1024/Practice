class TreeNode:
	def __init__(self, k, v):
		self.key = k 
		self.val = v 
		self.left = None
		self.right = None
	

class Map:
	def __init__(self):
		self.root = None
		self.s = 0

	def put(self, k, v):
		if not self.root:
			self.root = TreeNode(k, v)
			self.s += 1
		else:
			tmp = self.root
			while tmp:
				if tmp.key > k:
					if tmp.left:
						tmp = tmp.left
					else:
						tmp.left = TreeNode(k, v)
						self.s+=1
						return
				else:
					if tmp.right:
						tmp = tmp.right
					else:
						tmp.right = TreeNode(k, v)
						self.s+=1
						return
	def get(self, k):
		if not self.root : return None
		tmp = self.root
		while tmp:
			if tmp.key == k:
				return tmp
			elif tmp.key < k:
				tmp = tmp.right
			else:
				tmp = tmp.left
		return None

	def size(self):
		return self.s

	def printTree(self):
		if not self.root : return
		t = self.root
		stack = []
		res = []
		while stack or t:
			while t:
				stack.append(t)
				t = t.left
			t= stack.pop()
			res.append(t.key)
			t = t.right
		print res
		
			
				
		
		


m = Map()

m.put(4, 2)
m.put(3, 2)
m.put(2, 2)
m.put(6, 2)
m.put(5, 2)
m.put(1, 2)
m.put(7, 2)
m.put(9, 2)

print m.get(1).val
m.printTree()
