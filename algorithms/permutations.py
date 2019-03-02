# https://leetcode.com/problems/permutations/


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        res = []

        for i, v in enumerate(nums):
            for p in self.permute(nums[:i] + nums[i + 1:]):
                res.append([v] + p)
        return res


# Another solution - itertools
#
# from itertools import permutations
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return list(permutations(nums))
