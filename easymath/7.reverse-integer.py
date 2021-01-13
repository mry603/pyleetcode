#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        '''(int) -> int
        edge example:
        1.negative number 
        2.one digit
        3.answer not in [-2**31, 2**31-1]
        
        import math
        ans = ''
        str_x = str(x)
        if len(str_x) == 1:
            return x
        else:
            for i in range(1,len(str_x)+1):
                ans += str_x[-i]
            if x < 0:
                ans = ans[-1]+ans[:-1]
            int_ans = int(ans)
            if (x >= 0 and math.log(int_ans,2) > 31 ) or (x < 0 and math.log(-int_ans,2) >= 31):
                return 0
            else:
                return int(ans)
        '''
        #list 
        # same runtime and memory usage in 2 ways
        
        import math
        flag = 0
        ans = 0
        if  x<0:
            x = -x 
            flag = 1
        while x // 10 != 0 or x % 10 != 0:
            ans = ans * 10 + x % 10
            x = x // 10
        if ans == 0 or math.log(ans,2) > 31:
            return 0
        elif flag == 1:
            return -ans
        else:
            return ans


        
# @lc code=end

