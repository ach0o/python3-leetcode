# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r1 = list()
        r2 = list()

        # Get values of all the nodes
        while l1 is not None:
            r1.append(str(l1.val))
            l1 = l1.next

        while l2 is not None:
            r2.append(str(l2.val))
            l2 = l2.next

        # Reverse the values
        r1 = int(''.join(reversed(r1)))
        r2 = int(''.join(reversed(r2)))

        # Add the values
        _sum = reversed(list(str(r1 + r2)))
        node_dict = {idx: ListNode(val) for idx, val in enumerate(_sum)}

        # Build the ListNode
        for key, val in node_dict.items():
            val.next = node_dict.get(key + 1)

        return node_dict[0]
