#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = []
        ans.append(cost[0])
        ans.append(cost[1])
        for i in range(2,len(cost)):
            ans.append(min(ans[i-1],ans[i-2])+cost[i])
        return min(ans[-1],ans[-2])
        
        
# @lc code=end

