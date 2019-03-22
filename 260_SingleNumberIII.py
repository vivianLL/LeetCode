'''
260. Single Number III
Medium

https://leetcode.com/problems/single-number-iii/
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
'''
class Solution:
    def singleNumber(self, nums):
        # # 用集合 时间复杂度O(n) 空间复杂度最坏O(n)
        # seen = set()
        # for i in nums:
        #     if i not in seen:
        #         seen.add(i)
        #     else:
        #         seen.remove(i)
        # return list(seen)

        # 异或 时间复杂度O(n) 空间复杂度O(1)
        if not nums: return []
        temp = 0            # 所有元素与0异或时，结果均不变
        for num in nums:
            temp ^= num
        idx = 0              # 获取temp中最低位1的位置
        while temp & 1 ==0:  # 和1按位与为0则说明最低位不为1
            temp = temp>>1
            idx += 1
        a = b = 0
        for num in nums:
            if self.isBit(num,idx):
                a ^=num
            else:
                b ^=num
        return [a,b]

    def isBit(self,num,idx):   # 判断num的二进制从低到高idx位是不是1
        num = num>>idx
        return num & 1

sol = Solution()
print(sol.singleNumber([2,5,6,6,3,2,4,4]))


# 思路：任何一个数字异或他自己都等于0，0异或任何一个数都等于那个数。
# 数组中出了两个数字之外，其他数字都出现两次，那么我们从头到尾依次异或数组中的每个数，那么出现两次的数字都在整个过程中被抵消掉，那两个不同的数字异或的值不为0，也就是说这两个数的异或值中至少某一位为1。
# 我们找到结果数字中最右边为1的那一位i，然后一次遍历数组中的数字，如果数字的第i位为1，则数字分到第一组，数字的第i位不为1，则数字分到第二组。
# 这样任何两个相同的数字就分到了一组，而两个不同的数字在第i位必然一个为1一个不为1而分到不同的组，然后再对两个组依次进行异或操作，最后每一组得到的结果对应的就是两个只出现一次的数字。
# 参考网址：https://blog.csdn.net/lrs1353281004/article/details/81187971