#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        
# @lc code=end

