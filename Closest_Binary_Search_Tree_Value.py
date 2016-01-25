# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        ans = abs(target - root.val)
        ans_val = root.val

        while root:
            if abs(target - root.val) < ans:
                ans = abs(target - root.val)
                ans_val = root.val

            if target > root.val:
                root = root.right
            else:
                root = root.left


        return ans_val
