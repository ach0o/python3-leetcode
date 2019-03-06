# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0

        if not nums:
            return j

        # two pointer approach
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1
