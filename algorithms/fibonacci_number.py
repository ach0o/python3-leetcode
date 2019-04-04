# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def __init__(self):
        self.memo = {
            0: 0,
            1: 1
        }

    def fib(self, N: int) -> int:
        if N in self.memo:
            return self.memo[N]
        else:
            self.memo[N] = self.fib(N - 2) + self.fib(N - 1)
        return self.memo[N]
