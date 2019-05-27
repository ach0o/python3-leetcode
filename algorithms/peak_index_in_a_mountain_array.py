# https://leetcode.com/problems/peak-index-in-a-mountain-array/


from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start = 0
        end = len(A) - 1

        while start < end:
            middle = (end + start) // 2
            gt_left = A[middle] > A[middle - 1]
            gt_right = A[middle] > A[middle + 1]

            if gt_left and gt_right:  # it's the peak!
                return middle
            elif gt_left and not gt_right:  # the value on the right is greater
                start = middle + 1
            elif not gt_left and gt_right:  # the value on the left is greater
                end = middle - 1
        return start
