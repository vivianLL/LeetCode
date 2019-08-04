'''
27. Remove Element
Easy

https://leetcode.com/problems/remove-element/
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''
class Solution:
    def removeElement(self, nums, val: int) -> int:
        # # 在leetcode上提交报错，不知道为什么，感觉没错
        # condition = lambda t: t != val
        # filter_nums = list(filter(condition, nums))
        # return len(filter_nums)

        # # remove函数
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)

        # # 指针法 时间O(n) 空间O(1)
        # i = 0
        # for j in range(len(nums)):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i += 1
        # return i

        # 指针法，当要删除的元素较多时效率高
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n

sol = Solution()
ans = sol.removeElement([3,2,2,3],3)
print(ans)