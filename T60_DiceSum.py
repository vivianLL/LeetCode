'''
剑指offer面试题60 n个骰子的点数

https://www.lintcode.com/problem/dices-sum/description
题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为S。输入n，打印出S的所有可能的值出现的概率。
（在LeetCode和牛客网上均没有，在LindCode上有）
'''
class Solution:
    def dicesSum(self, n):
        # Write your code here
        if n < 1:
            return []
        data1 = [0] + [1] * 6 + [0] * 6 * (n - 1)
        data2 = [0] + [0] * 6 * n  # 开头多一个0，方便按照习惯从1计数
        flag = 0
        for v in range(2, n + 1):  # 控制次数
            if flag:
                for k in range(v, 6 * v + 1):
                    data1[k] = sum([data2[k - j] for j in range(1, 7) if k > j])
                flag = 0
            else:
                for k in range(v, 6 * v + 1):
                    data2[k] = sum([data1[k - j] for j in range(1, 7) if k > j])
                flag = 1
        ret = []
        total = 6 ** n
        data = data2[n:] if flag else data1[n:]
        for v in data:
            ret.append(v * 1.0 / total)
        # print(data1)
        # print(data2)
        # print(data)
        # print(ret)
        pros = []
        count = [i for i in range(n,6*n+1)]
        for i in range(0,len(data)):
            pros.append([count[i],ret[i]])

        # print(pros)
        return pros

        # #另一种方式得到data，即计算频数
        # dp = [[0 for i in range(6 * n)] for i in range(n)]
        # for i in range(6):
        #     dp[0][i] = 1
        # print(dp)
        # for i in range(1, n):  # 1，相当于2个骰子。
        #     for j in range(i, 6 * (i + 1)):  # [0,i-1]的时候，频数为0（例如2个骰子不可能投出点数和为1）
        #         dp[i][j] = dp[i - 1][j - 6] + dp[i - 1][j - 5] + dp[i - 1][j - 4] + \
        #                    dp[i - 1][j - 3] + dp[i - 1][j - 2] + dp[i - 1][j - 1]
        #
        # count = dp[n - 1]
        # return count

    # 递归写法得到频数
    def dicesSum(self, n):
        # Write your code here
        for i in range(n,6*n+1):
            resCount = self.getNSumCount(n,i)
            print(n,i,resCount)

    def getNSumCount(self,n,sum):
        if n<1 or sum<n or sum>6*n:
            return 0
        if n==1:
            return 1
        resCount = 0
        resCount = self.getNSumCount(n-1,sum-1) + \
                   self.getNSumCount(n-1,sum-2) + \
                   self.getNSumCount(n-1,sum-3) + \
                   self.getNSumCount(n-1,sum-4) + \
                   self.getNSumCount(n-1,sum-5) + \
                   self.getNSumCount(n-1,sum-6)
        return resCount


sol = Solution()
# newS = sol.dicesSum(1)
# print(newS)
newS = sol.dicesSum(3)
print(newS)
# Example Given n = 1, return [ [1, 0.17], [2, 0.17], [3, 0.17], [4, 0.17], [5, 0.17], [6, 0.17]].

# 思路：n出现的可能是前面n-1到n-6出现可能的和，设置两个数组，分别保存每一轮