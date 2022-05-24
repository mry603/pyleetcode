#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[ float('inf') ] * (n+1) for _ in range(n+1)]
        for left in range(n, 0, -1):
            for right in range(left,n+1):
                if left == right :
                    dp[left][right] = 0
                elif right - left == 1:
                    dp[left][right] = left
                else:
                    for k in range(left+1, right):
                        dp[left][right] = min( dp[left][right], max( dp[left][k-1] + k, dp[k+1][right] + k ) )
        # print(dp)
        return dp[1][-1]


    #     return self.dp(1,n)

    # def dp(self,left, right):
    #     if left == right:
    #         print(left,right,0)
    #         return 0
    #     elif right - left ==1:
    #         print(left,right,left)
    #         return left
    #     else:
    #         minlose =min(left + self.dp(left+1,right),right +self.dp(left,right-1))
    #         for i in range(left+1,right):
    #             if max(self.dp(left,i-1),self.dp(i+1,right))+i<minlose:
    #                 minlose = max(self.dp(left,i-1),self.dp(i+1,right))+i
    #         print(left,right,minlose)
    #         return minlose
        
# @lc code=end

