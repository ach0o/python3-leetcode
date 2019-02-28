# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


from typing import List


class Solution:
    def __init__(self):
        self.memo = {'2': 'abc', '3': 'def', '4': 'ghi',
                     '5': 'jkl', '6': 'mno', '7': 'pqrs',
                     '8': 'tuv', '9': 'wxyz'}
        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.backtrack('', digits)
        return self.res

    def backtrack(self, comb, next_digits):
        if len(next_digits) == 0:
            self.res.append(comb)
        else:
            for l in self.memo[next_digits[0]]:
                self.backtrack(comb + l, next_digits[1:])
