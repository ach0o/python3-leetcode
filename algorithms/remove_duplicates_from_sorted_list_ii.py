# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def find_dups(self, head):
        nodes = head
        dups = set()
        while nodes and nodes.next:
            if nodes.val == nodes.next.val:
                dups.add(nodes.val)
            nodes = nodes.next
        return dups

    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':

        if not head:
            return None

        nodes = head
        dups = self.find_dups(head)

        new_list = None
        new_nodes = None

        while nodes:
            if nodes.val not in dups:
                if not new_list:
                    new_list = ListNode(nodes.val)
                    new_nodes = new_list

                else:
                    new_nodes.next = ListNode(nodes.val)
                    new_nodes = new_nodes.next
            nodes = nodes.next
        return new_list
