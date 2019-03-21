'''
263. Ugly Number
Easy

https://leetcode.com/problems/ugly-number/
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
'''
class Solution:
    def isUgly(self, num: int) -> bool:
        if num<=0:return False  # 注意0和负数 0进入循环后一直为0，死循环
        while num % 2 == 0:
            num = num//2
        while num %3 ==0:
            num = num//3
        while num %5 ==0:
            num = num//5
        if num==1:       # 不用列在前面
            return True
        else:
            return False
        # 或 return num==1

sol = Solution()
ans = sol.isUgly(0.7)
print(ans)