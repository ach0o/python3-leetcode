# https://leetcode.com/problems/set-matrix-zeroes/


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        cols = set()  # columns that must be zero.
        zero_row = [0] * len(matrix[0])

        for i, row in enumerate(matrix):
            for j, colv in enumerate(row):
                if colv == 0:
                    cols.add(j)

                    # alters the row but, doesn't affect the loop
                    matrix[i] = zero_row

        for row in matrix:
            for j in cols:
                row[j] = 0
