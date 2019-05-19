# https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True

        cap_range = range(ord('A'), ord('Z') + 1)
        low_range = range(ord('a'), ord('z') + 1)

        letter_range = low_range
        if (ord(word[0]) in cap_range) and (ord(word[1]) in cap_range):
            letter_range = cap_range

        for char in word[1:]:
            if ord(char) not in letter_range:
                return False
        return True
