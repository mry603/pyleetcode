#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        '''
        fail 20+15 有字典+dp的思路但是没有考虑到枚举,想按edit distance做一直报错
        TC:O(n*logn+n*max(words[i].length))) 排序一次，每一个单词按字母数量枚举
        SC:O(n) 维护一个字典
        '''
        words.sort(key = lambda word: len(word))    #按照长度排序
        dp = {}#defaultdict(int)
        #当 int 类作为 default_factory 参数传递时，会创建一个默认值为零的 defaultdict。
        ans = 0

        for word in words:
            dp[word] =1
            #把存在的单词添加进去
            for j in range(len(word)):
                cur = word[ :j] + word[j+1: ]
                #枚举少一个字符的所有可能性
                if cur in dp:
                    dp[word] = max(dp[word], dp[cur] + 1)
                #cur存在，则更新为dp[w] = dp[cur]+1, 
                #若不存在，dp[w] =0
                #随着枚举维护出一个最大值
            ans = max(ans, dp[word])
        return ans


        
# @lc code=end

