'''
26. Remove Duplicates from Sorted Array
Easy

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
class Solution:
    def removeDuplicates(self, nums) -> int:
        # # 最简单 但LeetCode通不过 因为要in-place
        # return len(set(nums))

        # # 我的代码 最差复杂度O(n^2)
        # i = 0
        # while i < len(nums)-1:  # len(nums)随nums的变化而变化
        #     if nums[i]==nums[i+1]:
        #         del nums[i+1]  # 删除操作复杂度O(n)
        #     else:
        #         i += 1         # 注意只有不相等的时候才i+1,相等时不用加
        # return len(nums)

        # 不改变数组仅设置指针 时间复杂度O(n)
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        slower = 0
        for faster in range(1, len(nums)):
            if nums[slower] != nums[faster]:
                slower += 1
                nums[slower] = nums[faster]

        return slower + 1


sol = Solution()
ans = sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(ans)
ans = sol.removeDuplicates([])
print(ans)
# 改进：用二分查找找下一个不同的值