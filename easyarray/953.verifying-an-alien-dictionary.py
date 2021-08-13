#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            x = words[i]
            y = words[i+1]
            minlength = min(len(x),len(y))
            for j in range(minlength):
                xin = order.index(x[j])
                yin = order.index(y[j])
                if xin > yin:
                    return False
                elif xin < yin:
                    break
            if j == minlength-1 and x[j] == y[j] and len(x) > len(y):
                #to solve special case like ["aa","a"]
                return False
        return True
        
# @lc code=end

