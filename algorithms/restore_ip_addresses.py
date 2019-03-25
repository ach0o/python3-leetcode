# https://leetcode.com/problems/restore-ip-addresses/


from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        result = []

        def backtrack(s, comb):
            if s and (len(comb) < 4):
                pass
            else:
                if (not s) and (len(comb) == 4) and (comb not in result):
                    result.append(comb)
                return

            for i in range(1, 4):
                digits = s[:i]
                if (i > 1 and digits[0] == '0') or (int(digits) > 255):
                    break
                backtrack(s[i:], comb + [digits])

        backtrack(s, [])
        return ['.'.join(c) for c in result]
