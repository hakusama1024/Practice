# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        neg,pos = [], []
        q = collections.deque([(root,0)])
        while q:
            curr, lev = q.popleft()
            if curr is None: continue
            if lev>=0:
                if lev>=len(pos): pos.append([])
                pos[lev].append(curr.val)
            else: 
                i = -lev-1
                if i>=len(neg): neg.append([])
                neg[i].append(curr.val)
            q.append((curr.left,lev-1))
            q.append((curr.right, lev+1))

        return neg[::-1]+pos

