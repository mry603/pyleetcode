#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxprofit = [0]
        # minpri = prices[0]
        # maxpri = minpri
        # for item in prices:
        #     if item <maxpri:
        #         maxprofit.append(maxpri-minpri)
        #         minpri = item
        #         maxpri = item
        #     else:
        #         maxpri = item
        # maxprofit.append(maxpri-minpri)
        # return sum(maxprofit) 
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit = profit + prices[i]-prices[i-1]
        return profit



        
# @lc code=end

