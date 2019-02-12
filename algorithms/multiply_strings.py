# https://leetcode.com/problems/multiply-strings/


class Solution:
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        res = 0
        for i, v in enumerate(reversed(num1)):
            for j, k in enumerate(reversed(num2)):
                res += int(v) * int(k) * (10 ** (i + j))

        return str(res)
