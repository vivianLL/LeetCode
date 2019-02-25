'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
'''
class Solution:
    def maxProfit(self, prices):
        # # 自己的常规解法 O(n)
        # min = float("inf")
        # profits = []
        # for i in range(0,len(prices)):
        #     if prices[i]<min:
        #         min = prices[i]
        #     else:
        #         profits.append(prices[i]-min)
        # if profits==[]:
        #     return 0
        # else:
        #     return max(profits)

        # 更快的写法
        minPrice = float('inf')
        res = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > res:
                res = prices[i] - minPrice
        return res




sol = Solution()
profit = sol.maxProfit([7,1,5,3,6,4])
print(profit) # 5
profit = sol.maxProfit([7,6,4,3,1])
print(profit) # 0
profit = sol.maxProfit([7,14,1,5,3,6,4])
print(profit) # 5
