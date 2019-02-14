# https://leetcode.com/problems/climbing-stairs/


class Solution:

    def climbStairs(self, n: 'int') -> 'int':
        # Define basic cases
        #   key: nth stair
        #   value: num of cases
        cases = {
            0: 1,
            1: 1,
            2: 2
        }

        if n <= 2:
            return cases[n]

        for i in range(3, n + 1):
            cases[i] = cases[i - 1] + cases[i - 2]

        return cases[n]
