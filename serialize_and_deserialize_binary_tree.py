# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""
        ans = []
        q = []
        q.append(root)

        while q:
            temp = q.pop(0)

            if temp == None:
                ans.append(None)
                continue
            else:
                ans.append(temp.val)

            q.append(temp.left)
            q.append(temp.right)
        return str(ans)
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) <= 2:
            return None

        data = data[1:len(data)-1].split(",")
        root = TreeNode(int(data[0]))
        root.left = TreeNode(None)
        root.right = TreeNode(None)
        data.pop(0)
        q = []
        q.append(root)

        while q:
            tempNode = q.pop(0)
            if tempNode == None:
                continue

            leftData = data.pop(0).strip()
            rightData = data.pop(0).strip()

            if leftData != 'None':
                tempNode.left = TreeNode(int(leftData))
                print(tempNode.left.val)
            else:
                tempNode.left = None

            if rightData != 'None':
                tempNode.right = TreeNode(int(rightData))
            else:
                tempNode.right = None

            q.append(tempNode.left)
            q.append(tempNode.right)
        return root
