# https://leetcode.com/problems/single-number-ii/


from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        memo = defaultdict(int)

        for i in nums:
            memo[i] += 1
        for k, v in memo.items():
            if v == 1:
                return k
        return 0
