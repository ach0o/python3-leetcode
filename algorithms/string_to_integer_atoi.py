# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        trim_str = str.lstrip()
        if not trim_str:
            return 0

        if (len(trim_str) == 1) and (not trim_str[0].isdigit()):
            return 0

        valid_char = '0123456789'
        number = trim_str.split()[0]

        if (number[0] in ('+', '-')):
            for idx, char in enumerate(number[1:]):
                if char not in valid_char:
                    number = number[:idx + 1]
        else:
            for idx, char in enumerate(number):
                if char not in valid_char:
                    number = number[:idx]

        try:
            number = float(number)
        except Exception:
            return 0

        return self.convert(number)

    def convert(self, number):
        if number < -2 ** 31:
            return -2 ** 31
        elif number > (2 ** 31) - 1:
            return (2 ** 31) - 1
        else:
            return int(number)
