# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr):
            if not node:
                return 0

            # shift left (multiply by 2) and add current bit
            curr = (curr << 1) | node.val

            # if leaf, return the formed number
            if not node.left and not node.right:
                return curr

            # sum from left and right subtrees
            return dfs(node.left, curr) + dfs(node.right, curr)

        return dfs(root, 0)
