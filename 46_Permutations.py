'''
46. Permutations
Medium

https://leetcode.com/problems/permutations/
Given a collection of distinct integers, return all possible permutations.
'''
class Solution:
    def permute(self, nums):
    #     if not nums:
    #         return []
    #     res = []
    #     self.helper(nums, res, '')
    #     return sorted(list(set(res)))
    #
    # def helper(self, nums, res, path):
    #     print("nums:",nums,"res:",res,"path:",path)
    #     if not nums:
    #         res.append(path)
    #     else:
    #         for i in range(len(nums)):
    #             self.helper(nums[:i] + nums[i + 1:], res, path + nums[i])
        if not nums:
            return []
        def permutation(nums,begin):
            if begin=='':
                print(nums)
            else:
                for i in range(begin,len(begin))




sol = Solution()
# ans = sol.permute([1,2,3])
ans = sol.permute("123")
print(ans)