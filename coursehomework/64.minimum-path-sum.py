#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        Success 5 + 30
        TC:O(m*n)
        SC:O(m*n)
        '''
        if not grid or not grid[0]: return 0
        m =len(grid)
        n =len(grid[0])
        dp =[[0]*n for _ in range(m)]
        dp[0][0] =grid[0][0]
        for i in range(m):
            for j in range(n):
                if i ==0 and j ==0: continue
                elif i ==0: dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j ==0: dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j])+grid[i][j]
        return dp[-1][-1]

        
        
# @lc code=end

