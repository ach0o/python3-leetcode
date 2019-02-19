# https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: 'str', magazine: 'str') -> 'bool':
        nmg = list(magazine)
        for c in ransomNote:
            if c not in nmg:
                return False
            nmg.remove(c)
        return True
