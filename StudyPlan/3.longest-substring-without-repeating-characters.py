#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s): return len(s)
        dic = {}
        maxlen = 0
        order = 0
        for i,value in enumerate(s):
            if value not in dic or dic[value]<order:
                dic[value] = i
                if maxlen < i-order+1:
                    maxlen = i-order+1
            else:
                order = dic[value]+1
                dic[value] = i
        return maxlen
        # maxlen = 0
        # left = 0
        # for i in range(1,len(s)+1):
        #     if len(set(s[left:i])) == i-left:
        #         if maxlen < i-left:
        #             maxlen = i-left
        #     else:
        #         left = left+1
        # return maxlen
                

        
# @lc code=end

