'''
268. Missing Number
Easy

https://leetcode.com/problems/missing-number/
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
'''
class Solution:
    def missingNumber(self, nums) -> int:
        # # 排序后遍历 时间复杂度O(nlogn) 或排序后二分查找 target是数组中第一个数值和下标不相等的下标
        # if nums == [1]: return 0
        # if nums == [0]: return 1
        # nums = sorted(nums)
        # for i in range(len(nums) - 1):
        #
        #     if nums[i + 1] - nums[i] != 1:
        #         return i + 1
        # if nums[0] == 0:
        #     return i + 2
        # else:
        #     return 0

        # 哈希表 时间复杂度O(n) 空间复杂度O(n)
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

        # # 公式计算数组之和 时间复杂度O(n) 空间复杂度O(1)
        # n = len(nums)
        # targetsum = n*(n+1)//2   # 返回为int型，所以应为//。注意此处为n+1，因为数组缺一个数，原本应该有n+1个数
        # print(targetsum)
        # sum = 0
        # for num in nums:
        #     sum+=num
        # print(sum)
        # return targetsum-sum

        # 位运算 异或 时间复杂度O(n) 空间复杂度O(1)
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


sol = Solution()
ans = sol.missingNumber([9,6,4,2,3,5,7,0,1])
print(ans)
# 思路：a ^ a = 0, a ^ b ^ a = b, a ^ b ^ c = a ^ c ^ b
# 1. 若两个元素相等，则异或结果为0
# 2. 所有元素与0异或时，结果均不变
# 3. 异或运算满足交换律
# 异或例子参考solution
