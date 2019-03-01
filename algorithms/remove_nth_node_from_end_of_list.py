# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# One Pass Algorithm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        fnode = None  # follow up node

        for i in range(n):  # set node to the nth from the beginning
            node = node.next

        while node:  # move both pointer until `node` reaches the end
            if not fnode:
                fnode = head
            else:
                fnode = fnode.next
            node = node.next

        if fnode:
            if fnode.next:
                # join the n-1 and n+1 node
                fnode.next = fnode.next.next
            else:
                # remove the lase node
                fnode.next = None
        else:
            # remove the first node
            fnode = head.next
            head = fnode

        return head
