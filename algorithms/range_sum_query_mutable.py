# https://leetcode.com/problems/range-sum-query-mutable/


# initial submission
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


# Segment tree implementation
class AnotherNumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tree = []
        self.n = 0

        if len(nums) > 0:
            self.n = len(nums)
            self.tree = [0] * (self.n * 2)
            self.build_tree(nums)

    def build_tree(self, nums):
        idx = 0
        for i in range(self.n, self.n * 2):
            self.tree[i] = nums[idx]
            idx += 1

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, pos, val):
        """
        :type pos: int
        :type val: int
        :rtype: void
        """
        pos += self.n
        self.tree[pos] = val
        while pos > 0:
            left = pos
            right = pos
            if pos % 2 == 0:
                right = pos + 1
            else:
                left = pos - 1
            self.tree[pos // 2] = self.tree[left] + self.tree[right]
            pos = pos // 2

    def sumRange(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        l += self.n
        r += self.n

        _sum = 0

        while l <= r:
            if l % 2 == 1:
                _sum += self.tree[l]
                l += 1
            if r % 2 == 0:
                _sum += self.tree[r]
                r -= 1
            l = l // 2
            r = r // 2
        return _sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
