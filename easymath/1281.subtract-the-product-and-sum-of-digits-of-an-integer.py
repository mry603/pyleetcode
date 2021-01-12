#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n):
        '''(int) -> int
        return product of digits minus sum of ndigits
        
        '''
        sum_of_n = 0
        product_of_n = 1
        while n // 10 != 0 or n % 10 != 0:
            digit = n%10
            n = n//10
            sum_of_n += digit
            product_of_n *= digit

        return product_of_n - sum_of_n
# @lc code=end

