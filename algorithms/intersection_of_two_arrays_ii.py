# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numcount = defaultdict(int)
        for n in nums1:
            numcount[n] += 1

        result = []
        for n in nums2:
            if numcount[n] > 0:
                numcount[n] -= 1
                result.append(n)
        return result
