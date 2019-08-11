# https://leetcode.com/problems/invert-binary-tree/
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew),
#         but you can’t invert a binary tree on a whiteboard so f*** off.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
        return root
