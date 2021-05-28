"""
     1
    / \
   3   4
  /
 5

 root -> left -> right
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        # root -> left -> right

            result = []
            stack = []

            while stack or root:
                while root:
                    result.append(root.val)
                    stack.append(root)
                    root = root.left

                root = stack.pop()
                root = root.right

            return result

        # recursively

        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root, result):
        if root is None:
            return

        result.append(root.val)
        self.dfs(root.left, result)
        self.dfs(root.right, result)
