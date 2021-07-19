#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        x = 0
        i = 1
        while(1):
            x = x + i
            i = i + 1
            if x == n:
                return i-1
            elif x > n:
                return i-2
        '''
        #binary search
        left,right = 0,n
        while left <= right:
            k = (left + right)//2
            curr = k*(k+1)//2  
            if curr == n: return k
            elif curr > n :right = k -1
            else: left = k + 1
        return right
        
# @lc code=end

