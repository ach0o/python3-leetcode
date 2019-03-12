# https://leetcode.com/problems/permutations-ii/


from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(visited, nums):
            if not nums:
                res.append(visited)
                return None

            for i in range(len(nums)):
                if i > 0 and (nums[i - 1] == nums[i]):
                    continue
                backtrack(visited + [nums[i]], nums[:i] + nums[i + 1:])

        backtrack([], sorted(nums))

        return res
