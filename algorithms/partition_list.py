# https://leetcode.com/problems/partition-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        node = head
        gt_head = gt_tail = None
        lt_head = lt_tail = None

        while node:
            # make two linked list: gt x AND lt x
            if node.val >= x:
                if not gt_head:
                    gt_head = gt_tail = node
                else:
                    gt_tail.next = node
                    gt_tail = gt_tail.next
            else:
                if not lt_head:
                    lt_head = lt_tail = node
                else:
                    lt_tail.next = node
                    lt_tail = lt_tail.next
            node = node.next

        if gt_tail:
            gt_tail.next = None

        if not lt_tail:
            return gt_head

        lt_tail.next = gt_head  # combine two lists
        return lt_head
