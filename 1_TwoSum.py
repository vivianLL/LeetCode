'''
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # # 暴力法 二重循环 7228 ms, 3.54%  O(n^2)
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):  # 注意为i+1 而非i，不然两个index则相同
        #         if nums[i]+nums[j] == target:
        #             print(i,j)
        #             index = [i,j]
        #             return index

        # # 若num 和 target - num都在数组里，则满足条件，1500 ms, 19.19%，O(n^2)
        # for i in range(0,len(nums)):
        #     if target-nums[i] in nums:
        #         if i!=nums.index(target-nums[i]):   # 不可自己加自己  .index() 时间复杂度为O(n)
        #             print([i,nums.index(target-nums[i])])
        #             return [i,nums.index(target-nums[i])]

        # # 建立字典 1676 ms, 17.46%
        # dict_nums = dict(zip(range(len(nums)),nums))
        # new_dict = {v: k for k, v in dict_nums.items()}   # 将原字典反转，由原来的K-V存储形式，变为V-K存储形式
        # for i in range(0,len(nums)):
        #     if target-nums[i] in nums:
        #         if i!=new_dict[target-nums[i]]:   # 不可自己加自己  .index() 时间复杂度为O(n)
        #             print([i,new_dict[target-nums[i]]])
        #             return [i,new_dict[target-nums[i]]]

        # # 建立字典 1432 ms, 20.57% O(n)
        # dict_nums = dict(zip(nums,range(len(nums))))
        # for i in range(0,len(nums)):
        #     if target-nums[i] in nums:
        #         if i!=dict_nums[target-nums[i]]:   # 不可自己加自己  .index() 时间复杂度为O(n)
        #             print([i,dict_nums[target-nums[i]]])
        #             return [i,dict_nums[target-nums[i]]]

        # 建立字典 不一下子全加进去 一个个加一个个找
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i



sol = Solution()
sol.twoSum([2,7,3,15],5)
sol.twoSum([3,2,4],6)
sol.twoSum([-10,-1,-18,-19],-19)
sol.twoSum([3,3],6)