'''
58. Length of Last Word
Easy

https://leetcode.com/problems/length-of-last-word/
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # # 自写
        # s = s.strip(' ')  # 去除字符串后面的空格
        # for i in reversed(range(len(s))):
        #     if s[i] == ' ':
        #         return len(s)-i-1
        # return len(s)

        # 更快
        words = s.split()  # 同时去除字符串后面的空格和将字符串用空格分成list
        if len(words):
            return len(words.pop())
        else:
            return 0

sol = Solution()
ans = sol.lengthOfLastWord("  ab abc ")
print(ans)