# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: 'str') -> 'bool':
        ps = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        order = []
        for c in s:
            if c in ps:
                order.append(ps[c])
            else:
                if not order:
                    return False
                if c != order.pop():
                    return False

        return True if not order else False
