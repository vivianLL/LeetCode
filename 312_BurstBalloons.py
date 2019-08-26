'''
312. Burst Balloons
Hard

https://leetcode.com/problems/burst-balloons/
You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
'''
class Solution:
    def maxCoins(self, nums) -> int:
        # 循环写法
        n = len(nums)
        if n == 1: return nums[0]
        nums.append(1)
        nums.insert(0,1)

        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

        for l in range(1,n+1):
            for i in range(1,n-l+2):
                j = i+l-1
                print(i,j)
                for k in range(i,j+1):
                    dp[i][j] = max(dp[i][j],nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j])

        print(dp)
        return dp[1][n]

        # # 递归写法
        # n = len(nums)
        # if n == 1: return nums[0]
        # nums.append(1)
        # nums.insert(0,1)
        # dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        #
        # def burst(nums,dp,i,j):
        #     if i>j: return 0
        #     if dp[i][j] > 0: return dp[i][j]
        #     res = 0
        #     for k in range(i,j+1):
        #         res = max(res, nums[i - 1] * nums[k] * nums[j + 1] + burst(nums, dp, i, k - 1) + burst(nums, dp, k + 1, j))
        #
        #     dp[i][j] = res
        #     return res
        #
        # return burst(nums,dp,1,n)

        # # 快速写法
        # nums = [1] + list(filter(lambda i: i != 0, nums)) + [1]
        # n = len(nums)
        # dp = [[0 for i in range(n)] for i in range(n)]
        # 
        # for i in range(n - 1, -1, -1):
        #     for j in range(i + 2, n):
        #         for k in range(i + 1, j):
        #             v = dp[i][k] + dp[k][j] + \
        #                 nums[i] * nums[k] * nums[j]
        #             if v > dp[i][j]: dp[i][j] = v
        # return dp[0][n - 1]

sol = Solution()
ans = sol.maxCoins([3, 1, 5, 8])
print(ans)
# 思路：https://blog.csdn.net/vivian_ll/article/details/100077000