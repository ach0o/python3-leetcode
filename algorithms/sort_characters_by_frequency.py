# https://leetcode.com/problems/sort-characters-by-frequency/


from collections import defaultdict


class Solution:
    def frequencySort(self, s: 'str') -> 'str':
        if not s:
            return s

        memo = defaultdict(int)
        for c in s:
            memo[c] += 1

        res = []
        for v in sorted(memo, key=memo.get):
            res.append(v * memo[v])

        return ''.join(res[::-1])
