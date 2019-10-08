'''
518. Coin Change 2
Medium

https://leetcode.com/problems/coin-change-2/
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
'''
class Solution:
    def change(self, amount: int, coins) -> int:
        # dp = [0] * (amount + 1)
        # dp[0] = 1
        # for coin in coins:
        #     for i in range(1, amount + 1):
        #         if coin <= i:
        #             dp[i] += dp[i - coin]
        # # print(dp)
        # return dp[amount]

        # 稍快的写法
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(amount - i + 1):
                if dp[j]:
                    dp[i + j] += dp[j]
        return dp[amount]


sol = Solution()
ans = sol.change(5,[1,2,5])
print(ans)

# 思路：动态规划
# dp[i]表示总额为i时的方案数.
# 转移方程: dp[i] = Σdp[i - coins[j]]; 表示 总额为i时的方案数 = 总额为i-coins[j]的方案数的加和.
# 记得初始化dp[0] = 1; 表示总额为0时方案数为1.