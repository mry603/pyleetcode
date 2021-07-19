#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        '''
        if num == 1: return True
        for i in range (2,num//2+1):
            if i * i == num:
                return True
            elif i*i >num:
                return False
        
        #newton 

        
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num
        '''
        #二分法
        left, right = 2, num // 2
        
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        
        return False
# @lc code=end

