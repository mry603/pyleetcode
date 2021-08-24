#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        ans = [0]
        for i in range(1,n+1):
            num = 0
            k = i
            while(k!=0):
                num = num + (k%2==1)
                k = int(k/2)
            ans.append(num)
        return ans
        '''
        
        ans = [0,1]
        if n<=1:return ans[:n+1]
        b = int(log2(n))
        for i in range(1,b+2):
            for j in range(0,2**i):
                ans.append(ans[j]+1)
        return ans[:n+1]

        
# @lc code=end

