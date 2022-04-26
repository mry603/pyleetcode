#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def minLen(self, strs):
        minlen = len(strs[0])
        for item in strs:
            if len(item) < minlen:
                minlen = len(item)
        return minlen
    
    def prefixCheck(self,index,strs):
        word = strs[0]
        letter = word[index]
        for item in strs:
            if item[index] == letter:
                pass
            else:
                return False
        return True


    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        遍历每个单词的开头 -》 停止条件：有一个字符串结束
        一样就保存
        '''
        # ans = ""
        # minlen = self.minLen(strs)
        # if minlen == 0: return ""

        # for i in range(minlen):
        #     if self.prefixCheck(i,strs)==True:
        #         ans = strs[0][:i+1]
        #     else:
        #         break
        # return ans
        # str1, str2 = min(strs), max(strs)
        # print(str1)
        # print(str2)
        # i = 0
        # while i < len(str1):
        #     if str1[i] != str2[i]:
        #         str1 = str1[:i]
        #     i +=1

        # return str1
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix

        
# @lc code=end

