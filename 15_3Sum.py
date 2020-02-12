'''
15. 3Sum
Medium

https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:The solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums):
        # # 三重循环 超时
        # if len(nums) <= 2:
        #     return []
        # setlist = []
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 if {nums[i],nums[j],nums[k]} not in setlist:
        #                     setlist.append({nums[i],nums[j],nums[k]})
        #                     ans.append([nums[i],nums[j],nums[k]])
        #                 else:
        #                     continue
        # return ans

        # # 两重循环 超时
        # if len(nums) <= 2:
        #     return []
        # setlist = []
        # ans = []
        #
        # for i in range(len(nums)):
        #     ansdict = {}           # 注意位置
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] not in ansdict:
        #             ansdict[-nums[i]-nums[j]] = nums[j]
        #         else:
        #             if {nums[i], ansdict[nums[j]], nums[j]} not in setlist:
        #                 setlist.append({nums[i], nums[j], ansdict[nums[j]]})
        #                 ans.append([nums[i], nums[j], ansdict[nums[j]]])
        #             else:
        #                 continue
        #
        # return ans

        # 二重循环 先排序 最外层循环遍历第一个数，后面两个数j，k在每次最外层循环开始时，取i+1和len(nums)-1，就是i之后的一头一尾。nums[i]+nums[j]+nums[k]如果小于0那就是nums[j]不够大，我们把j后移一个，如果大于0那就是nums[k]太大了，我们把k前移一个。
        res = []
        nums.sort()
        for i in range(len(nums)-2):
        	#考虑过的i就不用再考虑了
            if i > 0 and nums[i] == nums[i-1]:
                continue
                #第二第三个数：一头一尾
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                elif s > 0:
                    r -= 1
                    #分支应该写清楚
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    #考虑过的l就不要考虑了
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                        #请记住一定要写这个变化条件。。
                    l += 1; r -= 1
        return res



sol = Solution()
ans = sol.threeSum([-1, 0, 1, 2, -1, -4])
print(ans)
