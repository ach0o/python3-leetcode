# https://leetcode.com/problems/long-pressed-name/


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # index of the first matching char in typed
        i = 0
        while name and typed:
            i = typed.find(name[0])
            if i == -1:  # return False if not found
                return False
            typed = typed[i + 1:]
            name = name[1:]

        # return False if name is not consumed,
        # it means the name is not fully matched.
        return not name
