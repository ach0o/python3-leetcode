# https://leetcode.com/problems/unique-paths/


from math import factorial as mf


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Consider each move as 1-bit string, say for m = 3 and n = 2,
        possible path could be RRD, RDR, DRR. There should be at least one D and two R.
        So, we can find all combinations where there is one D in three moves.
        Below is an implementation of closed formula for n chooses k = n!/(n-k)!k!.
        """
        total_moves = m - 1 + n - 1
        down_moves = n - 1
        return mf(total_moves) // (mf(total_moves - down_moves) * mf(down_moves))
