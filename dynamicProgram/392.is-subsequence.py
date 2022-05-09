#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t: return True
        if len(s)>len(t):return False
        if not len(s) and len(t): return True
        slist = list(s)
        tlist =list(t)
        spos =0
        tpos =0
        while tpos<len(tlist):
            if slist[spos] == tlist[tpos]:
                spos = spos +1
                if spos>=len(slist):
                    return True
            tpos = tpos+1
        return False
        
# @lc code=end

