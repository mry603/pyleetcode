#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#

# @lc code=start
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        '''
        fail 20+20 没有想到不同step之间的dp运算方法
        TC:O(k*n*n)
        SC:O(n*n*2)只需保存前一步状态
        '''
        #Solution1
        if k ==0: return 1
        move = [[-2, -1],[-1,-2],[2, 1],[1,2],[-2, 1],[-1,2],[2, -1],[1,-2]]
        dp =[[[1]*n for _ in range(n)] for _ in range(2)]
        for m in range(1,k+1):
            for i in range(n):
                for j in range(n):
                    dp[m%2][i][j] =0
                    for x, y in move:
                        if 0 <= i + x < n and 0 <= j + y < n:
                            dp[m%2][i][j] += dp[(m+1)%2][i + x][j + y] *0.125
        return dp[k%2][row][column]


        # Solution 2 --recursive DP--超时
    #     if k ==0: return 1
    #     self.n = n
    #     self.move = [[-2, -1],[-1,-2],[2, 1],[1,2],[-2, 1],[-1,2],[2, -1],[1,-2]]
    #     return  self.moveProb(k,row,column)

    # def moveProb(self,k,row,col):
    #     if k ==0: return 1 
    #     else:
    #         ans =0
    #         for x,y in self.move:
    #             if 0<=x+row<self.n  and  0<=y+col<self.n:
    #                 ans += self.moveProb(k-1,x+row,y+col)*0.125
    #         return ans 

        

# @lc code=end

