# https://leetcode.com/problems/word-break/


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {i: True for i in wordDict}

        def _break(string: str) -> bool:
            if not string:  # all `s` is consumed by `wordDict`
                return True
            for w in memo:
                if memo[w] and string.startswith(w):
                    if _break(string[len(w):]):
                        return True

                    # set memo False to skip on the next try
                    memo[w] = False

            # when `string` cannot be broken down with `wordDict`
            return False

        return _break(s)
