# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:

        def filter_gen(s):
            for i in s:
                if i.isalnum():
                    yield i

        s = ''.join(filter_gen(s)).lower()
        return s == s[::-1]
