#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left, right) :
        '''(int, int) ->list of int
        edge example:
        don't include 10.20.30...
        i%0 leads error
        '''
        ans = []
        for i in range(left,right+1):
            if i<10:
                ans.append(i)
            else:
                num = i 
                flag = 0
                while num // 10 != 0 or num % 10 != 0:
                    digit = num % 10 
                    if (digit != 0 and i % digit != 0) or digit == 0:
                        flag = 1
                        break
                    else:
                        num = num // 10
                if flag == 0:
                    ans.append(i)
        return ans
# @lc code=end

