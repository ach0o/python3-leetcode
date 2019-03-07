# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # two pointer approach
        i = 0
        j = 1
        is_twice = False

        while j < len(nums):

            if nums[j] == nums[i]:
                # j equals i means `at most two dups` condition is satisfied.
                if is_twice:
                    # condition previously satisfied.
                    # remove the current value
                    nums.pop(j)
                    continue
                # change flag to indicate the condition is met.
                is_twice = True

                # move pointer to the last elem of dups
                i = j

            else:
                # condition is no longer valid
                is_twice = False
                i += 1

            j += 1

        return i + 1
