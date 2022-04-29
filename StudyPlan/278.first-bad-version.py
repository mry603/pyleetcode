#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        end = n
        while first <= end:
            mid = int(first + (end-first)/2)
            if isBadVersion(mid) == True:
                if mid-1 <first:
                    return mid
                elif isBadVersion(mid-1) == False:
                    return mid
                else:
                    end = mid-1
            else:
                if mid + 1 >=end:
                    return mid+1
                elif isBadVersion(mid+1) == True:
                    return mid+1
                else:
                    first = mid+1
                
        return -1
        
# @lc code=end

