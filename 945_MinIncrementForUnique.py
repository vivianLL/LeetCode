'''
945. 使数组唯一的最小增量
Medium

https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
返回使 A 中的每个值都是唯一的最少操作次数。
'''
class Solution:
    def minIncrementForUnique(self, A):
        # # 我的方法 暴力递增 超时
        # count = 0
        # nums = set()
        # for x in A:
        #     if x not in nums:
        #         nums.add(x)
        #     else:
        #         if x+1 not in nums:
        #             nums.add(x+1)
        #             count += 1
        #         else:
        #             i = 1
        #             while x+i in nums:
        #                 i += 1
        #             nums.add(x+i)
        #             count += i
        # return count


        # # 我的方法的优化 先排序后遍历
        # A.sort()
        # count = 0
        # for i in range(1,len(A)):
        #     if A[i]<=A[i-1]:
        #         count += A[i - 1] + 1 - A[i]
        #         A[i] = A[i-1]+1
        # return count

        # 再优化 先计数后遍历 时间复杂度 O(n + k)O(n+k)
        count = [0] * 40000
        for x in A:
            count[x] += 1
        maxnum = max(A)   # 数组中的最大值
        res = 0
        for i in range(maxnum):
            if count[i]>1:
                res += count[i] - 1              # 有count[i]-1个数需要增加
                count[i+1] += count[i] - 1

        if count[maxnum]>1:                     # 单独计算，因为可能超出40000的边界
            d = count[maxnum]-1                 # 有d个数需要增加
            res += (1+d)*d//2                   # 分别增加为max+1，max+2，...max+d，使用等差数列公式求和
        return res


        # # 官方方法一：计数 比较难理解
        # count = [0] * 80000
        # for x in A:
        #     count[x] += 1
        #
        # ans = taken = 0
        # for x in range(80000):
        #     if count[x] >= 2:
        #         taken += count[x] - 1
        #         ans -= x * (count[x] - 1)
        #     elif taken > 0 and count[x] == 0:
        #         taken -= 1
        #         ans += x
        #
        # return ans


sol = Solution()
ans = sol.minIncrementForUnique([3,2,1,2,1,7])
print(ans)
sol = Solution()
ans = sol.minIncrementForUnique([1,2,2])
print(ans)
sol = Solution()
ans = sol.minIncrementForUnique([1,3,0,3,0])
print(ans)