# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        lowp = prices[0]
        maxp = 0

        # One pass approach
        for p in prices:
            if p < lowp:
                lowp = p
            else:
                maxp = max(maxp, p - lowp)

        return maxp
