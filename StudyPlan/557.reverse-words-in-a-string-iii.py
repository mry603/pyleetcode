#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseword(self,s):
        ans = ""
        for i in range(len(s)-1,-1,-1):
            ans = ans + s[i]
        return ans

    def reverseWords(self, s: str) -> str:
        # if len(s) ==1:
        #     return s
        # ans = ""
        # l = 0
        # r = len(s)-1
        # for i in range(len(s)):
        #     if s[i] ==" " or i ==len(s)-1:
        #         r = i
        #         if i !=len(s)-1:
        #             ans = ans + self.reverseword(s[l:r])
        #             ans = ans + " "
        #         else:
        #             ans = ans + self.reverseword(s[l:r+1])
        #         l = i+1
        #         r = len(s)-1
        # return ans

        res = ''
        l, r = 0, 0
        while r < len(s):
            if s[r] != ' ':
                r += 1
            elif s[r] == ' ':
                res += s[l:r + 1][::-1]
                r += 1
                l = r
        res += ' '
        res += s[l:r + 2][::-1]
        return res[1:]
    


# @lc code=end

