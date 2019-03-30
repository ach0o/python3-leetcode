# https://leetcode.com/problems/implement-stack-using-queues/


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_q = list()
        self.sub_q = list()
        self.cache_top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.main_q.append(x)
        self.cache_top = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        x = self.main_q.pop(0)

        while self.main_q:
            self.cache_top = x
            self.sub_q.append(x)
            x = self.main_q.pop(0)

        self.main_q, self.sub_q = self.sub_q, self.main_q
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.cache_top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.main_q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
