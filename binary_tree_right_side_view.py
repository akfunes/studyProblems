# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = []
        ans = []
        q.append([root,0])

        while q:
            node,depth = q.pop(0)
            if node:
                if depth >= len(ans):
                    ans.append(node.val)
                else:
                    ans[depth] = node.val
                q.append([node.left,depth+1])
                q.append([node.right,depth+1])
        return ans
