# https://leetcode.com/problems/contains-duplicate/


from typing import List


class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        memo = dict()
        for i in nums:
            if i not in memo:
                memo[i] = True
            else:
                return True
        return False
