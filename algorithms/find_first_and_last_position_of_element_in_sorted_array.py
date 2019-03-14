# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # modified binary search
        def bs(nums: List[int], target: int, is_leftmost: bool) -> int:
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                if nums[mid] > target:
                    hi = mid
                if nums[mid] == target:
                    if is_leftmost:
                        hi = mid
                    else:
                        lo = mid + 1

            return lo if is_leftmost else hi - 1

        lo = bs(nums, target, True)  # first position
        hi = bs(nums, target, False)  # last position
        if lo > hi:
            return [-1, -1]
        return [lo, hi]
