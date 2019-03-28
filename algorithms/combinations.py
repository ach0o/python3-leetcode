# https://leetcode.com/problems/combinations/


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        memo = list()

        def backtrack(s, comb):
            if len(comb) == k:
                memo.append(comb)
                return
            for i in range(s, n + 1):
                backtrack(i + 1, comb + [i])
        backtrack(1, [])
        return memo
