'''
40. Combination Sum II
Medium

https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''


class Solution:
    def combinationSum2(self, candidates, target):
        # DFS 深度优先搜索
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:   # 如果在这一层递归的时候有重复数据 比如有两个1， 那之前做一次1的时候，第二次就不处理了，不然会重复
                continue
            if nums[i] > target:
                break
            self.dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)  # 因为不能重复，所以从i+1开始


sol = Solution()
ans = sol.combinationSum2([10,1,2,7,6,1,5],8)
print(ans)

# 解题思路：穷举出符合条件的组合，我们一般考虑dfs。