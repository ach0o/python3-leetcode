# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n

        while lo < hi:
            mid = (lo + hi) // 2
            if not isBadVersion(mid):
                # first bad version is on the right
                lo = mid + 1
            else:
                # is on the left
                hi = mid
        return lo
