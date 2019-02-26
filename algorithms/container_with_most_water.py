# https://leetcode.com/problems/container-with-most-water/


from typing import List


class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        lp, rp = 0, len(height) - 1  # Initialize two pointers
        max_vol = 0

        while lp != rp:
            wid = rp - lp

            # Keep the pointer with higher value and 
            # move the other pointer towards the center.
            if height[lp] > height[rp]:
                max_vol = max(wid * height[rp], max_vol)  # Save the max volume.
                rp -= 1
            else:
                max_vol = max(wid * height[lp], max_vol)
                lp += 1

        return max_vol
