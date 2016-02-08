from collections import defaultdict

class TrieNode:
	def __init__(self):
		self.nodes = defaultdict(TrieNode)
		self.isWord = False
class Trie:
	def __init__(self):
		self.root = TrieNode()
		
	def insert(self, word):
		cur = self.root
		for c in word:
			cur = cur.nodes[c]
		cur.isWord = True

	def search(self, word):
		cur = self.root
		for c in word:
			if c not in cur.nodes:
				return False
			cur = cur.nodes[c]
		return cur.isWord
	
	def startWith(self, prefix):
		cur = self.root
		for c in prefix:
			if c not in cur.nodes:
				return False
			cur = cur.nodes[c]
		return True

	def complete(self, prefix):
		cur = self.root
		for i in range(len(prefix)-1):
			cur = cur.nodes[prefix[i]]
		res = []
		tmp = cur

		def dfs(node, valist):
			if node.isWord:
				res.append(valist)
			for i in node.nodes:
				dfs(i, valist+[i])
		dfs(cur, [])

		if tmp.isWord:
			res.append(prefix)
		print res

t = Trie()

t.insert("hakusama")
t.insert("haa")
t.insert("hae")
t.insert("hakaaa")
t.complete("h")
