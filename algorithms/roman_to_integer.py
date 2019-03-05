# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym = {'I': 1, 'V': 5, 'X': 10,
               'L': 50, 'C': 100, 'D': 500,
               'M': 1000}

        expt = {'I': 'VX', 'X': 'LC', 'C': 'DM'}

        res = 0
        prev = None  # temporarily store prev character
        for c in s:
            if c in expt.get(prev, ''):
                # check if exceptional case matches.
                # `prev` * 2 means, subtracting from `res` and `c`
                res -= sym.get(prev) * 2
            prev = c
            res += sym.get(c)  # always add up the symbol values.
        return res
