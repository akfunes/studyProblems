
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        visited = []
        q = queue.Queue()

        q.put([root,1])

        while not q.empty():
            item = q.get()

            if item[0]:
                node = item[0]
                depth = item[1]

                q.put([node.left,depth+1])
                q.put([node.right,depth+1])

                if len(visited) < depth:
                    visited.append([])

                if(depth % 2 == 1):
                    visited[depth-1].append(node.val)
                else:
                    visited[depth-1].insert(0,node.val)


        return visited
