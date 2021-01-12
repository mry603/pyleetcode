#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number (self, num) :
        '''(int) -> int
        num only includes 6 and 9,
        return the max number by changing at most one digit
        '''
        str_num = str(num)
        ans = ''
        for i in range(len(str_num)):
            if str_num[i] == '6':
                ans += '9'
                if i != len(str_num)-1:
                    ans += str_num[i+1:]

                break
            else:
                ans += str_num[i]
        return int(ans)

# @lc code=end

