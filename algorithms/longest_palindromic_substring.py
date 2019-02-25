# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s

        even_centers = set()
        odd_centers = set()

        for idx, val in enumerate(s):
            # even case
            if idx + 1 < len(s) and val == s[idx + 1]:
                even_centers.add(idx)

            # odd case
            if idx + 2 < len(s) and val == s[idx + 2]:
                odd_centers.add(idx + 1)

        odd_pal, odd_len = self.expand_and_check(s, odd_centers, is_odd=True)
        even_pal, even_len = self.expand_and_check(
            s, even_centers, is_odd=False)

        return odd_pal if odd_len > even_len else even_pal

    def expand_and_check(self,
                         s: str,
                         indexes: set,
                         is_odd: bool) -> (str, int):
        """
        Gets palindrome center indexes and try to expand the palindrome.

        Returns palindrome string and its length.

        :type s: str
        :type indexes: set
        :type is_odd: bool
        :rtype: str, int
        """
        pal = s[0]  # initial palindrome.
        for i in indexes:
            if is_odd:
                fp, sp = i, i
            else:
                fp, sp = i, i + 1
            cnt = 1
            while True:
                if fp - cnt >= 0 and sp + cnt < len(s):
                    # compare the next char
                    if s[fp - cnt] == s[sp + cnt]:
                        cnt += 1
                    else:
                        # if not palindrome,
                        # compare the previous palindrome
                        if sp + cnt - (fp - cnt + 1) > len(pal):
                            pal = s[fp - cnt + 1: sp + cnt]
                        break
                else:
                    # if the pointer goes beyond the range,
                    # compare the previous palindrome
                    if sp + cnt - (fp - cnt + 1) > len(pal):
                        pal = s[fp - cnt + 1: sp + cnt]
                    break
        return pal, len(pal)
