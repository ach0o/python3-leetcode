# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        words = string.split()
        if len(words) != len(pattern):
            return False

        matching = dict()
        for index, value in enumerate(zip(pattern, words)):
            patt, word = value

            if patt not in matching:
                # Check if the word is found previously
                if word in words[:index]:
                    return False
                matching[patt] = word
            else:
                if matching[patt] != word:
                    return False
        return True
