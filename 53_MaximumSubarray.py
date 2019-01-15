'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -2147483647
        n = len(nums)

        sums = 0
        for i in range(0, n):
            sums += nums[i]
            if sums > ans:
                ans = sums
            if sums < 0:
                sums = 0

        return ans
        
        # ans = -2147483647
        # n = len(nums)
        #
        # sj = 0
        # si = 0
        # minSi = 0
        # for i in range(0, n):
        #     sums = 0
        #     sj += nums[i]
        #     if si < minSi:
        #         minSi = si
        #     sums = sj - minSi
        #     if sums > ans:
        #         ans = sums
        #     si += nums[i]
        # return ans

sol = Solution()
ans = sol.maxSubArray([3,2,5,6])
print(ans)
