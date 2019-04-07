'''
322. Coin Change
Medium

https://leetcode.com/problems/coin-change/
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
'''
import math
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)

        return -1 if dp[-1] > amount else dp[-1]


        # 更快的解法 回溯法+剪枝
        coins.sort(reverse=True)  # 降序排序，希望硬币数量尽可能的少，那么就需要尽量将面值大的硬币加入结果中
        len_coins, result = len(coins), amount + 1

        def countCoins(index, target, count):
            nonlocal result
            if not target:
                result = min(result, count)

            for i in range(index, len_coins):
                if coins[i] <= target < coins[i] * (result - count):   # 目标值一定是要大于等于我们将要放入的硬币面额，而且本次使用的硬币数量一定要比上次少
                    countCoins(i, target - coins[i], count + 1)

        for i in range(len_coins):
            countCoins(i, amount, 0)
        return -1 if result > amount else result

        # 更更快的解法
        coins.sort(reverse=True)
        len_coins, result = len(coins), amount + 1

        def countCoins(index, target, count):
            nonlocal result                      # nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
            if count + math.ceil(target / coins[index]) >= result:   # ceil:向上取整，返回大于或等于函数参数的数值
                return                           # 无解

            if target % coins[index] == 0:
                result = count + target // coins[index]
                return                           # 有解

            if index == len_coins - 1:
                return

            for i in range(target // coins[index], -1, -1):
                countCoins(index + 1, target - coins[index] * i, count + i)

        countCoins(0, amount, 0)
        return -1 if result > amount else result



sol = Solution()
ans = sol.coinChange([186,419,83,408],6249)
print(ans)
# 思路：动态规划
# 考虑成一个完全背包问题，将n个物品放入容量为amount的背包中，使得物品金额正好为amount时，所需的硬币数目最少。
# 我们定义f(amount)为使物品金额正好是amount的最少硬币数，我们会考虑第i个物品放入后，所需硬币数目
# f(amount)=min(f(amount-coins[i])+1)
# 初始条件f(0)=0，而f(i)=float('inf') i>0
# 如果最后解出的f(amount)>amount，那么表示无解