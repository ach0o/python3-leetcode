# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        r = 1  # initialize the 'plue one'
        l = range(len(digits) - 1, -1, -1)  # order of 10^n
        for n, i in zip(digits, l):  # zip digit and n
            r += n * (10 ** i)

        return [int(i) for i in str(r)]
