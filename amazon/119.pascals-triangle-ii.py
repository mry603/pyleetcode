#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
        #method1
        # yang = list(1 for i in range(rowIndex+1))
        # for i in range(2,rowIndex+1):
        #     for j in range(i-1,0,-1):
        #         yang[j] += yang[j-1]
        # return yang  

        #method2
        # triangle = [1]
        
        # for i in range(1, rowIndex + 1):
        #     triangle.append(int(triangle[i - 1] * (rowIndex - (i - 1)) / i))
        
        # return triangle  
class Solution:
    
    def comb(self, n, m):
        
        if n == m or m == 0:
            return 1
        else:
            return factorial(n) // ( factorial(m) * factorial(n-m) )
            #factorial 阶乘 

        
    def getRow(self, rowIndex: int) -> List[int]:       
        return [ self.comb(rowIndex,i) for i in range(0, rowIndex+1) ]
        


        
# @lc code=end

