class TreeNode:
	def __init__(self, v):
		self.val = v
		self.left = None
		self.right = None

def BuildBST(edges):
	size = len(edges)
	if size == 0 : return None
	dic = {}
	for e in edges:
		if e[1] not in dic:
			dic[e[1]] = [e[0]]
			if e[0] not in dic:
				dic[e[0]] = [] 
		else:
			dic[e[1]].append(e[0])
	root = None
	for i in dic:
		if dic[i] == []:
			root = TreeNode(i)
	node = helper(root, edges)
	InOrder(node)
	return node
	

def InOrder(node):
	p = node
	res = []
	stack = []
	while p or stack:
		while p :
			stack.append(p)
			p = p.left
		p = stack.pop()
		res.append(p.val)
		p = p.right 

	print res
		

def helper(root, edges):
	for i in edges:
		if i[0] == root.val:
			if i[1] < root.val:
				root.left = TreeNode(i[1])	
			else:
				root.right = TreeNode(i[1])
			del i
	if root.left:
		helper(root.left, edges)
	if root.right:
		helper(root.right, edges) 
	return root
	
	
		

eds = [[3, 1], [1, 0], [3, 6], [6, 4], [6, 7]]	

BuildBST(eds)

		
		
	

