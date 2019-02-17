# https://leetcode.com/problems/move-zeroes/


from typing import List


class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        zidx = []  # indexes of element 0
        for idx, val in enumerate(nums):
            if val == 0:
                zidx.append(idx)
        p = 0  # pointer for index diffs. reduce by 1 on every pop.
        for i in zidx:
            idx = i - p
            nums.pop(idx)
            p += 1

        nums.extend([0] * len(zidx))  # extend the list with zeros.
