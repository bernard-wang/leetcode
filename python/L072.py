"""
Description:
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
* Insert a character
* Delete a character
* Replace a character

Constrains:
* 0 <= word1.length, word2.length <= 500
* word1 and word2 consist of lowercase English letters

Ideas:
use a 2D dp array to keep track of alters needed, and the key idea is to start from length 0 for both of the words
also, notice if word1[i-1] != word2[j-1], the condition can be dp[j][i] = dp[j-1][i-1] + 1, and this means replacing
can use a 1D dp array, see minDistance_alternative()
"""

from typing import *

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not len(word1) or not len(word2):
            return len(word1) + len(word2)
        
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        for i in range(1, len(word1) + 1):
            dp[0][i] = i
        
        for j in range(1, len(word2) + 1):
            dp[j][0] = j
        
        for j in range(1, len(word2) + 1):
            for i in range(1, len(word1) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[j][i] = dp[j-1][i-1]
                else:
                    dp[j][i] = min(dp[j-1][i], dp[j][i-1], dp[j-1][i-1]) + 1
        return dp[-1][-1]
    
    def minDistance_alternative(self, word1: str, word2: str) -> int:
        if not len(word1) or not len(word2):
            return len(word1) + len(word2)
        
        dp_last = [i for i in range(len(word1) + 1)]

        for j in range(1, len(word2) + 1):
            dp_current = [0 for _ in range(len(word1) + 1)]
            dp_current[0] = j
            for i in range(1, len(word1) + 1):
                if word1[i-1] == word2[j-1]:
                    dp_current[i] = dp_last[i-1]
                else:
                    dp_current[i] = min(dp_current[i-1], dp_last[i], dp_last[i-1]) + 1
            dp_last = dp_current
        return dp_last[-1]
