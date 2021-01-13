#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        edge example:
        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
        '''
        ans = 0
        for i in range(len(s)):
            if s[i] == 'M':
                if i > 0 and s[i-1] =='C':
                    ans += 800
                else:
                    ans += 1000
            elif s[i] == 'D':
                if i > 0 and s[i-1] =='C':
                    ans += 300
                else:
                    ans += 500
            elif s[i] == 'C':
                if i > 0 and s[i-1] =='X':
                    ans += 80
                else:
                    ans += 100
            elif s[i] == 'L':
                if i > 0 and s[i-1] =='X':
                    ans += 30
                else:
                    ans += 50
            elif s[i] == 'X':
                if i > 0 and s[i-1] =='I':
                    ans += 8
                else:
                    ans += 10
            elif s[i] == 'V':
                if i > 0 and s[i-1] =='I':
                    ans += 3
                else:
                    ans += 5
            elif s[i] == 'I':
                ans += 1
        return ans
        
# @lc code=end

