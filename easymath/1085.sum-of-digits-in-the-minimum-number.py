#
# @lc app=leetcode id=1085 lang=python3
#
# [1085] Sum of Digits in the Minimum Number
#

# @lc code=start
class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_nums = min(nums)
        if min_nums <10 :
            if min_nums %2 == 0:
                return 1
            else:
                return 0
        else:
            minnumsum = 0
            for item in str(min_nums):
                minnumsum = minnumsum + int(item)
            if minnumsum %2 == 0:
                return 1
            else:
                return 0
        
# @lc code=end

