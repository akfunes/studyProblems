# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node,lower,upper = q.popleft()
            val = node.val
            if val <= lower or val >= upper:
                return False

            if node.left:
                q.append((node.left,lower,val))
            if node.right:
                q.append((node.right,val,upper))
        return True
