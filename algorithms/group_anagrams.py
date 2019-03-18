# https://leetcode.com/problems/group-anagrams/


from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        for s in strs:
            tmp = ''.join(sorted(s))
            memo[tmp].append(s)
        return list(memo.values())
