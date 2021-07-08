#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        '''
        tribonacci_list = [0,1,1]
        if n < 3:
            return tribonacci_list[n]
        for i in range(3,n+1):
            tribonacci_list.append(tribonacci_list[0]+tribonacci_list[1]+tribonacci_list[2])
            del tribonacci_list[0]
        return tribonacci_list[-1]
        '''
        x,y,z = 0,1,1
        if n == 0: return x
        elif n == 1: return y
        elif n == 2: return z
        else:
            for i in range(3,n+1):
                x,y,z = y,z,x+y+z
            return z

    
# @lc code=end

