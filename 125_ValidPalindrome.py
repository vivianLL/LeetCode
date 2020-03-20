'''
125. Valid Palindrome
Easy

https://leetcode.com/problems/valid-palindrome/
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 我的方法
        # if s=="":
        #     return True
        # s = ''.join(list(filter(str.isalnum, s))).lower()
        # print(s)
        # left = 0
        # right = len(s)-1
        # while left <= right:
        #     if s[left]!=s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        # 最简练的方法
        s1 = [*filter(str.isalnum, s.lower())]   # *用于 unpack 可迭代的变量
        return s1 == s1[::-1]

sol = Solution()
ans = sol.isPalindrome("A man, a plan, a canal: Panama")
print(ans)
ans = sol.isPalindrome("race a car")
print(ans)

