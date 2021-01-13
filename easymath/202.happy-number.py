#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        loop 100 times
        flag = 0 
        while not n == 1 and flag < 100:
            flag += 1
            n1 = 0
            while n // 10 != 0 or n % 10 != 0:
                n1 += (n % 10) ** 2
                n = n // 10
            n = n1
        if n == 1: 
            return True
        else:
            return False
        '''
        # 4→16→37→58→89→145→42→20→4

        cycle = [4,16,37,58,89,145,42,20]
        while not n == 1:
            n1 = 0
            while n // 10 != 0 or n % 10 != 0:
                n1 += (n % 10) ** 2
                n = n // 10
            if n1 in cycle:
                return False
            n = n1
        return True



        
# @lc code=end

