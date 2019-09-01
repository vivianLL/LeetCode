'''
33. Search in Rotated Sorted Array
Medium

https://leetcode.com/problems/search-in-rotated-sorted-array/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
'''
class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            print(left,mid,right)

            if nums[mid]==target:
                return mid
            if nums[left]==target:
                return left
            if nums[right]==target:
                return right

            if nums[left]<nums[mid]:
                if nums[left]<target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target<nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return -1

sol = Solution()
ans = sol.search([4,5,6,7,0,1,2],0)
print(ans)
ans = sol.search([4,5,6,7,8,1,2,3],8)
print(ans)
ans = sol.search([5,1,2,3,4],1)
print(ans)
ans = sol.search([1,2,3,4,5,6],4)
print(ans)
ans = sol.search([1],1)
print(ans)
# 思路：二分法
# 从左向右，如果左边的点比右边的点小，说明这两个点之间是有序的。
# 如果左边的点比右边的点大，说明中间有个旋转点，所以一分为二后，肯定有一半是有序的。所以还可以用二分法。
# 不过先要判断左边有序还是右边有序，如果左边有序，则直接将目标与左边的边界比较，就知道目标在不在左边，
# 如果不在左边肯定在右边。