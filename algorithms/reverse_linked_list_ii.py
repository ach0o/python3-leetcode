# https://leetcode.com/problems/reverse-linked-list-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        node = head
        memo = dict()
        i = 1
        while i <= n:
            if i in range(m, n + 1):
                # j is an index of node reflected by the mid pt
                # example:
                #   linked list=[1->2->3->4->5->6] where m=2 and n=5
                #   say i=4, then j=2+5-4=3
                #   since memo[3] exist, switch val of memo[3] with node: 4->3
                j = m + n - i
                if j in memo:
                    node.val, memo[j].val = memo[j].val, node.val
                else:
                    memo[i] = node

            node = node.next
            i += 1
        return head
