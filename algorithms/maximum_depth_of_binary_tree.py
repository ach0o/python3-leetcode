# https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def get_depth(node, depth):
            if not node:
                return depth - 1
            leftc = get_depth(node.left, depth + 1)
            rightc = get_depth(node.right, depth + 1)
            return max(leftc, rightc)

        return get_depth(root, 1)
