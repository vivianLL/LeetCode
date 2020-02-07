'''
16. 3Sum Closest
Medium

https://leetcode.com/problems/3sum-closest/
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''
class Solution:
    def threeSumClosest(self, nums, target):
        # # 三重循环 超时
        # if len(nums) <= 2:
        #     return sum(nums)
        # diff = float('inf')
        # ans = diff
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             sum_num = nums[i] + nums[j] + nums[k]
        #             if target == sum_num:
        #                 return sum_num
        #             if abs(target - sum_num) < diff:
        #                 ans = sum_num
        #                 diff = abs(target - sum_num)
        # return ans

        # 二重循环 先排序 最外层循环遍历第一个数，后面两个数j，k在每次最外层循环开始时，取i+1和len(nums)-1，就是i之后的一头一尾。nums[i]+nums[j]+nums[k]如果小于目标那就是nums[j]不够大，我们把j后移一个，如果大于0那就是nums[k]太大了，我们把k前移一个。
        res = 0
        nums.sort()
        diff = float('inf')
        for i in range(len(nums) - 2):
            # 考虑过的i就不用再考虑了
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                # 第二第三个数：一头一尾
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                temp_diff = abs(s-target)
                if temp_diff < diff:
                    res = s
                    diff = temp_diff
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                    # 分支应该写清楚
                else:
                    return s
        return res


sol = Solution()
ans = sol.threeSumClosest([-1, 2, 1, -4], 1)
print(ans)
sol = Solution()
ans = sol.threeSumClosest([1, 1, 1, 0], -100)
print(ans)
ans = sol.threeSumClosest([1, 1, 1, 0], 3)
print(ans)