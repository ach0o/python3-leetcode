# https://leetcode.com/problems/excel-sheet-column-title/


from string import ascii_uppercase


class Solution:
    def __init__(self):
        self.alpha = {i + 1: v for i, v in enumerate(ascii_uppercase)}
        self.alpha[0] = 'Z'

    def convertToTitle(self, n: 'int') -> 'str':
        if n in self.alpha:
            return self.alpha[n]

        res = []

        if n % 26 == 0:
            # for edge case: 52 = 'AZ' and 0 = 'Z'
            res.append(self.convertToTitle(n // 26 - 1))
        else:
            res.append(self.convertToTitle(n // 26))

        res.append(self.convertToTitle(n % 26))

        return ''.join(res)
