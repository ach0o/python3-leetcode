# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        nodes = head

        while nodes and nodes.next:
            if nodes.val == nodes.next.val:
                nodes.next = nodes.next.next
            else:
                nodes = nodes.next

        return head
