"""
Description:
Given a string `s`, find the length of the longest substring without duplicate characters.

Constrains:
* 0 <= s.length <= 5 * 104
* `s` consists of English letters, digits, symbols and spaces.

Ideas:
Double pointers and set, but pay attention to corner case when there is no duplicates at all (use max() when return)

"""

from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start, end = 0, 1
        max_count = 1
        max_index = (0, 1)
        char_set = set()
        char_set.add(s[0])
        while end < len(s):
            if s[end] not in char_set:
                char_set.add(s[end])
            else:
                current_count = end - start
                if current_count > max_count:
                    max_count = current_count
                    max_index = (start, end)
                while start < end and s[start] != s[end]:
                    char_set.remove(s[start])
                    start += 1
                start += 1
            end += 1
        # pay attention to the max()
        return max(max_index[1] - max_index[0], len(char_set))
      
