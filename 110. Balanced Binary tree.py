class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root):
        if not root:
            return 0

        left_h = self.height(root.left)
        right_h = self.height(root.right)

        return max(left_h, right_h) + 1

    def isBalanced(self, root):
        if not root:
            return True

        left_h = self.height(root.left)
        right_h = self.height(root.right)

        if abs(left_h - right_h) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
