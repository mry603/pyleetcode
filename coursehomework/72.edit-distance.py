#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        fail 20+20
        思路： 
        字符相同:dp[i][j] = dp[i-1][j-1] 
        修改字符:dp[i][j] = dp[i-1][j-1] +1
        增加字符:dp[i][j] = dp[i-1][j] +1
        删除字符:相当于word2增加字符dp[i][j] = dp[i][j-1] +1
        初始化：相当于一直在增加一个字符
        TC:O(mn)
        SC:O(mn)
        '''
        dp =[[0]* (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i ==0 and j ==0: continue 
                elif i ==0: dp[i][j] = j
                elif j ==0: dp[i][j] = i
                else:
                    dp[i][j] = min(dp[i-1][j-1]-(word1[i-1]==word2[j-1]),dp[i-1][j], dp[i][j-1])+1
        #print(dp)
        return dp[-1][-1]
                
        
# @lc code=end

