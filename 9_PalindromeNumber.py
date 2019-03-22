'''
9. Palindrome Number
Easy

https://leetcode.com/problems/palindrome-number/
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # # 我的写法
        # if x is None: return False
        # s = str(x)                  # O(n)空间复杂度
        # i=0
        # while i <=(len(s)//2):
        #     if s[i]!=s[-1-i]:
        #         return False
        #     i += 1
        # return True

        # # 较快的写法
        # if x < 0:                # 负数因为有负号，直接为False，节省时间
        #     result = False
        # else:
        #     strx = str(x)
        #     result = strx == strx[::-1]
        # return result

        # # 不把整数转换成字符串 将整个数取反后看和原来的数是否相同 注意直接逆序整数在其他语言里可能会溢出 可考虑定义长整型
        # if x < 0:
        #     return False
        # elif x == 0:
        #     return True
        # elif x % 10 == 0:
        #     return False
        # else:
        #     def rev(x):
        #         reverse = 0
        #         temp = x
        #         while temp != 0:
        #             reverse = reverse * 10 + temp % 10
        #             temp = temp // 10
        #         return reverse
        #     print(x)
        #     print(rev(x))
        #     return x == rev(x)

        # 只需要判断左边一半和翻转后的右边一半是否相等即可
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while (x > rev):             # 注意循环中止条件
            rev = rev * 10 + x % 10  # 将低位一半的数取反
            x = x // 10
        return x == rev or x == int(rev / 10)     # 有rev >= x， 奇数情况下需要除去10


sol = Solution()
ans = sol.isPalindrome(31013)
print(ans)