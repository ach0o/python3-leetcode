# https://leetcode.com/problems/symmetric-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        lefts = root.left
        rights = root.right

        while True:
            if not lefts and not rights:  # Both None
                return True
            elif bool(lefts) != bool(rights):  # Either one is None
                return False

            if lefts.val != rights.val:
                return False

            new_tree = TreeNode(None)
            new_tree.left = lefts.right
            new_tree.right = rights.left
            if not self.isSymmetric(new_tree):
                return False

            lefts = lefts.left  # towards left-most
            rights = rights.right  # toward right-most

        return True
