'''
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''
class Solution:
    def maxProfitII(self, prices):
    #     # 暴力解法 时间复杂度O(n^n) 空间复杂度O(n) 计算所有可能的交易集对应的利润，并找出其中的最大利润
    #     return self.calculate(prices,0)
    #
    # def calculate(self,prices,s):
    #     if s>=len(prices):
    #         return 0
    #     max = 0
    #     for start in range(s,len(prices)):
    #         maxprofit = 0
    #         for i in range(start+1,len(prices)):
    #             if prices[start]<prices[i]:
    #                 profit = self.calculate(prices,i+1)+prices[i]-prices[start] # 动态规划，分段
    #                 if profit > maxprofit:
    #                     maxprofit = profit # 同一个起点时的最大利润
    #         if maxprofit > max:
    #             max = maxprofit # 多个起点的最大利润
    #     return max

        # # 峰谷法 时间复杂度O(n) 空间复杂度O(1) TotalProfit=∑_i(height(peak_i)−height(valley_i))
        # i = 0
        # valley = prices[0]
        # peak = prices[0]
        # maxprofit = 0
        # while i<len(prices)-1:
        #     while i<len(prices)-1 and prices[i]>=prices[i+1]: #前大于后，后为谷底 注意i<len(prices)-1不能少
        #         i+=1
        #     valley = prices[i]
        #     while i<len(prices)-1 and prices[i]<=prices[i+1]: # 峰顶
        #         i += 1
        #     peak = prices[i]
        #     maxprofit += peak - valley
        # return maxprofit

        # 简单方法 时间复杂度O(n) 空间复杂度O(1)
        profit = 0
        for i in range(1, len(prices)):
            if (prices[i] > prices[i - 1]):
                profit += prices[i] - prices[i - 1] # 两句合为一句：profit += max(0, prices[i] - prices[i - 1])
        return profit



        # # 快速方法
        # profit = 0
        # buy = 0
        # if len(prices) < 2:
        #     return 0
        # if prices[1] > prices[0]:
        #     buy = 1
        #     profit -= prices[0]
        # for i in range(1, len(prices) - 1):
        #     if prices[i + 1] > prices[i] and not buy:
        #         buy = 1
        #         profit -= prices[i]
        #     elif buy and prices[i + 1] < prices[i]:
        #         profit += prices[i]
        #         buy = 0
        # if buy:
        #     profit += prices[-1]
        # return profit



sol = Solution()
profit = sol.maxProfitII([7,1,5,3,6,4])
print(profit) # 7
# profit = sol.maxProfitII([1,2,3,4,5])
# print(profit) # 4
# profit = sol.maxProfitII([7,1,3,5,1,4])
# print(profit) # 7
# profit = sol.maxProfitII([7,6,4,3,1])
# print(profit) # 0

# 思路：
# 比较后一天与前一天的价格高低，大于0买进，小于0不交易。其实相当于在谷底买入在峰顶卖出，因为如果连续几天上涨，每天的涨幅加一起就等于峰顶-谷底的值。
