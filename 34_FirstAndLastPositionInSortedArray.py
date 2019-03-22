'''
34. Find First and Last Position of Element in Sorted Array
Medium

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 法1 线性搜索：O(n)
        # # 法2 二分搜索 自己写的 先找到target，然后往左往右查找
        # if nums==[] or target==None: return [-1,-1]  # 不能用not target,防止target==0
        # left = 0
        # right = len(nums)-1
        # index = -1          # 注意需要先定义index，以防找不到的情况
        # count = 0
        # while left<=right:
        #     mid = (left+right)//2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         count = 1
        #         index = mid
        #         break
        # print(index)
        # indexlow = index  # 注意此处需要重新赋值，否则先往左走再从最左往
        # while indexlow>0:
        #     indexlow -= 1
        #     if nums[indexlow]==target:
        #         count+=1
        #     else:
        #         indexlow += 1
        #         break
        # indexhigh = index
        # while indexhigh<len(nums)-1:
        #     indexhigh += 1
        #     if nums[indexhigh]==target:
        #         count+=1
        #     else:
        #         indexhigh -= 1
        #         break
        # output = [indexlow,indexhigh]
        # print(count)
        # return output

        # 法3 二分查找 直接在查找过程中判断是不是第一个或最后一个target 时间复杂度O(logn)
        if nums is None or len(nums) == 0:
            return [-1, -1]
        if target is None:
            return [-1, -1]
        n = len(nums)

        left, right = 0, n - 1     # 往左走
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target: # 注意此处带等号
                right = mid
            else:
                left = mid
        if nums[left] == target:   # 因为循环条件是left+1<right，即最后left和right一定相差1
            ind1 = left
        elif nums[right] == target:
            ind1 = right
        else:
            return [-1, -1]

        left, right = 0, n - 1    # 往右走
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        ind2 = right if nums[right] == target else left

        return [ind1, ind2]


sol = Solution()
# ans = sol.searchRange([3,3,3,3,3,6],3)
# print(ans)
# ans = sol.searchRange([1,2,3,4,5,5],6)
# print(ans)
ans = sol.searchRange([-1,0,0,0,2,3],0)
print(ans)