# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()

        mid_idx = len(nums1) // 2
        if len(nums1) % 2 == 0:
            return (nums1[mid_idx - 1] + nums1[mid_idx]) / 2
        else:
            return nums1[mid_idx]
