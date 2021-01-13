#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x):
        '''(int) -> bool
        transfer to str 
        edge example:
        1 negative number
        2 len of number is odd 
        '''
        if x < 0:
            return False
        elif x < 10:
            return True
        str_x = str(x)
        for i in range(len(str_x) // 2):
            if str_x[i] != str_x[-i-1]:
                return False
        return True
        
# @lc code=end

