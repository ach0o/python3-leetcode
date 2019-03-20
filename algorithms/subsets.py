# https://leetcode.com/problems/subsets/


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(visited, nums):
            res.append(visited)
            for i in range(len(nums)):
                backtrack(visited + [nums[i]], nums[i + 1:])
        backtrack([], nums)
        return res
