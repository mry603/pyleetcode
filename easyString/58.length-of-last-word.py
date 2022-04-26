#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while s[i] == " " and i >= 0:
            i = i-1
        if i == -1:
            return len(s)
        j = i
        while s[j] != " " and j >= 0:
            j = j-1
        return i-j
        # wordlist = s.split()
        # if wordlist:
        #     return len(wordlist[-1])
        # return 0

# @lc code=end

