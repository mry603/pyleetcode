#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        '''
        numc = num
        while numc > 9:
            carry = 0
            while numc > 9:
                carry = carry + numc%10
                numc = numc // 10
            numc = carry+numc
        return numc
        
        while num>9:
            numlist = [int(item) for item in str(num)]
            ans = 0
            for item in numlist:
                ans = ans + item
            num = ans
        return num
        '''
        if num%9 == 0 and num != 0:
            return 9
        else:
            return num%9

        
# @lc code=end

