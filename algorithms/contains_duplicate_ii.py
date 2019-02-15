# https://leetcode.com/problems/contains-duplicate-ii/


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        if not nums or not k:  # Handle edge cases
            return False

        memo = dict()
        diff = 0

        for idx, val in enumerate(nums):
            if val in memo:  # True if duplicate
                if diff:
                    # Get the smallest difference
                    diff = min(diff, idx - memo[val])
                else:
                    diff = idx - memo[val]
            memo[val] = idx  # Update the memo

        if 0 < diff <= k:
            # 0 means there were no duplicates
            # and should be AT MOST k.
            return True
        else:
            return False
