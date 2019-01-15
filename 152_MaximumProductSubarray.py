'''
152. Maximum Product Subarray

https://leetcode.com/problems/maximum-product-subarray/
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
'''

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        if len(nums)==1:
            return ans
        else:
            imin = ans
            imax = ans
            for i in range(1,len(nums)):  # 注意i从1开始
                if nums[i]<0:
                    imin,imax = imax,imin  # 一定要先交换再求最大最小值

                imax = max(imax*nums[i],nums[i])
                imin = min(imin*nums[i],nums[i])

                ans = max(ans,imax)
            return ans

sol = Solution()
ans = sol.maxSubArray([3,2,5,6])
print(ans)