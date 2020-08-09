# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__ (self):
        self.s = float("-inf")

    def helper(self,node):
        if not node:
            return 0

        left = max(self.helper(node.left), 0)
        right = max(self.helper(node.right), 0)

        newPath = node.val + left + right
        self.s = max(self.s, newPath)

        return node.val + max(left,right)

    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.s
