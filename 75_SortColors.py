'''
75. Sort Colors
Medium

https://leetcode.com/problems/sort-colors/
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.
'''
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # 有大量重复元素的快速排序——三向切分快速排序 这种方法与普通快排所区分的地方在于划分时不是划分成不大于和不小于两部分，而是划分成小于，等于，大于三部分，这样重复的值就可以不用再次划分排序。
        # # 其时间复杂度介于N - NlogN之间，最好的时间复杂度接近于O(N)，在没有重复元素的情况下有最坏的时间复杂度，空间复杂度为lgN
        # gt = len(nums)-1
        # lt = 0
        # i = 0
        # while i<=gt:
        #     if nums[i]>1:
        #         nums[i],nums[gt] = nums[gt],nums[i]
        #         gt -= 1
        #     elif nums[i]==1:
        #         i += 1
        #     else:
        #         nums[i], nums[lt] = nums[lt], nums[i]
        #         i += 1
        #         lt += 1
        # print(nums)

        # 更快的写法
        start, mid, end = 0, 0, len(nums) - 1
        while mid <= end:
            if nums[mid] == 0:
                nums[mid], nums[start] = nums[start], nums[mid]
                start += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1

        # # 对0,1,2计数
        # count1 = 0
        # count2 = 0
        # count0 = 0
        # for x in nums:
        #     if x==0:
        #         count0 += 1
        #     elif x==1:
        #         count1 +=1
        #     else:
        #         count2 += 1
        # nums[:count0] = [0]*count0
        # nums[count0:count1+count0] = [1]*count1
        # nums[count1+count0:] = [2]*count2
        # print(nums)



sol = Solution()
sol.sortColors([2,0,2,1,1,0])