'''
35. Search Insert Position
Easy

https://leetcode.com/problems/search-insert-position/
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
'''
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # # 顺序查找 复杂度O(n)
        # if target in nums:
        #     return nums.index(target)   # 时间复杂度O(1)
        # else:
        #     for i in range(len(nums)):
        #         if target<nums[i]:
        #             return i
        #     return len(nums)

        # # 二分查找的改进 复杂度O(logn)
        # if target<nums[0]: return 0
        # if target>nums[-1]: return len(nums)
        #
        # left = 0
        # right = len(nums)-1
        #
        # while left <= right:
        #     mid = (left + right)>>1
        #
        #     if nums[mid] > target:
        #         right = mid - 1
        #         if nums[right] < target:
        #             return right + 1
        #     elif nums[mid] < target:
        #         left = mid + 1
        #         if nums[left] > target:
        #             return left
        #
        #     else:
        #         return mid
        # return False

        # 快速写法
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l


sol = Solution()
ans = sol.searchInsert([1], 1)
print(ans)
ans = sol.searchInsert([1,3,5], 2)
print(ans)
ans = sol.searchInsert([1,3,5,7], 6)
print(ans)
ans = sol.searchInsert([1,3,5,7], 2)
print(ans)
ans = sol.searchInsert([1,3,5,6], 7)
print(ans)
ans = sol.searchInsert([1,3,5,6], 5)
print(ans)
ans = sol.searchInsert([1,3,5,6], 0)
print(ans)
ans = sol.searchInsert([1,3,5,6], 7)
print(ans)