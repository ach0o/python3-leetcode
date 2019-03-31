# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_s = list()
        self.sub_s = list()
        self.cache_peek = None

    def push(self, x: 'int') -> 'None':
        """
        Push element x to the back of queue.
        """
        if not self.main_s:
            self.cache_peek = x
        self.main_s.append(x)

    def pop(self) -> 'int':
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.sub_s:
            while self.main_s:
                self.sub_s.append(self.main_s.pop())
        return self.sub_s.pop()

    def peek(self) -> 'int':
        """
        Get the front element.
        """
        if not self.sub_s:
            return self.cache_peek
        return self.sub_s[-1]

    def empty(self) -> 'bool':
        """
        Returns whether the queue is empty.
        """
        return not self.main_s and not self.sub_s


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
