# https://leetcode.com/problems/two-sum/

from collections import defaultdict


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = defaultdict()
        for idx, val in enumerate(nums):
            rem = target - val

            if rem in nums_dict:
                return [nums_dict[rem], idx]
            else:
                nums_dict[val] = idx
