#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1,len(digits)+1):
            if digits[-i] == 9:
                digits[-i] = 0
                if i == len(digits):
                    digits.insert(0,1)
                continue
            else:
                digits[-i] = digits[-i] + 1
                break
        
        return digits
        '''
        sum = 0
        for i in range(len(digits)):
            sum = sum*10 + digits[i]
        sum = sum +1
        return [ int(item) for item in str(sum) ]
        '''

        
# @lc code=end

