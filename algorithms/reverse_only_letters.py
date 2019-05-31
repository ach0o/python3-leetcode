# https://leetcode.com/problems/reverse-only-letters/


from string import ascii_letters


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        result = []
        i = len(S) - 1
        for v in S:
            if v in ascii_letters:
                while not S[i] in ascii_letters:
                    i -= 1
                result.append(S[i])
                i -= 1
            else:
                result.append(v)

        return ''.join(result)
