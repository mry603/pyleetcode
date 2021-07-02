#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1list = list(num1)
        num2list = list(num2)
        num1list.reverse()
        num2list.reverse()
        carry = 0
        ans = []
        for i in range(max(len(num1list),len(num2list))):
            if i <len(num1list) and i <len(num2list):
                x = int(num1list[i])-int('0') + int(num2list[i])-int('0')  + carry
            elif i<len(num1list):
                x = int(num1list[i])-int('0')  + carry
            elif i<len(num2list):
                x = int(num2list[i])-int('0') + carry
            ans.append(str(x%10))
            carry = x//10
        if carry>0:
            ans.append(str(carry))
        ans.reverse()
        return "".join(ans)
        
        
# @lc code=end

