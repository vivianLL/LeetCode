'''
136. Single Number
Easy

https://leetcode.com/problems/single-number/
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution:
    def singleNumber(self, nums) -> int:
        if nums==[]:return None
        temp = 0
        for num in nums:
            temp ^= num
        return temp

        # # 数学法
        # return 2 * sum(set(nums)) - sum(nums)

# 思路：遍历时新建列表并查找、哈希表、数学法、异或法