# https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.s = 0
    def helper(self,node):
        if not node:
            return 0

        left = self.helper(node.left)
        right = self.helper(node.right)

        newpath = left + right + 1
        self.s = max(self.s,newpath)

        return max(left,right) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.helper(root)
        return self.s- 1

