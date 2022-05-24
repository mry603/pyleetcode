#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#

# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) <3 or len(grid[0]) <3:
            return 0
        ans = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j]==5:
                    new_grid = []
                    for m in range(i-1,i+2):
                        for n in range(j-1,j+2):
                            new_grid.append(grid[m][n])
                    if self.ismagic(new_grid) == True:
                        ans = ans +1
        return ans
    def ismagic(self,grid):

        if len(set(grid))!=9: return False #不重复
        if max(grid)!= 9 or min(grid)!=1:
            return False
        col =[0]*3
        lin =[0]*3
        for i in range(len(grid)):
            col[i%3] = col[i%3]  + grid[i]
            lin[i//3] = lin[i//3] + grid[i]
        if len(set(col))!=1 or len(set(lin))!=1:
            return False
        return True
        
# @lc code=end

