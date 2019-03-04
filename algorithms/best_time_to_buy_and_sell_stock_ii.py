# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        totalp = 0
        lowp = prices[0]

        # One pass approach
        for p in prices:
            if p > lowp:
                totalp += p - lowp
            lowp = p
        return totalp
