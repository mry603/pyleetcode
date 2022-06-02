#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Success 5+10
        quick select需要重写
        '''
        #Solution 1:
        # for item in nums[k:]:
        #     minindex = nums.index(min(nums[:k]))
        #     if nums[minindex]<item:
        #         nums[minindex] = item
        # return min(nums[:k])

        # TC:O((n-k+1)*k)
        # SC:O(1)

        #Solution 2 -> quick select
        # TC:O((n)
        # SC:O(logn)
        return self.findKthSmallest(nums, len(nums)+1-k)
    
    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]
 
    def partition(self, nums):
        l=0
        r=len(nums)-1
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
        

               
# @lc code=end

