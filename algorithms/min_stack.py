# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(
            (x, min(self.getMin(), x))
        )

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return float("inf")


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
