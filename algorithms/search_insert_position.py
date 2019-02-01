# https://leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = first + (last - first) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                first = mid + 1
            else:
                last = mid - 1
        return first
