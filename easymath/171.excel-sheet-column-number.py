#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for item in columnTitle:
            ans = ans*26 + alphabet.find(item)+1
        return ans


# @lc code=end

