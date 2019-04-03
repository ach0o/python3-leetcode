# https://leetcode.com/problems/path-sum/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def sum_paths(tree, val):
            if not tree:
                return False

            val += tree.val
            if val == sum and not(tree.left or tree.right):
                return True

            is_left = sum_paths(tree.left, val)
            is_right = sum_paths(tree.right, val)
            return is_left or is_right

        return sum_paths(root, 0)
