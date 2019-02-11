# https://leetcode.com/problems/longest-common-prefix/


from types import List


class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        prefix = ''

        for v in zip(*strs):
            if all([v[0] == i for i in v]):
                prefix += v[0]
            else:
                return prefix
        return prefix
