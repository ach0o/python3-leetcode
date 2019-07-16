# https://leetcode.com/problems/binary-search/


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (end + start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
