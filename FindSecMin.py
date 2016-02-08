class TreeNode:
	def __init__(self, v):
		self.val = v
		self.left = None
		self.right = None

def findSecMin(root):
	m = root.val
	res = 99999
	def helper(node, res, m):
		if not node : return
		if node.left and node.left.val == m:
			if node.right and node.right.val < res and node.right.val > m:
				res = node.right.val
			return helper(node.left, res, m)
		if node.right and node.right.val == m:
			if node.left and node.left.val < res and node.left.val > m:
				res = node.left.val
			return helper(node.right, res, m)
		return res
	print helper(root, res, m)

a = TreeNode(2)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.right.left  = TreeNode(3)
a.right.right = TreeNode(5)
a.left.left = TreeNode(2)
a.left.right = TreeNode(4)
a.left.left.left = TreeNode(2)
a.left.left.right = TreeNode(2)
a.left.right.rihgt = TreeNode(4)
findSecMin(a)
