'''
77. Combinations
Medium

https://leetcode.com/problems/combinations/
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
'''
import itertools
import copy

class Solution:
    # # DFS 递归
    # def combine(self, n: int, k: int):
    #     ans = []
    #     # self.dfs([i for i in range(1,n+1)],k,ans,[])
    #     self.dfs(range(1, n + 1), k, ans, [])
    #     return ans
    #
    # def dfs(self,nums,k,ans,path):
    #     print(nums,k,ans,path)
    #     if k > len(nums):
    #         return
    #     elif k == 0:
    #         ans.append(path)
    #     else:
    #         for i in range(len(nums)):
    #             print(i)
    #             self.dfs(nums[i+1:],k-1,ans,path+[nums[i]])

    # # 另一个版本的DFS
    # def combine(self, n, k):
    #     res = []
    #     out = []
    #     self.n = n + 1
    #     self.k = k
    #     self.DFS(1, out, res)
    #     return res
    #
    # def DFS(self, level, out, res):
    #     if len(out) == self.k:
    #         res.append(copy.deepcopy(out))
    #         return
    #     for i in range(level, self.n):
    #         out.append(i)
    #         self.DFS(i + 1, out, res)
    #         out.pop()


    # # 内置函数
    # def combine(self, n: int, k: int):
    #     return list(itertools.combinations(range(1, n + 1), k))  # 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序

    # 迭代
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = list()
        pool = [i for i in range(1, n + 1)]
        if k > n:
            return
        indices = [i for i in range(k)]
        result.append([pool[i] for i in indices])
        print(result)
        while True:
            for i in reversed(range(k)):
                if indices[i] != i + n - k:
                    break  # 可以理解为goto
            else:
                return result

            indices[i] += 1  # goto 到这个位置
            for j in range(i + 1, k):
                indices[j] = indices[j - 1] + 1
            result.append([pool[i] for i in indices])
            print(result)

sol = Solution()
ans = sol.combine(4,3)
print(ans)