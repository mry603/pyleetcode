#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) ==0: return 0
        if haystack == needle : return 0
        i =0
        while i < len(haystack)-len(needle)+1:
            if haystack[i] ==needle[0]:
                if needle == haystack[i:i+len(needle)]:
                    return i
                else:
                    i = i+1
            else:
                i = i+1
        return -1




# @lc code=end

