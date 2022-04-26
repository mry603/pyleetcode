#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        g.sort()
        s.sort()
        while len(g) and len(s):
            if g[0]<=s[0]:
                result = result+1
                g.pop(0)
                s.pop(0)
            else:
                s.pop(0)
            #print(g,s)
        return result




# @lc code=end

