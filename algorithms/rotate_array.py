# https://leetcode.com/problems/rotate-array/


from types import List


class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        steps = k % len(nums)
        num_copy = nums.copy()
        for i, v in enumerate(nums):
            nums[i] = num_copy[i - steps]
