#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if  k ==0 or k == len(nums) or len(nums) ==1:
            pass
        else:
            # for i in range(k):
            #     nums.insert(0,nums[-1])
            #     nums.pop()
            k=k%len(nums)
            self.partreverse(nums,0,len(nums)-1)
            self.partreverse(nums,0,k-1)
            self.partreverse(nums,k,len(nums)-1)
            
    def partreverse(self,nums,left, right):
        while left<right:
            left_item = nums[left]
            nums[left] = nums[right]
            nums[right] = left_item
            left = left + 1 
            right = right -1
        return nums



# @lc code=end

