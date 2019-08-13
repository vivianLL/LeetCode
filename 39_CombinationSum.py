'''
39. Combination Sum
Medium

https://leetcode.com/problems/combination-sum/
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''
class Solution:
    def combinationSum(self, candidates, target):
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
            if i > index and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:  # candidates有序，只要当前大于目标，后面都大于，直接break
                break  # 或 break
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

sol = Solution()
ans = sol.combinationSum([2,3,6,7,9], 7)
print(ans)

# 解题思路：穷举出符合条件的组合，我们一般考虑dfs。