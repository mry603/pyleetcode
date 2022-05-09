#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n ==0: return None
        L = len(nums1)-1
        M = m-1
        N = n-1
        while N>=0 and M>=0:
            if nums1[M] > nums2[N]:
                nums1[L] = nums1[M]
                L = L-1
                M =M-1
            else:
                nums1[L] = nums2[N]
                L = L-1
                N = N-1
        if N >=0:
            for k in range(N,-1,-1):
                nums1[k] = nums2[k]



        
# @lc code=end

