#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     rest = target - numbers[i]
        #     if rest in numbers:
        #         index2 = numbers.index(rest)
        #         if index2!=i:
        #             if i<index2:
        #                 return [i+1,index2+1]
        #             else:
        #                 return [index2+1,i+1]
        #以上超时,改为二分查找
        for i in range(len(numbers)):
            rest = target - numbers[i]
            l = i+1
            r = len(numbers)-1
            while l<=r:
                mid = l+(r-l)//2
                if numbers[mid] == rest:
                    return [i+1,mid+1]
                elif numbers[mid] < rest:
                    l = mid+1
                else:
                    r = mid-1

        
        # left = 0
        # right = len(numbers)-1
        # while left<right:
        #     if numbers[left]+numbers[right] == target:
        #         return [left+1,right+1]
        #     elif numbers[left]+numbers[right] < target:
        #         left = left + 1
        #     else:
        #         right = right-1
        # dic = {}
        # for i,val in enumerate(numbers):
        #     if target - val in dic:
        #         return [dic[target - val]+1,i+1]
        #     else:
        #         dic[val] =i

        
# @lc code=end

