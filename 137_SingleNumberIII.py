'''
137. Single Number II
Medium

https://leetcode.com/problems/single-number-ii/
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution:
    def singleNumber(self, nums) -> int:
        if nums==None or nums==[]: return False
        res = 0
        for i in range(32):
            sum = 0
            for num in nums:
                if num & 1<<i:   # 先算1<<i，再算&
                    sum += 1     # 这两句也可为sum += (num>>i) & 1
            if sum % 3 != 0:     # 若能被3整除，则该位是0，不变
                res |=  1<<i     # 只出现一次的数字不能被三整除的那一位是1，用或置1
        if res >= 2**31:         # 32位整数-2^31~2^31-1
            res -= 2**32
        return res

sol = Solution()
print(sol.singleNumber([2,-6,-6,-6,2,2,-4]))

# 思路：把32位的二进制数进行遍历，统计每个数字的每一位出现的和。
# 因为每个数字出现了3次或者1次，所以如果某一位出现的次数不是3次，那么这个位置一定是因为那个只出现1次的数字导致的。
# 用来保存结果的res是0，因此使用或操作，就能把这个位置的数字变成1.
# 需要注意的是：python的整型没有最大值，所以，当输入是一堆负数的时候，会导致认为结果是个整数！因为32位有符号的被认为成了无符号的，所以这就是Python的一个坑。。
# 注意一下结论，以后出现位运算的时候，需要对结果进行判断一下最好。如果不在这个范围内，说明了结果被认为是无符号的数了，需要减去2 ^ 32。
