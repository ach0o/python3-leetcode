# https://leetcode.com/problems/triangle/


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tmp = []

        while len(triangle) > 2:
            v = triangle[-2][-1]
            tmp.insert(0, min(v + triangle[-1][-1], v + triangle[-1][-2]))

            triangle[-1].pop()
            triangle[-2].pop()
            if not triangle[-2]:
                triangle.pop()
                triangle[-1] = tmp
                tmp = []

        if len(triangle) == 2:
            return triangle[0][0] + min(triangle[-1])
        return triangle[0][0]
