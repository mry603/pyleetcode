#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        fail:20+8
        TC:O(n*m)
        SC:O(n*m)
        '''
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        #第一个index匹配p，第二个index匹配s
        dp[0][0] = True # egde case: 当两个字符串都是空：输出true
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    #如果字符相同或p是点->dp[i + 1][j + 1] = dp[i][j]
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]


# @lc code=end

