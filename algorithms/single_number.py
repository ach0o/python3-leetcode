# https://leetcode.com/problems/single-number/


from typing import List


class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        temp = set()
        for idx, val in enumerate(nums):
            if val in temp:
                temp.remove(val)
            else:
                temp.add(val)
        return temp.pop()
