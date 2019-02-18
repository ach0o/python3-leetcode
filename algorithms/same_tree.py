# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':

        if not p or not q:  # handle when either p or q is None
            return (not p and not q)  # True when both p and q be equal

        if p.val == q.val:
            # recurse over lefts and rights on the same height
            lstatus = self.isSameTree(p.left, q.left)
            rstatus = self.isSameTree(p.right, q.right)

            # True when all values of the height are equal
            return (lstatus and rstatus)
        else:
            return False
