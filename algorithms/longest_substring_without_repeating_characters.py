# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        highest = 0
        char_position = dict()
        left_slider = 0
        for right_slider, char in enumerate(s):
            if char_position.get(char):
                left_slider = max(char_position.get(char), left_slider)
            highest = max(highest, right_slider - left_slider + 1)
            char_position[char] = right_slider + 1
        return highest
