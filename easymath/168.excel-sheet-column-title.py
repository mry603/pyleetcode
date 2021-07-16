#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet ='ZABCDEFGHIJKLMNOPQRSTUVWXY'
        ans = [' ']
        while(columnNumber != 0):
            units = columnNumber%26
            columnNumber = columnNumber//26
            if units == 0:
                columnNumber = columnNumber-1
            ans = list(alphabet[units])+ans
            ansstr = "".join(ans)
        return ansstr.rstrip()
# @lc code=end

