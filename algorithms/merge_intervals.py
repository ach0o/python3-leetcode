# https://leetcode.com/problems/merge-intervals/

from typing import List


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key=lambda x: x.start)
        res = []
        for it in intervals:
            if not res or it.start > res[-1].end:
                res.append(it)
            else:
                res[-1].end = max(res[-1].end, it.end)
        return res
