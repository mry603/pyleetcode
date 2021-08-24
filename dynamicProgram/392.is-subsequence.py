#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans = False
        lists = list(s)
        listt = list(t)
        if len(lists) == 0: return 1
        if len(listt) == 0: return 0
        i = 0
        for item in listt:
            if item == lists[i]:
                i = i + 1
                if i == len(lists):
                    ans =True
                    break

        return ans
        
# @lc code=end

