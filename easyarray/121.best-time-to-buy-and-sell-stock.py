#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = prices[0]
        mid = []
        for i in range(1,len(prices)):
            if prices[i]-minP < 0:
                mid.append(maxP - minP)
                minP = prices[i]
                maxP = 0
            elif prices[i]-minP > maxP - minP:
                maxP = prices[i]
        mid.append(maxP - minP)
        ans = max(mid)
        if ans>0:
            return ans
        else:
            return 0
        
        
# @lc code=end

