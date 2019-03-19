# https://leetcode.com/problems/rotate-image/


from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        memo = dict()
        size = len(matrix)
        for i in range(size):
            for j in range(size):
                memo[(i, j)] = matrix[i][j]
                matrix[i][j] = memo.get(
                    (size - j - 1, i), matrix[size - j - 1][i])
