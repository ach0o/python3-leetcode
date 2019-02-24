# https://leetcode.com/problems/maximum-subarray/
# Kadane's algorithm

from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = tmp_sum = nums[0]

        for i in nums[1:]:
            tmp_sum = max(i, tmp_sum + i)
            max_sum = max(max_sum, tmp_sum)

        return max_sum
