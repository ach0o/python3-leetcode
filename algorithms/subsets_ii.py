# https://leetcode.com/problems/subsets-ii/

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []  # list for subsets

        def backtrack(visited, nums):
            if visited not in res:
                res.append(visited)
            for i in range(len(nums)):
                backtrack(visited + [nums[i]], nums[i + 1:])

        backtrack([], sorted(nums))
        return res
