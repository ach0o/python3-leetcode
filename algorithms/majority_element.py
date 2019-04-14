# https://leetcode.com/problems/majority-element/


from typing import List


class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        nums.sort()
        major_cutline = len(nums) // 2

        i = 0
        j = i + major_cutline

        while j < len(nums):
            if nums[i] == nums[j]:
                return nums[i]
            else:
                i = nums.index(nums[j])
                j = i + major_cutline

        # Boyer-Moore Voting Algorithm approach
        # from leetcode
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
