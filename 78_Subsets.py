'''
78. Subsets
Medium

https://leetcode.com/problems/subsets/
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
'''
import copy
class Solution:
    def subsets(self, nums):
        res = []
        for i in range(len(nums)+1):
            ans = []
            self.dfs(nums, i, ans, [])
            res.extend(ans)
        return res


    def dfs(self,nums,k,ans,path):
        # print(nums,k,ans,path)
        if k > len(nums):
            return
        elif k == 0:
            ans.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[i+1:],k-1,ans,path+[nums[i]])

sol = Solution()
ans = sol.subsets([1,2,3])
print(ans)
ans = sol.subsets([-1,0])
print(ans)
# 思路类似于77.组合