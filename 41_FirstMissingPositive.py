'''
41. First Missing Positive
Hard

https://leetcode.com/problems/first-missing-positive/
Given an unsorted integer array, find the smallest missing positive integer.
Note:
Your algorithm should run in O(n) time and uses constant extra space.
'''
class Solution:
    def firstMissingPositive(self, nums) -> int:
        # # 自写排序做法，时间复杂度O(nlogn)
        # if nums == []:
        #     return 1
        # nums = [x for x in sorted(nums) if x >= 1]
        # if nums == []:
        #     return 1
        # if nums[0] != 1:
        #     return 1
        # for i in range(1, len(nums)):
        #     if nums[i] < 1:
        #         continue
        #     elif nums[i] - nums[i - 1] > 1:
        #         return nums[i - 1] + 1
        # return nums[-1] + 1

        # 思路是将数组的第i位存正数i+1。最后再遍历一次就可以。
        for i, v in enumerate(nums):
            if i != v - 1:
                prev = v
                while (True):
                    if prev - 1 < 0 or prev - 1 >= len(nums) or nums[prev - 1] == prev:
                        break
                    t = nums[prev - 1]  # 因为数组下标也用到了prev python自带的交换变量方法会出错
                    nums[prev - 1] = prev
                    prev = t
        for n in range(len(nums)):
            if nums[n] != n + 1:
                return n + 1
        return len(nums) + 1

        # # O(n)简洁写法
        # if nums == []:  return 1
        # for i in range(1, max(max(nums), 1) + 2):
        #     if i not in nums: return i

        # # 最快的写法 首元素为0，元素n 都放在正确的位置 index n 上
        # if not nums:
        #     return 1
        # nums = [0] + nums
        # minPositiveVal = float("inf")
        # for num in nums:
        #     if 0 < num < minPositiveVal:
        #         minPositiveVal = num
        #
        # if minPositiveVal > 1:
        #     return 1
        #
        # for i, num in enumerate(nums):
        #     if num < 0:
        #         continue
        #     elif num == i:
        #         continue
        #     elif 0 < num < len(nums):
        #         nums[i] = -1
        #         while 0 < num < len(nums):
        #             if nums[num] == num:
        #                 break
        #             temp, nums[num] = nums[num], num
        #             num = temp
        # print(nums)
        # for i, num in enumerate(nums[1:], 1):
        #     if num != i:
        #         return i
        #
        # return len(nums)



sol = Solution()
# ans = sol.firstMissingPositive([1,2,0])
# print(ans)
# ans = sol.firstMissingPositive([3,4,-1,1])
# print(ans)
ans = sol.firstMissingPositive([1,7,8,9,11,12])
print(ans)
# 中心思想：
# 1，如果每个元素n 都放在正确的位置 index n-1 上，只需要从1开始到len（nums）遍历一遍，哪个index上的数字不对，这个index+1就是空缺的最小整数。
# 2，并且空缺的最小正整数只会在“1,len(nums)+1”(极端情况下 [1,2]空缺是3)
# 3.任何负数包括0和任何大于len(nums)的数不会对结果造成影响 ([-9999,1,2,3]空缺是4  [1,2,3,9999]结果是4)
# 思路：
# 循环替换，从第一个元素n开始，找到它应该放置的位置（index为n-1），将index n-1位置的元素放置到临时变量中，将n放置在该位置。再找临时变量中元素的正确位置，以此类推，当正确位置的index大于len（nums）-1，则跳过。当正确位置的index小于0，则跳过。遇上正确的元素也跳过。跳过之后，对下一个元素循环替换。

# 如果不限制使用额外空间的话，可以用hashset存储所有的数，然后找出最大值。再遍历一次，如果i（从1开始）不在set里就返回它，全在就返回max+1.
# 但是题目规定了不能使用额外空间，那么就采取交换的策略，强行将index与elements联系起来。