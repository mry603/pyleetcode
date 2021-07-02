#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        '''
        num_int = 0
        for i in range(len(num)):
            num_int = num_int*10 + num[i]
        
        numsum = num_int + k
        return [int(item) for item in str(numsum)]
        '''
        num.reverse()
        ans = []
        for i in range(len(num)):
            m = num[i]+k
            ans.append(m%10)
            k = m//10
        if k>0:
            kl = [int(item) for item in str(k)]
            kl.reverse()
            ans.extend(kl)
        ans.reverse()
        return ans          

        
# @lc code=end

