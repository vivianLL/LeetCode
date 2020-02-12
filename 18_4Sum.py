'''
18. 4Sum
Medium

https://leetcode.com/problems/4sum/
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Note:
The solution set must not contain duplicate quadruplets.
'''
class Solution:
    def fourSum(self, nums, target):
        # # 三重循环 先排序 最外层循环遍历第一个数，后面两个数j，k在每次最外层循环开始时，取i+1和len(nums)-1，就是i之后的一头一尾。nums[i]+nums[j]+nums[k]如果小于0那就是nums[j]不够大，我们把j后移一个，如果大于0那就是nums[k]太大了，我们把k前移一个。
        # res = []
        # nums.sort()
        # for j in range(len(nums)):
        #     for i in range(j+1,len(nums) - 2):
        #         # 第二第三个数：一头一尾
        #         l, r = i + 1, len(nums) - 1
        #         while l < r:
        #             s = nums[j] + nums[i] + nums[l] + nums[r]
        #             if s < target:
        #                 l += 1
        #             elif s > target:
        #                 r -= 1
        #                 # 分支应该写清楚
        #             else:
        #                 if [nums[j], nums[i], nums[l], nums[r]] not in res:
        #                     res.append([nums[j], nums[i], nums[l], nums[r]])
        #                 # 考虑过的l就不要考虑了
        #                 while l < r and nums[l] == nums[l + 1]:
        #                     l += 1
        #                 while l < r and nums[r] == nums[r - 1]:
        #                     r -= 1
        #                     # 请记住一定要写这个变化条件。。
        #                 l += 1
        #                 r -= 1
        # return res

        # # 建立一个字典dict，字典的key值为数组中每两个元素的和，两重循环，平均O(n^2 )，最坏O(n^4 )
        # numLen, res, num_dict = len(nums), set(), {}
        # if numLen < 4:
        #     return []
        # nums.sort()   # 不能省略
        # for p in range(numLen):  # 存储hash表
        #     for q in range(p + 1, numLen):
        #         if nums[p] + nums[q] not in num_dict:
        #             num_dict[nums[p] + nums[q]] = [(p, q)]
        #         else:
        #             num_dict[nums[p] + nums[q]].append((p, q))
        # print(num_dict)
        # for i in range(numLen):
        #     for j in range(i + 1, numLen - 2):
        #         T = target - nums[i] - nums[j]
        #         if T in num_dict:
        #             for k in num_dict[T]:
        #                 if k[0] > j: res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        # return [list(i) for i in res]

        # k Sum 的一般解法
        def findNSum(nums, l, r, target, N, result, results):
            if N < 2 or r - l + 1 < N or target < nums[l] * N or target > nums[r] * N:
                return

            if N == 2:
                while l < r:
                    value = nums[l] + nums[r]
                    if value == target:
                        results.append(result + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1;
                        r -= 1
                    elif value > target:
                        r -= 1
                    else:
                        l += 1
            else:  # Reduce to N-1
                for i in range(l, r + 1):
                    if i > l and nums[i] == nums[i - 1]:
                        continue
                    findNSum(nums, i + 1, r, target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        nums.sort()
        findNSum(nums, 0, len(nums) - 1, target, 4, [], results)
        return results


sol = Solution()
ans = sol.fourSum([-1, 0, 1, 2, 0, -2], 3)
print(ans)
sol = Solution()
ans = sol.fourSum([0,0,0,0,], 1)
print(ans)