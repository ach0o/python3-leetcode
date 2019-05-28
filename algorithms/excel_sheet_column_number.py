from string import ascii_uppercase


class Solution:
    def titleToNumber(self, s: str) -> int:
        total_column = 0
        for i, v in enumerate(s[::-1]):  # iterate from the end
            # A-Z = 26 letters
            # As size increase by one, A-Z repeats = 26 ^ (size-1)
            total_column += (26 ** i) * (ascii_uppercase.index(v) + 1)

        return total_column
