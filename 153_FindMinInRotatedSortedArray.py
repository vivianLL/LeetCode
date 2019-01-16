'''
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.
'''
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 基础遍历 python列表的min方法
        # return min(nums)

        # 二分查找
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:  # 如果最后一个元素大于第一个，则没有旋转
            return nums[0]

        while right >= left:
            mid = left + (right - left) // 2  # 这个操作不考虑操作对象的类型，总是省略小数部分，因为python3中的除法变成真除法（无论任何类型都会保持小数部分，即使整除也会表示为浮点数形式）
            if nums[mid] > nums[mid + 1]:  # 如果中间元素大于它的下一个元素，那么mid+1元素是最小的
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:  # 如果中间元素小于前一个元素，那么中间元素是最小的
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1


sol = Solution()
ans = sol.findMin([5,6,7,3])
print(ans)
ans = sol.findMin([6,7,5])
print(ans)