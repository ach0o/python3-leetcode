# https://leetcode.com/problems/first-missing-positive/


from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        nums = set(nums)
        missing = 1
        for _ in range(len(nums)):
            if missing in nums:
                missing += 1
        return missing
