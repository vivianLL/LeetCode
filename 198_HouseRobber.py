'''
198. House Robber
Easy

https://leetcode.com/problems/house-robber/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution:
    def rob(self, nums) -> int:
        # 我的方法 递归 超时
        # if nums==[]:
        #     return 0
        # if len(nums)==1:
        #     return nums[0]
        # if len(nums)==2:
        #     return max(nums[0],nums[1])
        # return max(self.massage(nums[:-1]),self.massage(nums[:-2])+nums[-1])

        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:
            for i in range(2, len(nums)):
                nums[i] += max(nums[:i - 1])
        return max(nums)

        # 改进
        # if nums == []:
        #     return 0
        #
        # dp0, dp1 = 0, nums[0]
        # for i in range(1, len(nums)):
        #     tdp0 = max(dp0, dp1)  # 计算 dp[i][0]
        #     tdp1 = dp0 + nums[i]  # 计算 dp[i][1]
        #     dp0, dp1 = tdp0, tdp1
        #     print(dp0,dp1)
        # return max(dp0, dp1)

sol = Solution()
ans = sol.rob([2,7,3,1])
print(ans)

# 递推方程：dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])