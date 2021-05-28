# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        #         result = []
        #         self.helper(root, result)
        #         return result

        #     def helper(self, root, result):
        #         if root is None:
        #             return

        #         self.helper(root.left, result)
        #         self.helper(root.right, result)
        #         result.append(root.val)

        if root is None:
            return

        stack = [root]
        result = []

        while stack:
            root = stack[-1]
            if not root.left and not root.right:
                root = stack.pop()
                result.append(root.val)
            else:
                if root.right:
                    stack.append(root.right)
                    root.right = None
                else:
                    if root.left:
                        stack.append(root.left)
                        root.left = None
        return result 